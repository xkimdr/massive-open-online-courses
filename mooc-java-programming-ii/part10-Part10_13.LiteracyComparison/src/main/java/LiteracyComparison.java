
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;

public class LiteracyComparison {

    public static void main(String[] args) {
        try {
            Files.lines(Paths.get("literacy.csv")).map(line -> line.split(","))
                    .map(array -> new Literacy(array[2].trim().split(" ")[0], array[3].trim(),
                            Integer.valueOf(array[4]), Double.valueOf(array[5])))
                    .sorted().forEach(x -> System.out.println(x));
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
