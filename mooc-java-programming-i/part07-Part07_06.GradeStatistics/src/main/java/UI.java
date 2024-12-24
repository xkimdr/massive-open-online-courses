import java.util.Scanner;

public class UI {
    private Points points;
    private Scanner scanner;

    public UI(Scanner scanner) {
        this.points = new Points();
        this.scanner = scanner;
    }

    public void start() {
        System.out.println("Enter point totals, -1 stops:");

        while (true) {
            String input = scanner.nextLine();

            if (input.equals("-1")) {
                break;
            }

            points.add(Integer.valueOf(input));
        }

        this.points.printAverage();
        this.points.printPassingAverage();
        this.points.printPassingPercentage();
        this.points.printGradeDistribution();
    }
}
