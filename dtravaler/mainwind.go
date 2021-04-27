package main

import (
	"fmt"
	"log"

	ui "github.com/gizak/termui/v3"
	"github.com/gizak/termui/v3/widgets"
)

func main() {
	if err := ui.Init(); err != nil {
		log.Fatalf("failed to initialize termui: %v", err)
	}
	defer ui.Close()

	x := 0
	y := 0

	p := widgets.NewParagraph()
	p.Title = "OrdinaryCave"
	p.SetRect(0, 0, 25, 5)

	ui.Render(p)

	uiEvents := ui.PollEvents()
	for {
		e := <-uiEvents
		switch e.ID {
		case "q", "<C-c>":
			return
		case "<Down>":
			y = y + 1
		case "<Up>":
			y = y - 1
		case "<Left>":
			x = x + 1
		case "<Right>":
			x = x - 1
		}

		p.Text = fmt.Sprintf("x = %d, y = %d", x, y)
		ui.Render(p)
	}
}
