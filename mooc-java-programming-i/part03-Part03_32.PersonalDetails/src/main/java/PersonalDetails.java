import java.util.Scanner;

public class PersonalDetails {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int sum = 0;
        int count = 0;
        int length = 0;
        String lname = "";

        while (true) {
            String text = scanner.nextLine();

            if (text.equals("")) {
                break;
            }

            ++count;

            String[] array = text.split(",");

            sum += Integer.valueOf(array[1]);

            String name = array[0];

            if (name.length() > length) {
                lname = name;
                length = name.length();
            }
        }

        scanner.close();

        System.out.println("Longest name: " + lname);
        System.out.println("Average of the birth years: " + ((double) sum / count));
    }
}
