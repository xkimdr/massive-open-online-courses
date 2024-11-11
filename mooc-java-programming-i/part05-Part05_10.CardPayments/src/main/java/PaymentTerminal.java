
public class PaymentTerminal {

    private double money; // amount of cash
    private int affordableMeals; // number of sold affordable meals
    private int heartyMeals; // number of sold hearty meals

    public PaymentTerminal() {
        // register initially has 1000 euros of money
        this.money = 1000;
        this.affordableMeals = 0;
        this.heartyMeals = 0;
    }

    public double eatAffordably(double payment) {
        // an affordable meal costs 2.50 euros
        // increase the amount of cash by the price of an affordable mean and return the
        // change
        // if the payment parameter is not large enough, no meal is sold and the method
        // should return the whole payment
        double cost = 2.5;
        double change = payment - cost;

        if (change >= 0) {
            ++this.affordableMeals;
            this.money += cost;

            return change;
        }

        return payment;
    }

    public boolean eatAffordably(PaymentCard card) {
        // an affordable meal costs 2.50 euros
        // if the payment card has enough money, the balance of the card is decreased by
        // the price, and the method returns true
        // otherwise false is returned
        if (card.takeMoney(2.5)) {
            ++this.affordableMeals;
            return true;
        }

        return false;
    }

    public double eatHeartily(double payment) {
        // a hearty meal costs 4.30 euros
        // increase the amount of cash by the price of a hearty mean and return the
        // change
        // if the payment parameter is not large enough, no meal is sold and the method
        // should return the whole payment
        double cost = 4.30;
        double change = payment - cost;

        if (change >= 0) {
            ++this.heartyMeals;
            this.money += cost;

            return change;
        }

        return payment;
    }

    public boolean eatHeartily(PaymentCard card) {
        // a hearty meal costs 4.30 euros
        // if the payment card has enough money, the balance of the card is decreased by
        // the price, and the method returns true
        // otherwise false is returned

        if (card.takeMoney(4.3)) {
            ++this.heartyMeals;
            return true;
        }

        return false;
    }

    public void addMoneyToCard(PaymentCard card, double sum) {
        // ...
        if (sum < 0) {
            return;
        }

        card.addMoney(sum);
        this.money += sum;

    }

    @Override
    public String toString() {
        return "money: " + money + ", number of sold affordable meals: " + affordableMeals
                + ", number of sold hearty meals: " + heartyMeals;
    }
}
