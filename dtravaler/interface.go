package main

import (
	"fmt"
	"os"

	"github.com/charmbracelet/lipgloss"
	"golang.org/x/term"
)

func main() {
	// Get the terminal dimensions
	width, height, err := term.GetSize(int(os.Stdout.Fd()))
	if err != nil {
		fmt.Println("Error getting terminal size:", err)
		return
	}
	fmt.Println("Width:", width, "Height:", height)

	// Define the height as 2/3 of the terminal height
	boxHeight := (2 * (height - 1)) / 3

	// Create a lip gloss style with the desired dimensions and border
	style := lipgloss.NewStyle().
		Width(width - 2).                // Set to full terminal width
		Height(boxHeight).               // Set to 2/3 of terminal height
		Border(lipgloss.RoundedBorder()) // Use rounded corners

	// Draw the box
	box := style.Render("")

	// Print the box to the terminal
	fmt.Println(box)
	fmt.Println("Width:", width, "Height:", boxHeight)
}
