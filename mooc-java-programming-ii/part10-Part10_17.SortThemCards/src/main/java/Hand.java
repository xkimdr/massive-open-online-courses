import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Hand implements Comparable<Hand> {
    private List<Card> cards;

    public Hand() {
        this.cards = new ArrayList<>();
    }

    public void add(Card card) {
        this.cards.add(card);
    }

    public void print() {
        this.cards.stream().forEach(x -> System.out.println(x));
    }

    public void sort() {
        Collections.sort(this.cards);
    }

    public int totalValue() {
        return this.cards.stream().mapToInt(card -> card.getValue()).sum();
    }

    @Override
    public int compareTo(Hand hand) {
        return this.totalValue() - hand.totalValue();
    }

    public void sortBySuit() {
        Collections.sort(this.cards, new BySuitInValueOrder());
    }
}
