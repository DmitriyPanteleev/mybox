package main

import (
	"fmt"
)

func main() {
	var number uint64

	fmt.Println("Enter a number to factorize:")
	fmt.Scanln(&number)

	fmt.Println("Factors of", number, "are:")
	for i := uint64(2); i <= number; i++ {
		for number%i == 0 {
			fmt.Println(i)
			number /= i
		}
	}
}
