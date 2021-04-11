package main

import "fmt"

func main() {
	minNum := 1
	maxNum := 100
	answr := "n"
	fmt.Println("Guess a number from 1 to 100.")

	for answr != "y" {

		guess := int(minNum + (maxNum-minNum)/2)

		fmt.Println("Your number is - ", guess, "?")
		fmt.Println("(y)es/(g)reater/(l)ess: ")
		fmt.Scanln(&answr)

		switch {
		case answr == "y":
			fmt.Println("Your number is - ", guess, "!")
			break
		case answr == "g":
			minNum = guess
			continue
		case answr == "l":
			maxNum = guess
			continue
		default:
			fmt.Println("Incorrect input. Try again.")
			continue
		}
	}
}
