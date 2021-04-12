package main

import "fmt"

type creature struct {
	species   string
	move_type string
}

func (c creature) voice() string {
	fmt.Println("Primal voice")
	return ""
}

type snake struct {
	creature
	unic_snake_param string
}

func (s snake) voice() string {
	fmt.Println("Shhhh....")
	return ""
}

type volf struct {
	creature
	volfcolor string
}

func main() {
	var shusha snake
	shusha.species = "snake"
	shusha.move_type = "crawl"
	shusha.unic_snake_param = "home pet"
	fmt.Println(shusha.species)
	fmt.Println(shusha.move_type)
	fmt.Println(shusha.creature)
	fmt.Println(shusha.voice())
	// fmt.Println(shusha.creature.voice())
	var akela volf
	akela.volfcolor = "brown"
	fmt.Println(akela.volfcolor)
	fmt.Println(akela.voice())
}
