package main

import (
	"fmt"
	"log"

	"github.com/nsf/termbox-go"
)

func drawRoundedBox(x, y, w, h int, title string) {
	// Верхняя часть рамки
	termbox.SetCell(x, y, '/', termbox.ColorDefault, termbox.ColorDefault)
	for i := 1; i < w-1; i++ {
		termbox.SetCell(x+i, y, '-', termbox.ColorDefault, termbox.ColorDefault)
	}
	termbox.SetCell(x+w-1, y, '\\', termbox.ColorDefault, termbox.ColorDefault)

	// Нижняя часть рамки
	termbox.SetCell(x, y+h-1, '\\', termbox.ColorDefault, termbox.ColorDefault)
	for i := 1; i < w-1; i++ {
		termbox.SetCell(x+i, y+h-1, '-', termbox.ColorDefault, termbox.ColorDefault)
	}
	termbox.SetCell(x+w-1, y+h-1, '/', termbox.ColorDefault, termbox.ColorDefault)

	// Левая и правая части рамки
	for i := 1; i < h-1; i++ {
		termbox.SetCell(x, y+i, '|', termbox.ColorDefault, termbox.ColorDefault)
		termbox.SetCell(x+w-1, y+i, '|', termbox.ColorDefault, termbox.ColorDefault)
	}

	// Заголовок
	for i, ch := range title {
		termbox.SetCell(x+2+i, y, ch, termbox.ColorDefault, termbox.ColorDefault)
	}
}

func drawText(x, y int, text string) {
	for i, ch := range text {
		termbox.SetCell(x+i, y, ch, termbox.ColorDefault, termbox.ColorDefault)
	}
}

func main() {
	err := termbox.Init()
	if err != nil {
		log.Fatal(err)
	}
	defer termbox.Close()

	// Рисуем первую рамку
	drawRoundedBox(1, 1, 40, 10, "Map")
	drawText(20, 5, "*")
	drawText(19, 4, "|")
	drawText(19, 6, "|")
	drawText(18, 5, "-")
	drawText(20, 5, "*")
	drawText(21, 5, "-")
	drawText(20, 3, "*")
	drawText(20, 7, "*")

	// Рисуем вторую рамку
	drawRoundedBox(1, 12, 20, 5, "Inv")
	drawText(3, 14, "Str: 5")
	drawText(3, 15, "Int: 7")

	termbox.Flush()

	fmt.Println("\n Press any key to exit...")
	termbox.PollEvent()
}
