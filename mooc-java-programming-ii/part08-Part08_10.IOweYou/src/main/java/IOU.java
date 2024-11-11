import java.util.HashMap;

public class IOU {
    private HashMap<String, Double> data;

    public IOU() {
        this.data = new HashMap<>();
    }

    public void setSum(String toWhom, double amount) {
        this.data.put(toWhom, amount);
    }

    public double howMuchDoIOweTo(String toWhom) {
        return this.data.getOrDefault(toWhom, (double) 0);
    }
}
