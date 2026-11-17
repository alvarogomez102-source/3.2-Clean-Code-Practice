public class NotificationApplication {
    public void run() {
        NotificationService service = new NotificationService();
        service.send("email", "ada@example.org", "Your account is ready", false);
        service.send("sms", "+34000000000", "Your parcel will arrive today", true);
        service.printAudit();
    }
}
