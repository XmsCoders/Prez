package main

import "fmt"
// END OMIT
type I interface {
	M()
}

type T struct {
	S string
}
func (t *T) M() {
	fmt.Println(t.S)
}

type F float64
func (f F) M() {
	fmt.Println(f)
}

func main() {
	var i I
	i = &T{"Kikoo"}
	i.M()
	i = F(4.5)
	i.M()
}
