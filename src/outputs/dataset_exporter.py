thonpython
import json
import csv
import logging

logging.basicConfig(level=logging.INFO)

class DatasetExporter:
    def export(self, data, fmt: str, output_path: str):
        fmt = fmt.lower()

        if fmt == "json":
            self._export_json(data, output_path)
        elif fmt == "csv":
            self._export_csv(data, output_path)
        else:
            logging.error(f"Unsupported export format: {fmt}")

    def _export_json(self, data, output_path):
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        logging.info("JSON export completed.")

    def _export_csv(self, data, output_path):
        if not data:
            logging.warning("No data to export as CSV.")
            return

        headers = data[0].keys()

        with open(output_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)

        logging.info("CSV export completed.")