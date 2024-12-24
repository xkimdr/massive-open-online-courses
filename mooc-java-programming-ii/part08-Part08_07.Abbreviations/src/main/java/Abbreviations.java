import java.util.HashMap;

public class Abbreviations {
    private HashMap<String, String> abbreviations;

    public Abbreviations() {
        this.abbreviations = new HashMap<>();
    }

    public void addAbbreviation(String abbreviation, String explanation) {
        String s = Abbreviations.sanitizedString(abbreviation);

        if (this.abbreviations.containsKey(s)) {
            System.out.println("abbreviation is already in the list!");
        } else {
            this.abbreviations.put(s, explanation);
        }
    }

    public boolean hasAbbreviation(String abbreviation) {
        String s = Abbreviations.sanitizedString(abbreviation);
        return this.abbreviations.containsKey(s);
    }

    private static String sanitizedString(String str) {
        if (str == null) {
            return "";
        }

        return str.toLowerCase().trim();
    }

    public String findExplanationFor(String abbreviation) {
        String s = Abbreviations.sanitizedString(abbreviation);
        return this.abbreviations.get(s);
    }
}
