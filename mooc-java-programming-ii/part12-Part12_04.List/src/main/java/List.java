public class List<T> {
    private T[] values;
    private int freeIndex;

    public List() {
        this.values = (T[]) new Object[10];
        this.freeIndex = 0;
    }

    public void add(T value) {
        if (this.freeIndex == this.values.length) {
            this.grow();
        }
        this.values[freeIndex] = value;
        ++this.freeIndex;
    }

    private void grow() {
        int newSize = this.values.length + this.values.length / 2;
        T[] newValues = (T[]) new Object[newSize];
        for (int i = 0; i < this.values.length; i++) {
            newValues[i] = this.values[i];
        }
        this.values = newValues;
    }

    public boolean contains(T value) {
        return indexOfValue(value) >= 0;
    }

    public int indexOfValue(T value) {
        for (int i = 0; i < this.freeIndex; ++i) {
            if (this.values[i].equals(value)) {
                return i;
            }
        }

        return -1;
    }

    private void moveToLeft(int fromIndex) {
        for (int i = fromIndex; i < this.freeIndex - 1; i++) {
            this.values[i] = this.values[i + 1];
        }
    }

    public void remove(T value) {
        int index = this.indexOfValue(value);
        if (index < 0) {
            return;
        }
        this.moveToLeft(index);
        --this.freeIndex;
    }

    public T value(int index) {
        if (index < 0 || index >= this.freeIndex) {
            throw new ArrayIndexOutOfBoundsException("Index " + index + " outside of [0, " + this.freeIndex + "]");
        }

        return this.values[index];
    }

    public int size() {
        return this.freeIndex;
    }

}
