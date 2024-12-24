public class Item {
    private String product;
    private int qunatity;
    private int unitPrice;

    public Item(String product, int qty, int unitPrice) {
        this.product = product;
        this.qunatity = qty;
        this.unitPrice = unitPrice;
    }

    public int price() {
        return this.unitPrice * this.qunatity;
    }

    public void increaseQuantity() {
        ++this.qunatity;
    }

    @Override
    public String toString() {
        return this.product + ": " + this.qunatity;
    }
}
