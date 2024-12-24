import java.util.ArrayList;

public class OneItemBox extends Box {
    private boolean isFull;
    private ArrayList<Item> box;

    public OneItemBox() {
        this.isFull = false;
        this.box = new ArrayList<>();
    }

    @Override
    public void add(Item item) {
        if (!this.isFull) {
            this.box.add(item);
            this.isFull = true;
        }
    }

    @Override
    public boolean isInBox(Item item) {
        return this.box.contains(item);
    }
}
