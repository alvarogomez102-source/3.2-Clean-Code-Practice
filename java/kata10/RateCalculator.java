public class RateCalculator {
    public double quote(Parcel parcel) {
        double price;
        if (parcel.destinationCountry().equals("ES")) {
            price = 5;
        } else if (parcel.destinationCountry().equals("PT")) {
            price = 9;
        } else {
            price = 18;
        }
        if (parcel.weightKg() > 2) price += (parcel.weightKg() - 2) * 3;
        if (parcel.express()) price += 12;
        if (parcel.insured()) price += 6;
        return Math.round(price * 1.07 * 100.0) / 100.0;
    }
}
