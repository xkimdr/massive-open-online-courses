
import java.util.Scanner;

public class LiquidContainers2 {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        UI ui = new UI(scan);
        ui.start();
        scan.close();
    }

}
