package main

import (
	"fmt"
)

var i, n, k int
var a []int
var b []int

func main() {
	// Set parameters
	fmt.Print("Enter number of persons: ")
	fmt.Scan(&n)
	fmt.Print("Enter scale number: ")
	fmt.Scan(&k)

	// Create array of persons
	a = make([]int, n)
	for i := 0; i < n; i++ {
		a[i] = i + 1
	}
	fmt.Println("Persons in circle: ", a)

	// Find calculated person
	i = 0
	for len(a) > 1 {
		i = (i + k - 1) % len(a)
		elem := a[i]
		a = append(a[:i], a[i+1:]...)
		b = append(b, elem)
	}
	b = append(b, a[0])
	fmt.Println("Persons in order: ", b)

}
