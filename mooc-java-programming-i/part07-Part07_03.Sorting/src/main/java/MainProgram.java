
public class MainProgram {

    public static void main(String[] args) {
        // write your test code here
        int[] array = { 3, 1, 5, 99, 3, 12 };
    }

    public static int smallest(int[] array) {
        // write your code here
        return array[indexOfSmallest(array)];
    }

    public static int indexOfSmallest(int[] array) {
        return indexOfSmallestFrom(array, 0);
    }

    public static int indexOfSmallestFrom(int[] table, int startIndex) {
        // write your code here

        int index = startIndex;

        for (int i = startIndex; i < table.length; ++i) {
            if (table[index] > table[i]) {
                index = i;
            }
        }

        return index;
    }

    public static void swap(int[] array, int index1, int index2) {
        // write your code here
        int temp = array[index1];
        array[index1] = array[index2];
        array[index2] = temp;
    }

    public static void sort(int[] array) {
        for (int i = 0; i < array.length; ++i) {
            int index = indexOfSmallestFrom(array, i);
            swap(array, i, index);
            System.out.println(array);
        }
    }

}
