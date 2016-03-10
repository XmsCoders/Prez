package main

import (
	"fmt"
	"time"
)

func main() {
	var hits struct {
      sync.Mutex
      n int
    }

    hits.Lock()
    hits.n++
    hits.Unlock()
}