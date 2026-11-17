import java.io.IOException;
import java.util.List;
import java.util.Locale;

public class ParcelApplication {
    public void run() throws IOException {
        DispatchService service = new DispatchService();
        List<Parcel> parcels = List.of(
            new Parcel("PK-101", "ada@example.org", "ES", 1.5, false, false),
            new Parcel("PK-102", "grace@example.org", "FR", 3.0, true, true),
            new Parcel("PK-103", "margaret@example.org", "PT", 2.2, false, true)
        );
        for (Parcel parcel : parcels) {
            service.prepare(parcel);
            System.out.printf(Locale.ROOT, "Quote %s: EUR %.2f%n", parcel.reference(), service.quote());
            service.dispatch();
        }
        service.printSummary();
    }
}
