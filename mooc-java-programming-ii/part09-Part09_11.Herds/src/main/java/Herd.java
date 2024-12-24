import java.util.ArrayList;
import java.util.List;

public class Herd implements Movable {
    private List<Movable> herd;

    public Herd() {
        this.herd = new ArrayList<>();
    }

    public void addToHerd(Movable movable) {
        this.herd.add(movable);
    }

    @Override
    public String toString() {
        if (this.herd.isEmpty()) {
            return "";
        }

        String s = "";

        for (Movable movable : this.herd) {
            s += movable.toString() + "\n";
        }

        return s.substring(0, s.length() - 1);
    }

    @Override
    public void move(int dx, int dy) {
        for (Movable movable : this.herd) {
            movable.move(dx, dy);
        }
    }

}
