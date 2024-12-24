import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        // implement here the program that allows the user to enter
        // book information and to examine them

        ArrayList<Books> books = new ArrayList<>();

        Scanner scan = new Scanner(System.in);

        while (true) {
            System.out.print("Title: ");
            String title = scan.nextLine();

            if (title.isEmpty()) {
                break;
            }

            System.out.print("Pages: ");
            int pages = Integer.valueOf(scan.nextLine());

            System.out.print("Publication year: ");
            int year = Integer.valueOf(scan.nextLine());

            books.add(new Books(title, pages, year));
        }

        System.out.print("What information will be printed? ");
        String level = scan.nextLine();

        scan.close();

        for (Books book : books) {
            if (level.equals("everything")) {
                System.out.println(book.toString());
            } else if (level.equals("name")) {
                System.out.println(book.getTitle());
            }
        }
    }
}
