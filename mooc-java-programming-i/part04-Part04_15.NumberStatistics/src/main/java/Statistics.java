
public class Statistics {
    private int count;
    private int sum;

    public Statistics() {
        // initialize the variable numberCount here
        this.count = 0;
    }

    public void addNumber(int number) {
        // write code here
        this.sum += number;
        ++this.count;
    }

    public int getCount() {
        // write code here
        return this.count;
    }

    public int sum() {
        // write code here
        return this.sum;

    }

    public double average() {
        // write code here
        if (this.sum != 0 && this.count != 0) {
            return (double) this.sum / this.count;
        } else {
            return 0;
        }
    }
}
