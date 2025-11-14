thonpython
import logging
from urllib.parse import urljoin
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)

class PaginationHandler:
    def detect_next_page(self, html: str, base_url: str):
        soup = BeautifulSoup(html, "html.parser")

        link = soup.find("a", string=lambda s: s and "next" in s.lower())
        if not link:
            logging.info("No next page found.")
            return None

        href = link.get("href")
        if not href:
            return None

        return urljoin(base_url, href)