import java.util.ArrayList;

public class TodoList {
    private ArrayList<String> tasks;

    public TodoList() {
        this.tasks = new ArrayList<>();
    }

    public void add(String task) {
        this.tasks.add(task);
    }

    public void print() {
        int count = 0;
        for (String task : this.tasks) {
            ++count;
            System.out.println(count + ": " + task);
        }
    }

    public void remove(int number) {
        this.tasks.remove(number - 1);
    }
}
