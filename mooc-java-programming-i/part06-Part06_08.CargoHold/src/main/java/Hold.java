import java.util.ArrayList;

public class Hold {
    private ArrayList<Suitcase> suitcases;
    private int maxWeight;
    private int weight;

    public Hold(int maxWeight) {
        this.suitcases = new ArrayList<>();
        this.maxWeight = maxWeight;
    }

    public void addSuitcase(Suitcase suitcase) {
        if (this.weight + suitcase.totalWeight() <= this.maxWeight) {
            this.suitcases.add(suitcase);
            this.weight += suitcase.totalWeight();
        }
    }

    public void printItems() {
        for (Suitcase suitcase : suitcases) {
            suitcase.printItems();
        }
    }

    @Override
    public String toString() {
        return this.suitcases.size() + " suitcases (" + this.weight + " kg)";
    }

}
