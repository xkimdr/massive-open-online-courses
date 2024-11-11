public class Literacy implements Comparable<Literacy> {
    private String gender;
    private String country;
    private int year;
    private double percent;

    public Literacy(String gender, String country, int year, double percent) {
        this.gender = gender;
        this.country = country;
        this.year = year;
        this.percent = percent;
    }

    public double getPercent() {
        return this.percent;
    }

    @Override
    public String toString() {
        return this.country + " (" + this.year + "), " + this.gender + ", " + this.percent;
    }

    @Override
    public int compareTo(Literacy literacy) {
        double val = this.percent - literacy.getPercent();

        if (val < 0) {
            return -1;
        } else if (val == 0) {
            return 0;
        } else {
            return 1;
        }
    }
}
