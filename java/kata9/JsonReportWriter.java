import java.util.List;
import java.util.Locale;

public class JsonReportWriter implements ReportWriter {
    public String writeCsv(List<SaleRow> rows) {
        throw new UnsupportedOperationException("JSON writer cannot produce CSV");
    }

    public String writeJson(List<SaleRow> rows) {
        StringBuilder result = new StringBuilder("[\n");
        for (int i = 0; i < rows.size(); i++) {
            SaleRow row = rows.get(i);
            result.append(String.format(Locale.ROOT,
                "  {\"product\":\"%s\",\"units\":%d,\"revenue\":%.2f}",
                row.product(), row.units(), row.revenue()
            ));
            if (i < rows.size() - 1) result.append(',');
            result.append('\n');
        }
        return result.append(']').toString();
    }

    public String writeHtml(List<SaleRow> rows) {
        throw new UnsupportedOperationException("JSON writer cannot produce HTML");
    }
}
