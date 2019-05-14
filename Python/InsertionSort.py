def InertionSort(A):
    # Inserta A[j] dentro de la secuencia ordenada A[1..j -1]
    for index in range(2, len(A)):
        key = A[index]
        i = index - 1
        while i > -1 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key

elements = [5, 2, 4, 6, 1, 3]
InertionSort(elements)
print(elements)