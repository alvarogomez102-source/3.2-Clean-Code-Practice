from exporters import CsvExporter, HtmlExporter, JsonExporter
from python.kata4 import exporters


class ExportJob:
    def __init__(self, title, sales):
        self.title = title
        self.records = [
            {
                "product": sale.product,
                "units": sale.units,
                "revenue": round(sale.units * sale.unit_price, 2)
            } for sale in sales
        ]

    def run(self, format_name):
        if self.records is None:
            raise RuntimeError("Call prepare() before run()")
        exporters = {
            "csv": (CsvExporter, "to_csv"),
            "json": (JsonExporter, "to_json"),
            "html": (HtmlExporter, "to_html")
        }

        if format_name not in exporters:
            raise ValueError("Unknown format")

        exporter_class, method_name = exporters[format_name]
        exporter = exporter_class()
        content = getattr(exporter, method_name)(self.records)
        print(f"Exported {self.title} as {format_name.upper()}")
        return content
