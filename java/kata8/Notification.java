public record Notification(
    String channel,
    String destination,
    String message,
    boolean urgent
) {}
