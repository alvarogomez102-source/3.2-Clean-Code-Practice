import java.util.List;
import java.util.Locale;

public class LibraryFineApplication {
    public void run() {
        LoanLedger ledger = new LoanLedger(List.of(
            new Loan("Clean Code", 3, false),
            new Loan("Tidy First?", 12, true),
            new Loan("Code That Fits in Your Head", 30, false)
        ));
        double total = ledger.totalOutstanding(new FineCalculator());
        System.out.printf(Locale.ROOT, "Total outstanding: EUR %.2f%n", total);
    }
}
