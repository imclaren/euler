/*
<p>The sum of the squares of the first ten natural numbers is,</p>
$$1^2 + 2^2 + ... + 10^2 = 385.$$
<p>The square of the sum of the first ten natural numbers is,</p>
$$(1 + 2 + ... + 10)^2 = 55^2 = 3025.$$
<p>Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.</p>
<p>Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.</p>
*/

package main

import (
	"fmt"
	"iter"
	"math"
)

type Item int64

func Items() iter.Seq[Item] {
	return func(yield func(Item) bool) {
		count := int64(-1)
		for {
			count += 2

			v := Item(0)
			switch count {
			case 1:
				v = Item(2)
			default:
				for !isPrime(count) {
					count += 2
				}
				v = Item(count)
			}
			if !yield(v) {
				return
			}
		}
	}
}

func isPrime(v int64) bool {
	a := int64(2)
	for {
		if float64(a) > math.Sqrt(float64(v)) {
			break
		}
		if v%a == 0 {
			return false
		}
		a += 1
	}
	return true
}

func main() {
	result := Item(0)
	i := 0
	for v := range Items() {
		i++

		if i == 10001 {
			result = v
			break
		}
	}

	fmt.Println(result)
}
