public class LabelFormatter {
    public String format(Parcel parcel) {
        String region;
        if (parcel.destinationCountry().equals("ES")) {
            region = "DOMESTIC";
        } else if (parcel.destinationCountry().equals("PT")) {
            region = "NEIGHBOUR";
        } else {
            region = "INTERNATIONAL";
        }
        return parcel.reference() + " | " + region + " | "
            + (parcel.express() ? "EXPRESS" : "STANDARD");
    }
}
