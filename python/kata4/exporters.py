import csv
import io
import json
from abc import ABC, abstractmethod


class Exporter(ABC):
    @abstractmethod
    def to_csv(self, records):
        raise NotImplementedError

    @abstractmethod
    def to_json(self, records):
        raise NotImplementedError

    @abstractmethod
    def to_html(self, records):
        raise NotImplementedError


class CsvExporter(Exporter):
    def to_csv(self, records):
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=["product", "units", "revenue"])
        writer.writeheader()
        writer.writerows(records)
        return output.getvalue()

    def to_json(self, records):
        raise NotImplementedError("CSV exporter cannot produce JSON")

    def to_html(self, records):
        raise NotImplementedError("CSV exporter cannot produce HTML")


class JsonExporter(Exporter):
    def to_csv(self, records):
        raise NotImplementedError("JSON exporter cannot produce CSV")

    def to_json(self, records):
        return json.dumps(records, indent=2)

    def to_html(self, records):
        raise NotImplementedError("JSON exporter cannot produce HTML")


class HtmlExporter(Exporter):
    def to_csv(self, records):
        raise NotImplementedError("HTML exporter cannot produce CSV")

    def to_json(self, records):
        raise NotImplementedError("HTML exporter cannot produce JSON")

    def to_html(self, records):
        rows = "".join(
            f"<tr><td>{r['product']}</td><td>{r['units']}</td>"
            f"<td>{r['revenue']}</td></tr>"
            for r in records
        )
        return "<table><tr><th>Product</th><th>Units</th><th>Revenue</th></tr>" + rows + "</table>"
