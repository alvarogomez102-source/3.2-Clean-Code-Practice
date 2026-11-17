public class FineCalculator {
    private final FinePolicy policy = new FinePolicy();
    private final FinePrinter printer = new FinePrinter();

    public double calc(Loan l) {
        double x = policy.baseFine(l.daysLate());
        if (l.member()) x = x * 0.80;
        if (x > 20) x = 20;
        printer.print(new FineReceipt(l.title(), x));
        return x;
    }
}
