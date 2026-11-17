import java.util.List;
import java.util.Locale;

public class CsvReportWriter implements ReportWriter {
    public String writeCsv(List<SaleRow> rows) {
        StringBuilder result = new StringBuilder("product,units,revenue\n");
        for (SaleRow row : rows) {
            result.append(row.product()).append(',')
                .append(row.units()).append(',')
                .append(String.format(Locale.ROOT, "%.2f", row.revenue())).append('\n');
        }
        return result.toString();
    }

    public String writeJson(List<SaleRow> rows) {
        throw new UnsupportedOperationException("CSV writer cannot produce JSON");
    }

    public String writeHtml(List<SaleRow> rows) {
        throw new UnsupportedOperationException("CSV writer cannot produce HTML");
    }
}
