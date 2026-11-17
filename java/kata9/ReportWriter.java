import java.util.List;

public interface ReportWriter {
    String writeCsv(List<SaleRow> rows);
    String writeJson(List<SaleRow> rows);
    String writeHtml(List<SaleRow> rows);
}
