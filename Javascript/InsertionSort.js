'use strict'

let insertionSort = A =>
{
    // Inserta A[j] dentro de la secuencia ordenada A[1..j -1]
    for (let j = 1; j < A.length; j++) {
        const key = A[j];
        let i = j - 1;
        while (i > -1 && A[i] > key) {
            A[i + 1] = A[i]
            i = i - 1
        }

        A[i + 1] = key
    }
}

let elements = [5, 2, 4, 6, 1, 3];
insertionSort(elements);
console.log(elements);