import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque
import csv
import time


def fetch_page(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        title = (
            soup.title.get_text(strip=True)
            if soup.title else "No Title"
        )

        description_tag = soup.find(
            "meta", attrs={"name": "description"}
        )

        description = (
            description_tag.get("content", "").strip()
            if description_tag else "No Description"
        )

        return response, soup, title, description

    except requests.RequestException as error:
        print(f"Error fetching {url}: {error}")
        return None, None, None, None
    


def extract_internal_links(soup, base_url):
    internal_links = set()

    base_domain = urlparse(base_url).netloc

    for tag in soup.find_all("a", href=True):
        href = tag["href"].strip()

        if not href:
            continue

        absolute_url = urljoin(base_url, href)
        parsed_url = urlparse(absolute_url)

        if (
            parsed_url.scheme in ("http", "https")
            and parsed_url.netloc == base_domain
        ):
            clean_url = parsed_url._replace(
                fragment=""
            ).geturl()

            internal_links.add(clean_url)

    return internal_links

def crawl_website(start_url, max_pages=10):
    queue = deque([start_url])
    visited = set()
    results = []

    while queue and len(visited) < max_pages:
        current_url = queue.popleft()

        if current_url in visited:
            continue

        visited.add(current_url)

        print(f"\nScanning: {current_url}")

        start_time = time.perf_counter()

        response, soup, title, description = fetch_page(current_url)

        response_time = round(
            (time.perf_counter() - start_time) * 1000, 2
        )

        if response is None:
            results.append({
                "url": current_url,
                "status": "ERROR",
                "title": "N/A",
                "description": "N/A",
                "response_time_ms": response_time,
                "links_found": 0
            })
            continue

        links = extract_internal_links(soup, current_url)

        results.append({
            "url": current_url,
            "status": response.status_code,
            "title": title,
            "description": description,
            "response_time_ms": response_time,
            "links_found": len(links)
        })

        for link in links:
            if link not in visited and link not in queue:
                queue.append(link)

    return results


def generate_report(results):
    fieldnames = [
        "url",
        "status",
        "title",
        "description",
        "response_time_ms",
        "links_found"
    ]

    with open(
        "audit_report.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(results)

    print("\nSEO audit report generated successfully!")
    print("File: audit_report.csv")