
public class Checker {
    public boolean isDayOfWeek(String string) {
        return string.matches("mon|tue|wed|thu|fri|sat|sun");
    }

    public boolean allVowels(String string) {
        return string.matches("(a|e|i|o|u)+");
    }

    public boolean timeOfDay(String string) {
        if (string.matches("24(:[1-9][1-9]){2}")) {
            return false;
        }
        return string.matches("[0-2][0-9](:[0-5][0-9]){2}");
    }
}
