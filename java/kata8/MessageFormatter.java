public class MessageFormatter {
    public String format(Notification notification) {
        String text = notification.urgent()
            ? "URGENT: " + notification.message()
            : notification.message();
        if (text.length() > 120) return text.substring(0, 120);
        return text;
    }
}
