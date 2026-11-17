from exporters import CsvExporter, HtmlExporter, JsonExporter


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
        if format_name == "csv":
            exporter = CsvExporter()
            content = exporter.to_csv(self.records)
        elif format_name == "json":
            exporter = JsonExporter()
            content = exporter.to_json(self.records)
        elif format_name == "html":
            exporter = HtmlExporter()
            content = exporter.to_html(self.records)
        else:
            raise ValueError("Unknown format")
        print(f"Exported {self.title} as {format_name.upper()}")
        return content
