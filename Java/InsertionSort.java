public class InsertionSort {

    public static void main(String[] args) {
        int[] A = {5, 2, 4, 6, 1, 3};

        // Inserta A[j] dentro de la secuencia ordenada A[1..j -1]
        for (int j = 1; j < A.length; j++) {
            int key = A[j];
            int i = j - 1;

            while(i > -1 && A[i] > key) {
                A[i + 1] = A[i];
                i = i - 1;
            }

            A[i + 1] = key;
        }

        for (int item : A) {
            System.out.println(item);
        }
    }
}