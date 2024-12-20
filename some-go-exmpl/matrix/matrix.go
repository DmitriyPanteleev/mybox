package main

import "fmt"

func main() {
	matrix := make([][]int, 10)
	for i := range matrix {
		matrix[i] = make([]int, 10)
	}
	count := 0
	for i := range matrix {
		for j := range matrix[i] {
			if (i+j)%3 == 0 {
				matrix[i][j] = count
			} else {
				matrix[i][j] = 0
			}
			count++
		}
		fmt.Printf("%02d\n", matrix[i])
	}
}
