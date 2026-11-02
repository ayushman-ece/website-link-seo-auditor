from auditor import crawl_website, generate_report


def main():
    website = "https://www.python.org"

    print("=" * 45)
    print("       WEBSITE LINK & SEO AUDITOR")
    print("=" * 45)

    results = crawl_website(
        website,
        max_pages=10
    )

    generate_report(results)

    successful = sum(
        1 for page in results
        if page["status"] != "ERROR"
    )

    print("\n========== AUDIT SUMMARY ==========")
    print(f"Pages scanned: {len(results)}")
    print(f"Successful pages: {successful}")
    print(f"Failed pages: {len(results) - successful}")


if __name__ == "__main__":
    main()