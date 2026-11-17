import java.util.Locale;

public class FinePrinter {
    public void print(FineReceipt receipt) {
        System.out.printf(Locale.ROOT, "Fine for %s: EUR %.2f%n",
            receipt.title(), receipt.amount());
    }
}
