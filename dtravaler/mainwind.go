package main

import (
	"log"

	ui "github.com/gizak/termui/v3"
	"github.com/gizak/termui/v3/widgets"
)

func drawCave(m [][]int) string {
	s := ""
	for _, row := range m {
		for _, val := range row {
			switch {
			case val == 0:
				s = s + " "
			case val == 1:
				s = s + "X"
			}
		}
	}
	return s
}

func main() {
	if err := ui.Init(); err != nil {
		log.Fatalf("failed to initialize termui: %v", err)
	}
	defer ui.Close()

	x := 10
	y := 10
	cavemap := make([][]int, 25)
	for i := range cavemap {
		cavemap[i] = make([]int, 25)
	}

	p := widgets.NewParagraph()
	p.Title = "OrdinaryCave"
	p.SetRect(0, 0, 27, 27)

	ui.Render(p)

	uiEvents := ui.PollEvents()
	for {
		cavemap[x][y] = 0

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

		cavemap[x][y] = 1

		p.Text = drawCave(cavemap)
		ui.Render(p)
	}
}
