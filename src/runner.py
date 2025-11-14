thonpython
import json
import logging
from pathlib import Path

from extractors.dynamic_loader import DynamicLoader
from extractors.table_detector import TableDetector
from extractors.pagination_handler import PaginationHandler
from outputs.dataset_exporter import DatasetExporter

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def load_config(config_path: str):
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)

def scrape_page(url: str):
    loader = DynamicLoader()
    html = loader.fetch(url)

    detector = TableDetector()
    rows = detector.extract_table_rows(html)

    return rows

def scrape_with_pagination(start_url: str, max_pages: int = 3):
    loader = DynamicLoader()
    paginator = PaginationHandler()

    results = []
    current_url = start_url

    for _ in range(max_pages):
        logging.info(f"Scraping: {current_url}")
        html = loader.fetch(current_url)

        detector = TableDetector()
        rows = detector.extract_table_rows(html)
        results.extend(rows)

        next_url = paginator.detect_next_page(html, current_url)
        if not next_url:
            break
        current_url = next_url

    return results

def main():
    config_path = Path("data/sample-input.json")
    config = load_config(config_path)

    url = config.get("url")
    pagination = config.get("pagination", False)
    max_pages = config.get("max_pages", 1)
    export_format = config.get("export_format", "json")

    if pagination:
        data = scrape_with_pagination(url, max_pages=max_pages)
    else:
        data = scrape_page(url)

    exporter = DatasetExporter()
    output_path = "data/example-output.json"
    exporter.export(data, export_format, output_path)

    logging.info(f"Export complete → {output_path}")

if __name__ == "__main__":
    main()