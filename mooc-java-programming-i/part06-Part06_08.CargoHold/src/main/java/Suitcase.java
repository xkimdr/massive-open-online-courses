import java.util.ArrayList;

public class Suitcase {
    private ArrayList<Item> items;
    private int maxWeight;
    private int weight;

    public Suitcase(int maxWeight) {
        this.items = new ArrayList<>();
        this.maxWeight = maxWeight;
        this.weight = 0;
    }

    public void addItem(Item item) {

        if (this.weight + item.getWeight() <= this.maxWeight) {
            this.items.add(item);
            this.weight += item.getWeight();
        }
    }

    public void printItems() {
        for (Item item : this.items) {
            System.out.println(item.toString());
        }
    }

    public int totalWeight() {
        return this.weight;
    }

    public Item heaviestItem() {
        if (this.items.isEmpty()) {
            return null;
        }

        Item heaviest = this.items.get(0);

        for (Item item : this.items) {
            if (item.getWeight() > heaviest.getWeight()) {
                heaviest = item;
            }
        }

        return heaviest;
    }

    @Override
    public String toString() {
        if (this.items.isEmpty()) {
            return "no items (0 kg)";
        } else if (this.items.size() == 1) {
            return "1 item (" + this.weight + " kg)";
        }

        return this.items.size() + " items (" + this.weight + " kg)";
    }
}
