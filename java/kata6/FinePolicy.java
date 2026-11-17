public class FinePolicy {
    public double baseFine(int daysLate) {
        if (daysLate <= 0) return 0;
        if (daysLate <= 7) return daysLate * 0.50;
        return 7 * 0.50 + (daysLate - 7) * 1.00;
    }
}
