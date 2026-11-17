public class Booking {
    private final Film film;
    private final boolean weekend;
    private final boolean student;
    private SeatSelection seats;
    private Double total;

    public Booking(Film film, boolean weekend, boolean student) {
        this.film = film;
        this.weekend = weekend;
        this.student = student;
    }

    public void setSeats(int seats) {
        if (seats < 1) {
            throw new IllegalArgumentException("At least one seat is required");
        }
        this.seats = new SeatSelection(seats);
    }

    public void calculate() {
        if (seats == null) {
            throw new IllegalStateException("Call setSeats() first");
        }
        double price = weekend ? 12 : 9;
        if (student) {
            price = price * 0.80;
        }
        total = Math.round((price * seats.count() + 2) * 100.0) / 100.0;
    }

    public String promotion() {
        return new PromotionText().forBooking(weekend, student);
    }

    public void printTicket() {
        if (total == null) {
            throw new IllegalStateException("Call calculate() first");
        }
        new TicketPrinter().print(new Ticket(film, seats, promotion(), total));
    }
}
