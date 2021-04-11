package main

import "fmt"

func fib(n uint) uint64 {
	if n < 2 {
		return uint64(n)
	}
	return fib(n-1) + fib(n-2)
}

func main() {
	var (
		num uint
	)
	fmt.Println("Enter fibonachi number: ")
	fmt.Scanln(&num)
	fmt.Println("Your fibonachi nuber is: ", fib(num))
}
