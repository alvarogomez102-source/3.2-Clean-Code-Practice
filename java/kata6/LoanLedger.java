import java.util.List;

public class LoanLedger {
    private final List<Loan> loans;

    public LoanLedger(List<Loan> loans) {
        this.loans = loans;
    }

    public double totalOutstanding(FineCalculator calculator) {
        double total = 0;
        for (Loan loan : loans) total += calculator.calc(loan);
        return total;
    }
}
