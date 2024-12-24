public class Container {
    private int amount;

    public Container() {
        this.amount = 0;
    }

    public void add(int num) {
        if (num < 0) {
            return;
        }

        if (this.amount + num > 100) {
            this.amount = 100;
            return;
        }

        this.amount += num;
    }

    public void remove(int num) {
        if (num < 0) {
            return;
        }

        if (this.amount - num < 0) {
            this.amount = 0;
            return;
        }

        this.amount -= num;
    }

    public int contains() {
        return this.amount;
    }

    @Override
    public String toString() {
        return this.amount + "/100";
    }

}
