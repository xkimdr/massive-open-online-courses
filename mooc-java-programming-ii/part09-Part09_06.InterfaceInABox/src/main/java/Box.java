import java.util.ArrayList;

public class Box implements Packable {
    private ArrayList<Packable> box;
    private double capacity;

    public Box(double capacity) {
        this.box = new ArrayList<>();
        this.capacity = capacity;
    }

    public void add(Packable item) {
        if (this.weight() + item.weight() <= this.capacity) {
            this.box.add(item);
        }
    }

    @Override
    public double weight() {
        double weight = 0;
        // calculate the total weight of the items in the box
        for (Packable item : this.box) {
            weight += item.weight();
        }
        return weight;
    }

    @Override
    public String toString() {
        return "Box: " + this.box.size() + " items, total weight " + this.weight() + " kg";
    }

}
