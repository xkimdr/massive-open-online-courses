public class Person implements Saveable {
    private String name;
    private String address;

    @Override
    public void save() {
        System.out.println("save");
    }

    @Override
    public void delete() {
        System.out.println("delete");
    }

    @Override
    public void load(String address) {
        System.out.println("load " + address);
    }
}
