def InertionSort(A):
    for index in range(1, len(A)):
        key = A[index]
        # Insert A[index] into the sorted sequence A[1..index -1]
        i = index - 1
        # i > -1 is in order to stop once the first item is reached
        print(f'Key: {key}')
        while i > -1 and A[i] > key:
            print(f'{A[i]} > {key} - steps')
            A[i + 1] = A[i]
            i = i - 1
            print(f'Array :{A}')
        A[i + 1] = key
        print (f'---------------end while {i}, Array:{A} - {A[i]} > {key}')

elements = [5, 2, 4, 6, 1, 3]
InertionSort(elements)
print(elements)