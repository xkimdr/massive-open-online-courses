
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Scanner;

public class SportStatistics {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("File:");
        String file = scan.nextLine();

        System.out.println("Team:");
        String team = scan.nextLine();

        scan.close();

        ArrayList<Statistics> stat = new ArrayList<>();

        try (Scanner scanner = new Scanner(Paths.get(file))) {
            while (scanner.hasNextLine()) {
                String[] data = scanner.nextLine().split(",");
                stat.add(new Statistics(data[0], data[1], Integer.valueOf(data[2]), Integer.valueOf(data[3])));
            }

            int games = 0;
            int win = 0;
            int loss = 0;

            for (Statistics s : stat) {
                if (s.getHomeTeamName().equals(team)) {
                    ++games;

                    if (s.getHomeTeamPoints() > s.getVisitingTeamPoints()) {
                        ++win;
                    } else if (s.getHomeTeamPoints() < s.getVisitingTeamPoints()) {
                        ++loss;
                    }
                } else if (s.getVisitingTeamName().equals(team)) {
                    ++games;

                    if (s.getHomeTeamPoints() < s.getVisitingTeamPoints()) {
                        ++win;
                    } else if (s.getHomeTeamPoints() > s.getVisitingTeamPoints()) {
                        ++loss;
                    }
                }
            }

            System.out.println("Games: " + games);
            System.out.println("Wins: " + win);
            System.out.println("Losses: " + loss);
        } catch (Exception e) {
        }

    }

}
