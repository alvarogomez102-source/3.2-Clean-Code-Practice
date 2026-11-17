public class PromotionText {
    public String forBooking(boolean weekend, boolean student) {
        if (student && weekend) return "Student weekend price applied";
        if (student && !weekend) return "Student weekday price applied";
        return "Standard price applied";
    }
}
