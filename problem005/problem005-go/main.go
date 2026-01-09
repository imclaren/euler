/*
<p>2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.</p>
<p>
	What is the smallest positive number that is
	<strong class="tooltip">
		evenly divisible
		<span class="tooltiptext">divisible with no remainder</span>
	</strong>
		by all of the numbers from 1 to 20?
</p>
*/

package main

import (
	"fmt"
	"math"
)

func main() {
	result := 20
	done := false
	for !done {
		done = true
		result += 20
		for a := 1; a <= 20; a++ {
			v := float64(result) / float64(a)
			if math.Mod(v, 1) != 0 {
				done = false
				break
			}
		}
	}
	fmt.Println(result)
}
