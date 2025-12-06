package main

import (
	"fmt"
	"os"
	"log"
	"strings"
	"strconv"
)

func main() {
	content, err := os.ReadFile("assets/submit.txt")
	if err != nil {
		log.Fatal(err)
	}

	lines := strings.Split(string(content), "\n")
	replacer := strings.NewReplacer("R", "", "L", "-")

	var pos = 50
	var res int

	for _, line := range lines {
		if line == "" {
			continue
		}
		i, err := strconv.Atoi(replacer.Replace(line))
		if err != nil {
			log.Fatal(err)
		}

		pos += i
		pos %= 100

		if pos == 0 {
			res += 1
		}
	}

	fmt.Println(res)
}
