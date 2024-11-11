
import java.util.ArrayList;
import java.util.Scanner;

public class IndexOfSmallest {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // implement here a program that reads user input
        // until the user enters 9999

        // after that, the program prints the smallest number
        // and its index -- the smallest number
        // might appear multiple times

        ArrayList<Integer> numbers = new ArrayList<>();

        while (true) {
            int num = Integer.valueOf(scanner.nextLine());

            if (num == 9999) {
                break;
            }

            numbers.add(num);
        }

        scanner.close();

        int min = numbers.get(0);
        int size = numbers.size();

        for (int i = 1; i < size; ++i) {
            min = numbers.get(i) < min ? numbers.get(i) : min;
        }

        System.out.println("Smallest number: " + min);

        for (int i = 0; i < size; ++i) {
            if (numbers.get(i) == min) {
                System.out.println("Found at index: " + i);
            }
        }
    }
}
