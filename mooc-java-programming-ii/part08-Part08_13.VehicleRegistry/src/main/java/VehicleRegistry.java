import java.util.ArrayList;
import java.util.HashMap;

public class VehicleRegistry {
    private HashMap<LicensePlate, String> vehicles;

    public VehicleRegistry() {
        this.vehicles = new HashMap<>();
    }

    public boolean add(LicensePlate licensePlate, String owner) {
        if (this.vehicles.containsKey(licensePlate)) {
            if (this.vehicles.get(licensePlate).equals("")) {
                this.vehicles.put(licensePlate, owner);
                return true;
            }
            return false;
        }
        this.vehicles.put(licensePlate, owner);
        return true;
    }

    public String get(LicensePlate licensePlate) {
        return this.vehicles.get(licensePlate);
    }

    public boolean remove(LicensePlate licensePlate) {
        if (this.vehicles.remove(licensePlate) == null) {
            return false;
        }
        return true;
    }

    public void printLicensePlates() {
        for (LicensePlate licensePlate : this.vehicles.keySet()) {
            System.out.println(licensePlate);
        }
    }

    public void printOwners() {
        ArrayList<String> names = new ArrayList<>();
        for (LicensePlate licensePlate : this.vehicles.keySet()) {
            String owner = this.vehicles.get(licensePlate);
            if (!names.contains(owner)) {
                names.add(owner);
                System.out.println(owner);
            }
        }
    }
}
