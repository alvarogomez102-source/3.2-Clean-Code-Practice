public class NotificationService {
    private final EmailSender email = new EmailSender();
    private final SmsSender sms = new SmsSender();
    private final AuditLog audit = new AuditLog();
    private final MessageFormatter formatter = new MessageFormatter();

    public void send(String channel, String destination, String message, boolean urgent) {
        Notification notification = new Notification(channel, destination, message, urgent);
        String text = formatter.format(notification);
        if (channel.equals("email")) {
            email.send(destination, text);
        } else if (channel.equals("sms")) {
            sms.send(destination, text);
        } else {
            throw new IllegalArgumentException("Unknown channel: " + channel);
        }
        audit.add(channel + " -> " + destination + ": " + text);
    }

    public void printAudit() {
        audit.print();
    }
}
