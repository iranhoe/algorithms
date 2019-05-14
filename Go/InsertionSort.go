package main

import "fmt"

func main() {
	var A = [6]int{5, 2, 4, 6, 1, 3}
	// Inserta A[j] dentro de la secuencia ordenada A[1..j -1]
	for j := 2; j < len(A); j++ {
		var key int = A[j]
		var i int = j - 1
		for i > -1 && A[i] > key {
			A[i+1] = A[i]
			i = i - 1
		}

		A[i+1] = key
	}

	for j := 0; j < len(A); j++ {
		fmt.Println(A[j])
	}
}
