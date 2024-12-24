import java.util.ArrayList;

public class ChangeHistory {
    private ArrayList<Double> history;

    public ChangeHistory() {
        this.history = new ArrayList<>();
    }

    public void add(double status) {
        this.history.add(status);
    }

    public void clear() {
        this.history.clear();
    }

    @Override
    public String toString() {
        return this.history.toString();
    }

    public double maxValue() {
        if (this.history.isEmpty()) {
            return 0;
        }

        double maxValue = this.history.get(0);

        for (Double val : this.history) {
            if (val > maxValue) {
                maxValue = val;
            }
        }

        return maxValue;
    }

    public double minValue() {
        if (this.history.isEmpty()) {
            return 0;
        }

        double minValue = this.history.get(0);

        for (Double val : this.history) {
            if (val < minValue) {
                minValue = val;
            }
        }

        return minValue;
    }

    public double average() {
        if (this.history.isEmpty()) {
            return 0;
        }

        double sum = 0;

        for (Double val : this.history) {
            sum += val;
        }

        return sum / this.history.size();
    }
}
