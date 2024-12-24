
public class MagicSquareFactory {
    public MagicSquareFactory() {

    }

    public MagicSquare createMagicSquare(int size) {

        MagicSquare square = new MagicSquare(size);

        // implement the creation of a magic square with the Siamese method algorithm
        // here
        int x = size / 2;
        int y = 0;
        int val = 1;

        square.placeValue(x, y, val);
        for (int i = 1; i < size * size; i++) {
            ++val;

            int oldx = x;
            int oldy = y;

            if (y - 1 == -1) {
                y = size - 1;
            } else {
                --y;
            }

            if (x + 1 == size) {
                x = 0;
            } else {
                ++x;
            }

            if (square.readValue(x, y) != 0) {
                x = oldx;
                y = oldy + 1;
            }
            square.placeValue(x, y, val);

        }

        return square;
    }

}
