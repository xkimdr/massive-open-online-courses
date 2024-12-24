package application;

import java.util.Random;

public class TemperatureSensor implements Sensor {
    private boolean state;

    public TemperatureSensor() {
        this.state = false;
    }

    @Override
    public boolean isOn() {
        return this.state;
    }

    @Override
    public void setOn() {
        this.state = true;
    }

    @Override
    public void setOff() {
        this.state = false;
    }

    @Override
    public int read() throws IllegalStateException {
        if (this.state) {
            return new Random().nextInt(61) - 30;
        } else {
            throw new IllegalStateException();
        }
    }
}
