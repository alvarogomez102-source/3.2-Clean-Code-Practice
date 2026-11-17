import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class DispatchService {
    private Parcel pending;
    private final List<String> audit = new ArrayList<>();
    private final List<Parcel> sent = new ArrayList<>();
    private final List<Double> amounts = new ArrayList<>();
    private final RateCalculator rates = new RateCalculator();
    private final LabelFormatter labels = new LabelFormatter();
    private final CsvDispatchStore store = new CsvDispatchStore();
    private final ConsoleNotifier notifier = new ConsoleNotifier();

    public void prepare(Parcel parcel) {
        if (parcel.reference() == null || parcel.reference().isBlank()) {
            throw new IllegalArgumentException("Reference is required");
        }
        if (parcel.weightKg() <= 0) {
            throw new IllegalArgumentException("Weight must be positive");
        }
        if (parcel.customerEmail() == null || !parcel.customerEmail().contains("@")) {
            throw new IllegalArgumentException("Valid email is required");
        }
        pending = parcel;
    }

    public double quote() {
        if (pending == null) {
            throw new IllegalStateException("Call prepare() before quote()");
        }
        double total = rates.quote(pending);
        audit.add("QUOTED " + pending.reference() + " EUR " + total);
        return total;
    }

    public String label() {
        if (pending == null) {
            throw new IllegalStateException("Call prepare() before label()");
        }
        return labels.format(pending);
    }

    public double dispatch() throws IOException {
        if (pending == null) {
            throw new IllegalStateException("Call prepare() before dispatch()");
        }
        double amount = quote();
        store.save(pending, amount);
        System.out.println("LABEL " + label());
        notifier.send(pending);
        sent.add(pending);
        amounts.add(amount);
        pending = null;
        return amount;
    }

    public void printSummary() {
        double revenue = 0;
        int expressCount = 0;
        int internationalCount = 0;
        for (int i = 0; i < sent.size(); i++) {
            revenue += amounts.get(i);
            if (sent.get(i).express()) expressCount++;
            if (!sent.get(i).destinationCountry().equals("ES")
                && !sent.get(i).destinationCountry().equals("PT")) {
                internationalCount++;
            }
        }
        new DispatchSummary(sent.size(), expressCount, internationalCount, revenue, audit.size()).print();
    }
}
