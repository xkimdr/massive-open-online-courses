import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Scanner;

public class UI {
    private ArrayList<Book> books;
    private Scanner scanner;
    private Comparator<Book> comparator;

    public UI(ArrayList<Book> books, Scanner scanner) {
        this.books = books;
        this.scanner = scanner;
        this.comparator = Comparator.comparing(Book::getAge).thenComparing(Book::getName);
    }

    public void start() {
        while (true) {
            System.out.print("Input the name of the book, empty stops: ");
            String name = scanner.nextLine();

            if (name.isEmpty()) {
                break;
            }

            System.out.print("Input the age recommendation: ");
            int age = Integer.valueOf(scanner.nextLine());

            this.books.add(new Book(name, age));

            System.out.println();
        }

        scanner.close();

        System.out.println();

        System.out.println(this.books.size() + " books in total.");

        System.out.println();

        System.out.println("Books:");
        Collections.sort(this.books, this.comparator);
        this.books.stream().forEach(book -> System.out.println(book));
    }
}
