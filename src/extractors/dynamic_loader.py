thonpython
import logging
import requests

logging.basicConfig(level=logging.INFO)

class DynamicLoader:
    def fetch(self, url: str) -> str:
        logging.info(f"Fetching URL: {url}")
        try:
            resp = requests.get(url, timeout=15, headers={
                "User-Agent": "Mozilla/5.0"
            })
            resp.raise_for_status()
            return resp.text
        except Exception as e:
            logging.error(f"Fetch failed: {e}")
            return ""