
import java.nio.file.Paths;
import java.util.Scanner;

public class RecordsFromAFile {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Name of the file:");
        String file = scanner.nextLine();

        scanner.close();

        try (Scanner scanner2 = new Scanner(Paths.get(file))) {
            while (scanner2.hasNextLine()) {
                String[] data = scanner2.nextLine().split(",");

                System.out.println(data[0] + ", age: " + data[1] + " years");
            }
        } catch (Exception e) {
        }
    }
}
