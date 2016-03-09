package main

import "errors"

var prefix = "Coucou"

func main() {
	helloPhrase, err := coucou("Gophers")
	if err != nil {
		panic(err)
	}
	println(helloPhrase)
}

func coucou(nom string) (string, error) {
	if len(nom) > 100 {
		return "", errors.New("Nom trop long")
	}
	return prefix + ", " + nom + " !! ", nil
}
