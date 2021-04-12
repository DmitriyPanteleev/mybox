package main

import "fmt"

func swap(x *int, y *int) {
	t := *y
	*y = *x
	*x = t
}

func main() {
	x := 1
	y := 2
	fmt.Println(x, y)
	swap(&x, &y)
	fmt.Println(x, y)
}
