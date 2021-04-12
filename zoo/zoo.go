package main

import "fmt"

type creatureThings interface {
	voice() string
}

type creature struct {
	species   string
	move_type string
}

type snake struct {
	creature
	tailBody string
}

type bird struct {
	creature
	wings string
}

type volf struct {
	creature
	fourLegs string
}

func (c creature) voice() string {
	return "Primal voice"
}

func (s snake) voice() string {
	return "Shhhh...."
}

func main() {
	var shusha snake
	shusha.species = "snake"
	shusha.move_type = "crawl"
	shusha.tailBody = "green"
	fmt.Println(shusha)
	fmt.Println(shusha.voice())
	// fmt.Println(shusha.creature.voice())
	var akela volf
	fmt.Println(akela)
	fmt.Println(akela.voice())
}
