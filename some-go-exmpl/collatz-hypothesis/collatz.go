package main

import (
	"fmt"
)

var n, m, c int

func collatz(n int) int {
	if n%2 == 0 {
		return n / 2
	}
	return 3*n + 1
}

func main() {

	fmt.Print("Enter a number: ")
	fmt.Scan(&n)

	m = 1
	c = 0
	for n != 1 {
		c++
		if m < n {
			m = n
		}
		n = collatz(n)
		fmt.Println(n)
	}

	fmt.Println("The number of steps is: ", c)
	fmt.Println("The maximum number is: ", m)
}
