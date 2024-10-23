# SCT_SD_4
 skillcraft technology internship - 4th project
# E-commerce Product Scraper

This project is a Python-based web scraping tool that extracts essential product information, such as names, prices, and ratings, from various e-commerce websites and stores the data in a structured format like a CSV file. The tool leverages the `BeautifulSoup` and `requests` libraries to parse web content and gather data.

## Features

- **Web Scraping Across Various E-commerce Websites**: Capable of scraping product details from different online stores.
- **Data Storage in CSV Format**: The scraped data is stored in a CSV file, making it easy to analyze.
- **Customizable Scraping Logic**: The scraping selectors can be modified to suit the structure of the target website for more accurate results.
- **Error Handling**: Gracefully handles cases where certain data points might be missing.
- **User-Agent Rotation**: Rotates user-agents to prevent scraping bans and mimics different browsers for smoother scraping.

## Prerequisites

Before running the script, make sure you have the following Python libraries installed:

```bash
pip install requests
pip install beautifulsoup4
pip install pandas
