import java.util.ArrayList;
import java.util.List;

public class ReportJob {
    private List<SaleRow> rows;
    private String title;

    public void prepare(String title, List<Sale> sales) {
        this.title = title;
        rows = new ArrayList<>();
        for (Sale sale : sales) {
            rows.add(new SaleRow(
                sale.product(), sale.units(), sale.units() * sale.unitPrice()
            ));
        }
    }

    public String run(String format) {
        if (rows == null) {
            throw new IllegalStateException("Call prepare() before run()");
        }
        String content;
        if (format.equals("csv")) {
            content = new CsvReportWriter().writeCsv(rows);
        } else if (format.equals("json")) {
            content = new JsonReportWriter().writeJson(rows);
        } else {
            throw new IllegalArgumentException("Unknown format: " + format);
        }
        System.out.println("Exported " + title + " as " + format.toUpperCase());
        return content;
    }
}
