package application;

import java.util.ArrayList;
import java.util.List;

public class AverageSensor implements Sensor {
    private List<Sensor> sensors;
    private List<Integer> values;

    public AverageSensor() {
        this.sensors = new ArrayList<>();
        this.values = new ArrayList<>();
    }

    public void addSensor(Sensor toAdd) {
        this.sensors.add(toAdd);
    }

    public List<Integer> readings() {
        return this.values;
    }

    @Override
    public boolean isOn() {
        for (Sensor sensor : this.sensors) {
            if (!sensor.isOn()) {
                return false;
            }
        }
        return true;
    }

    @Override
    public void setOn() {
        this.sensors.stream().forEach(Sensor::setOn);
    }

    @Override
    public void setOff() {
        this.sensors.stream().forEach(Sensor::setOff);
    }

    @Override
    public int read() throws IllegalStateException {
        int sum = 0;
        int count = 0;
        for (Sensor sensor : this.sensors) {
            sum += sensor.read();
            ++count;
        }
        int avg = sum / count;
        this.values.add(avg);
        return avg;
    }
}
