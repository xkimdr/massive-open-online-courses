
import java.util.ArrayList;

public class SimpleCollection {

    private String name;
    private ArrayList<String> elements;

    public SimpleCollection(String name) {
        this.name = name;
        this.elements = new ArrayList<>();
    }

    public void add(String element) {
        this.elements.add(element);
    }

    public ArrayList<String> getElements() {
        return this.elements;
    }

    @Override
    public String toString() {
        if (this.elements.isEmpty()) {
            return "The collection " + this.name + " is empty.";
        }

        String returnString = "The collection " + this.name + " has " + this.elements.size() + " element";

        if (this.elements.size() != 1) {
            returnString += "s";
        }

        returnString += ":\n";

        for (String element : elements) {
            returnString += element + "\n";
        }

        return returnString.substring(0, returnString.length() - 1);
    }

}
