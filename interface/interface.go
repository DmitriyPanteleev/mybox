package main

import (
	"fmt"

	"github.com/charmbracelet/lipgloss"
)

func main() {
	// Определяем стили для рамок и текста
	borderStyle := lipgloss.NewStyle().
		Border(lipgloss.NormalBorder()).
		BorderForeground(lipgloss.Color("63")).
		Padding(1, 2).
		Width(20)

	titleStyle := lipgloss.NewStyle().
		Bold(true).
		Foreground(lipgloss.Color("205"))

	textStyle := lipgloss.NewStyle().
		Foreground(lipgloss.Color("240"))

	// Создаем текст с заголовком "Map"
	mapHeader := titleStyle.Render("Map")
	mapContent := textStyle.Render("\n  *\n * *\n  *")
	mapBox := borderStyle.Render(mapContent)
	mapWithHeader := lipgloss.PlaceHorizontal(len(mapBox), lipgloss.Left, mapHeader) + "\n" + mapBox

	// Создаем текст с заголовком "Inv"
	invHeader := titleStyle.Render("Inv")
	invContent := textStyle.Render("Str: 5\nInt: 7")
	invBox := borderStyle.Render(invContent)
	invWithHeader := lipgloss.PlaceHorizontal(len(invBox), lipgloss.Right, invHeader) + "\n" + invBox

	// Выводим рамки в консоль
	fmt.Println(mapWithHeader)
	fmt.Println(invWithHeader)
}
