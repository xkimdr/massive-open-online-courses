public class Hideout<T> {
    private T container;

    public Hideout() {
        this.container = null;
    }

    public void putIntoHideout(T toHide) {
        this.container = toHide;
    }

    public T takeFromHideout() {
        T temp = this.container;
        this.container = null;
        return temp;
    }

    public boolean isInHideout() {
        if (this.container != null) {
            return true;
        }

        return false;
    }
}
