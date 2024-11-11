import java.util.ArrayList;

public class Birds {
    private ArrayList<Bird> birds;

    public Birds() {
        this.birds = new ArrayList<>();
    }

    public void add(String name, String latinName) {
        this.birds.add(new Bird(name, latinName));
    }

    public boolean observation(String name) {
        for (Bird bird : this.birds) {
            if (bird.getName().equals(name)) {
                bird.increaseObservations();
                return true;
            }
        }

        return false;
    }

    public void prineOne(String name) {
        for (Bird bird : this.birds) {
            if (bird.getName().equals(name)) {
                System.out.println(bird.toString());
                return;
            }
        }
    }

    public void printAll() {
        for (Bird bird : this.birds) {
            System.out.println(bird.toString());
        }
    }

}
