
import java.util.ArrayList;
import java.util.Scanner;

public class MainProgram {

    public static void main(String[] args) {
        UI ui = new UI(new ArrayList<Book>(), new Scanner(System.in));
        ui.start();
    }

}
