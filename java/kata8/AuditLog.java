import java.util.ArrayList;
import java.util.List;

public class AuditLog {
    private final List<String> entries = new ArrayList<>();

    public void add(String entry) {
        entries.add(entry);
    }

    public void print() {
        for (String entry : entries) System.out.println("AUDIT " + entry);
    }
}
