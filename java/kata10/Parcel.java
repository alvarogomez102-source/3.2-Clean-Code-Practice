public record Parcel(
    String reference,
    String customerEmail,
    String destinationCountry,
    double weightKg,
    boolean express,
    boolean insured
) {}
