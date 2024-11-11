public class Archive {
    private String identifier;
    private String name;

    public Archive(String identifier, String name) {
        this.identifier = identifier;
        this.name = name;
    }

    @Override
    public boolean equals(Object compared) {
        if (this == compared) {
            return true;
        }

        if (!(compared instanceof Archive)) {
            return false;
        }

        Archive a = (Archive) compared;

        return this.identifier.equals(a.identifier);
    }

    @Override
    public String toString() {
        return this.identifier + ": " + this.name;
    }
}
