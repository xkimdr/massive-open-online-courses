
public class Song {

    private String artist;
    private String name;
    private int durationInSeconds;

    public Song(String artist, String name, int durationInSeconds) {
        this.artist = artist;
        this.name = name;
        this.durationInSeconds = durationInSeconds;
    }

    public boolean equals(Object compared) {
        if (this == compared) {
            return true;
        }

        if (!(compared instanceof Song)) {
            return false;
        }

        Song simpleSong = (Song) compared;

        return this.artist.equals(simpleSong.artist) && this.name.equals(simpleSong.name)
                && this.durationInSeconds == simpleSong.durationInSeconds;

    }

    @Override
    public String toString() {
        return this.artist + ": " + this.name + " (" + this.durationInSeconds + " s)";
    }

}
