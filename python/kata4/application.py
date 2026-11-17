from job import ExportJob
from sale import Sale


class ExportApplication:
    def run(self):
        sales = [Sale("Keyboard", 3, 45.0), Sale("Mouse", 5, 18.0)]
        job = ExportJob()
        job.prepare("Weekly sales", sales)
        print(job.run("csv"))
        print(job.run("json"))
