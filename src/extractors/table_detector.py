thonpython
import logging
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)

class TableDetector:
    def extract_table_rows(self, html: str):
        soup = BeautifulSoup(html, "html.parser")
        table = soup.find("table")

        if not table:
            logging.warning("No table found on page.")
            return []

        rows = []
        headers = [th.get_text(strip=True) for th in table.find_all("th")]

        for tr in table.find_all("tr"):
            cells = tr.find_all(["td", "th"])
            if not cells:
                continue
            row = {headers[i] if i < len(headers) else f"col_{i}": cell.get_text(strip=True)
                   for i, cell in enumerate(cells)}
            rows.append(row)

        return rows