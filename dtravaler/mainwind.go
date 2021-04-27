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
		s = s + "\n"
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
			x = x + 1
			if x > 24 {
				x = 24
			}
		case "<Up>":
			x = x - 1
			if x < 0 {
				x = 0
			}
		case "<Left>":
			y = y - 1
			if y < 0 {
				y = 0
			}
		case "<Right>":
			y = y + 1
			if y > 24 {
				y = 24
			}
		}

		cavemap[x][y] = 1

		p.Text = drawCave(cavemap)
		ui.Render(p)
	}
}
