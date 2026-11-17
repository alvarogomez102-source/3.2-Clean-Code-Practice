import java.util.Locale;

public class TicketPrinter {
    public void print(Ticket ticket) {
        System.out.println("Film: " + ticket.film().title());
        System.out.println("Seats: " + ticket.seats().count());
        System.out.println(ticket.promotion());
        System.out.printf(Locale.ROOT, "Total: EUR %.2f%n", ticket.total());
    }
}
