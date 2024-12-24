package application;

public class StandardSensor implements Sensor {
    private final boolean state;
    private int value;

    public StandardSensor(int value) {
        this.value = value;
        this.state = true;
    }

    @Override
    public boolean isOn() {
        return this.state;
    }

    @Override
    public void setOn() {

    }

    @Override
    public void setOff() {

    }

    @Override
    public int read() throws IllegalStateException {
        if (this.state) {
            return this.value;
        } else {
            throw new IllegalStateException();
        }
    }
}
