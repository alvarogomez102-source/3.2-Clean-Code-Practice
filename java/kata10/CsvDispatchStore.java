import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;

public class CsvDispatchStore {
    public void save(Parcel parcel, double amount) throws IOException {
        Path path = Path.of("dispatches.csv");
        if (!Files.exists(path)) {
            Files.writeString(path, "reference,country,weight,express,insured,total\n",
                StandardCharsets.UTF_8, StandardOpenOption.CREATE);
        }
        String line = parcel.reference() + "," + parcel.destinationCountry() + ","
            + parcel.weightKg() + "," + parcel.express() + ","
            + parcel.insured() + "," + amount + "\n";
        Files.writeString(path, line, StandardCharsets.UTF_8, StandardOpenOption.APPEND);
    }
}
