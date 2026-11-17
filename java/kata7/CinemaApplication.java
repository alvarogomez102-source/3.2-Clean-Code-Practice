public class CinemaApplication {
    public void run() {
        Booking booking = new Booking(new Film("The Imitation Game"), true, true);
        booking.setSeats(3);
        booking.calculate();
        booking.printTicket();
    }
}
