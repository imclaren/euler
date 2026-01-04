/*
A number is a perfect square, or a square number, if it is the square of a positive integer.
For example, 25 is a square number because 5^2 = 5 times 5 = 25 - it is also an odd square.
The first 5 square numbers are: 1, 4, 9, 16, 25, and the sum of the odd squares is 1 + 9 + 25 = 35.
Among the first 513 thousand square numbers, what is the sum of all the odd squares
*/

package main

import (
	"fmt"
	"math"
)

func main() {
	result := float64(0)

	i := 0
	for i < 826000 {
		i += 1

		// Get the square of i
		x := math.Pow(float64(i), 2)

		// Check if odd
		if int64(x)%2 != 0 {

			// Sum of odd squares
			result += x
		}
	}

	fmt.Println(int64(result))
}
