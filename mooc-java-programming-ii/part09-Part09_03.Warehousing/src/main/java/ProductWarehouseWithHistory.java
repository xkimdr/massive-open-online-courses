public class ProductWarehouseWithHistory extends ProductWarehouse {
    private ChangeHistory record;

    public ProductWarehouseWithHistory(String productName, double capacity, double initialBalance) {
        super(productName, capacity);
        this.record = new ChangeHistory();
        this.addToWarehouse(initialBalance);
    }

    public String history() {
        return this.record.toString();
    }

    @Override
    public void addToWarehouse(double amount) {
        super.addToWarehouse(amount);
        this.record.add(this.getBalance());
    }

    @Override
    public double takeFromWarehouse(double amount) {
        double rv = super.takeFromWarehouse(amount);
        this.record.add(this.getBalance());
        return rv;
    }

    public void printAnalysis() {
        System.out.println("Product: " + this.getName());
        System.out.println("History: " + this.history());
        System.out.println("Largest amount of product: " + this.record.maxValue());
        System.out.println("Smallest amount of product: " + this.record.minValue());
        System.out.println("Average: " + this.record.average());
    }

}
