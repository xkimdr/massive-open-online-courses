
import java.io.IOException;
import java.nio.file.Paths;
import java.util.Scanner;

public class IsItInTheFile {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Name of the file:");
        String file = scanner.nextLine();

        System.out.println("Search for:");
        String searchedFor = scanner.nextLine();

        scanner.close();

        try {
            Scanner scan = new Scanner(Paths.get(file));

            while (scan.hasNextLine()) {
                String line = scan.nextLine();

                if (line.contains(searchedFor)) {
                    System.out.println("Found!");
                    return;
                }
            }

            scan.close();

            System.out.println("Not found.");
        } catch (IOException e) {
            System.out.println("Reading the file " + file + " failed.");
        }

    }
}
