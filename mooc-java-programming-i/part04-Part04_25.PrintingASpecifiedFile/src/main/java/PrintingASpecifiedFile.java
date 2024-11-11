
import java.nio.file.Paths;
import java.util.Scanner;

public class PrintingASpecifiedFile {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Which file should have its contents printed?");
        String fname = scanner.nextLine();

        scanner.close();

        try {
            Scanner scan = new Scanner(Paths.get(fname));

            while (scan.hasNextLine()) {
                System.out.println(scan.nextLine());
            }

            scan.close();
        } catch (Exception e) {
        }

    }
}
