
package main

import (
	"fmt"
	"log"
	"os"
)
func main() {
    data := []rune{81027, 81022, 81011, 81342, 81020, 80979, 81131, 81014, 81035, 81014}
	fmt.Print("rune: ", (data), "\n")
	
	output := string(data)
	err := os.WriteFile("output.txt", []byte(output), 0644)
	if err != nil {
		log.Fatal(err)
	}

}
