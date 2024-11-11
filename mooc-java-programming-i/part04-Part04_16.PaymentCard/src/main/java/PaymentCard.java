public class PaymentCard {
    private double balance;

    public PaymentCard(double openingBalance) {
        // write code here
        this.balance = openingBalance;
    }

    public String toString() {
        // write code here
        return "The card has a balance of " + this.balance + " euros";
    }

    public void eatAffordably() {
        // write code here
        double newBalance = this.balance - 2.60;
        if (newBalance >= 0) {
            this.balance = newBalance;
        }
    }

    public void eatHeartily() {
        // write code here
        double newBalance = this.balance - 4.60;
        if (newBalance >= 0) {
            this.balance = newBalance;
        }
    }

    public void addMoney(double amount) {
        // write code here
        if (amount < 0) {
            return;
        }

        double newBalance = this.balance + amount;
        if (newBalance <= 150) {
            this.balance = newBalance;
        } else {
            this.balance = 150;
        }
    }

}
