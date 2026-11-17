public class ConsoleNotifier {
    public void send(Parcel parcel) {
        System.out.println("EMAIL to " + parcel.customerEmail()
            + ": parcel " + parcel.reference() + " dispatched");
    }
}
