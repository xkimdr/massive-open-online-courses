public class Timer {
    private ClockHand second;
    private ClockHand centiSecond;

    public Timer() {
        this.second = new ClockHand(60);
        this.centiSecond = new ClockHand(100);
    }

    public void advance() {
        centiSecond.advance();

        if (centiSecond.value() == 0) {
            second.advance();
        }
    }

    @Override
    public String toString() {
        return second.toString() + ":" + centiSecond.toString();
    }

}
