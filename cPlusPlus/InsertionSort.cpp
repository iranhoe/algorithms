#include <iostream>
using namespace std;

int main()
{
    int A[] = {5, 2, 4, 6, 1, 3};

    // Inserta A[j] dentro de la secuencia ordenada A[1..j -1]
    for(int j = 2; j < sizeof(A); j++)
    {
        int key = A[j];
        int i = j - 1;
        while(i > -1 && A[i] > key)
        {
            A[i + 1] = A[i];
            i = i - 1;
        }

        A[i + 1] = key;
    }

    for(int i = 0; i < sizeof(A); i++)
    {
         cout << A[i] <<endl;
    }
    
    return 0;
}