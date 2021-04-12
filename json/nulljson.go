package main

import (
	"encoding/json"
	"fmt"
)

type S struct {
	F []*int `json:"f"`
}

func main() {
	a := 1
	b := 2
	c := 3
	s := S{F: []*int{&a, &b, &c}}
	j, _ := json.Marshal(s)
	fmt.Println(string(j))
	s2 := S{F: []*int{nil, nil, nil}}
	j2, _ := json.Marshal(s2)
	fmt.Println(string(j2))
}
