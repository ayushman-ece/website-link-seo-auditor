# 🔍 Website Link & SEO Auditor

<p align="center">
  <strong>A Python-powered website auditing tool that crawls internal pages, extracts SEO metadata, checks HTTP responses, and generates structured audit reports.</strong>
</p>

<p align="center">
  ![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
  ![Requests](https://img.shields.io/badge/HTTP-Requests-green)
  ![BeautifulSoup](https://img.shields.io/badge/HTML-BeautifulSoup-orange)
  ![Project](https://img.shields.io/badge/Project-Completed-success)
</p>

---

## 📌 Project Overview

**Website Link & SEO Auditor** is a Python-based web crawling and auditing application designed to inspect website pages, discover internal links, extract SEO metadata, measure response times, and identify unsuccessful HTTP requests.

The application uses web scraping and crawling techniques to explore a website and generate a structured CSV report containing important page information.

## 🎯 Project Objectives

- Crawl multiple pages within a website.
- Discover and extract internal links.
- Avoid duplicate URL processing.
- Extract page titles and meta descriptions.
- Identify unsuccessful HTTP responses.
- Measure page response times.
- Generate structured website audit reports.

## ✨ Key Features

| Feature | Description |
|---|---|
| 🌐 Website Crawling | Automatically discovers and scans internal pages. |
| 🔗 Internal Link Extraction | Extracts internal links from HTML pages. |
| 🔄 Duplicate Prevention | Uses sets to avoid repeatedly adding the same URLs. |
| 📝 SEO Metadata Extraction | Collects page titles and meta descriptions. |
| 🚨 HTTP Error Detection | Identifies unsuccessful requests and HTTP errors. |
| ⚡ Response-Time Measurement | Measures request duration in milliseconds. |
| 📊 CSV Reporting | Exports website audit results into a CSV file. |
| 🔢 Page Limit Control | Limits the maximum number of pages scanned. |

## ⚙️ How It Works

1. **Initialize Crawler:** Start with the website's homepage.
2. **Fetch HTML:** Send HTTP requests using the Requests library.
3. **Parse HTML:** Process website content using BeautifulSoup.
4. **Extract Metadata:** Collect page titles and meta descriptions.
5. **Discover Links:** Find internal links and convert relative URLs into absolute URLs.
6. **Manage Crawling:** Use a queue and visited set to manage page discovery and avoid duplicate processing.
7. **Measure Performance:** Calculate HTTP request duration.
8. **Generate Report:** Export the collected information into a CSV file.

## 🧰 Technologies Used

- **Python 3** – Core programming language.
- **Requests** – HTTP requests and response handling.
- **BeautifulSoup4** – HTML parsing and metadata extraction.
- **urllib.parse** – URL parsing and resolution.
- **collections.deque** – Queue-based crawling.
- **CSV** – Structured audit reporting.
- **time** – Performance measurement.

## 📂 Project Structure

```text
website-link-seo-auditor/
│
├── main.py              # Application entry point
├── auditor.py           # Crawling and auditing logic
├── requirements.txt     # Project dependencies
├── .gitignore           # Git ignored files
└── README.md             # Project documentation
```

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ayushman-ece/website-link-seo-auditor.git
```

### 2. Navigate to the Project

```bash
cd website-link-seo-auditor
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Environment

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
python main.py
```

## 📊 Sample Output

```text
=============================================
       WEBSITE LINK & SEO AUDITOR
=============================================

Scanning: https://www.python.org

Scanning: https://www.python.org/about/

SEO audit report generated successfully!
File: audit_report.csv

========== AUDIT SUMMARY ==========
Pages scanned: 10
Successful pages: 10
Failed pages: 0
```

*Illustrative output. Actual results depend on website structure and network conditions.*

## 📁 Generated Audit Report

The application generates:

`audit_report.csv`

The report contains:

| Column | Description |
|---|---|
| URL | Scanned page address |
| Status | HTTP response status or ERROR |
| Title | Extracted HTML page title |
| Description | Extracted meta description |
| Response Time | HTTP request duration in milliseconds |
| Links Found | Number of unique internal links discovered on the page |

## 🧠 Python Concepts Practiced

- HTTP requests and response handling.
- HTML parsing using BeautifulSoup.
- URL parsing and resolution.
- Queue-based crawling using `deque`.
- Duplicate prevention using `set`.
- Dictionaries and lists.
- Exception handling.
- CSV file handling.
- Modular programming.
- Performance measurement.

## ⚠️ Current Limitations

- Only internal HTTP/HTTPS links are crawled.
- External links are not independently checked.
- Crawling is limited to a configured maximum number of pages.
- Dynamic JavaScript-generated content may not be captured.
- SEO analysis currently extracts metadata but does not calculate an SEO quality score.
- The crawler does not implement automatic background scheduling.
- No graphical dashboard or notifications are included.

## 🔮 Future Improvements

- 🌍 External link validation.
- 📈 SEO quality scoring.
- 🚨 Detailed broken-link reporting.
- 📊 Interactive website audit dashboard.
- 🗄️ SQLite database integration.
- 🔄 Scheduled website auditing.
- 📩 Email and Telegram notifications.
- 🧠 Advanced SEO recommendations.

## 👨‍💻 Author

**Ayushman Tiwari**

🎓 B.Tech Student | Python Developer | AI & Machine Learning Enthusiast

🔗 GitHub: [@ayushman-ece](https://github.com/ayushman-ece)

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

<p align="center">
  <strong>🚀 Part of My Daily Python Project Development Journey</strong>
  <br>
  <em>Learning by building. Improving through practice. Growing one project at a time.</em>
</p>