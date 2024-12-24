public class Cube {
    private int edge;

    public Cube(int edgeLength) {
        this.edge = edgeLength;
    }

    public int volume() {
        return this.edge * this.edge * this.edge;
    }

    @Override
    public String toString() {
        return "The length of the edge is " + this.edge + " and the volume " + this.volume();
    }
}
