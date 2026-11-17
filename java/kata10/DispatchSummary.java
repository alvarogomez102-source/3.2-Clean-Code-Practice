import java.util.Locale;

public record DispatchSummary(
    int dispatches,
    int express,
    int international,
    double revenue,
    int auditEntries
) {
    public void print() {
        System.out.printf(Locale.ROOT,
            "Dispatches: %d | Express: %d | International: %d | Revenue: EUR %.2f%n",
            dispatches, express, international, revenue);
        System.out.println("Audit entries: " + auditEntries);
    }
}
