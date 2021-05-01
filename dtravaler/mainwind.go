package main

import (
	"log"

	ui "github.com/gizak/termui/v3"
	"github.com/gizak/termui/v3/widgets"
)

func caveGenerator() [][]int {
	cavemap := make([][]int, 25)
	for i := range cavemap {
		cavemap[i] = make([]int, 50)
	}
	return cavemap
}

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

	y := 10
	x := 10
	cavemap := caveGenerator()

	p := widgets.NewParagraph()
	p.Title = "OrdinaryCave"
	p.SetRect(0, 0, 52, 27)

	ui.Render(p)

	uiEvents := ui.PollEvents()
	for {
		cavemap[y][x] = 0

		e := <-uiEvents
		switch e.ID {
		case "q", "<C-c>":
			return
		case "<Down>":
			y = y + 1
			if y > 24 {
				y = 24
			}
		case "<Up>":
			y = y - 1
			if y < 0 {
				y = 0
			}
		case "<Left>":
			x = x - 1
			if x < 0 {
				x = 0
			}
		case "<Right>":
			x = x + 1
			if x > 49 {
				x = 49
			}
		}

		cavemap[y][x] = 1

		p.Text = drawCave(cavemap)
		ui.Render(p)
	}
}
