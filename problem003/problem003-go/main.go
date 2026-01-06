/*
<p>The prime factors of 13195 are 5, 7, 13$ and $29.</p>
<p>What is the largest prime factor of the number 600851475143?</p>
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
	target := int64(600851475143)

	result := Item(0)
	for v := range Items() {
		if float64(v) > math.Sqrt(float64(target)) {
			break
		}
		if target%int64(v) == 0.0 {
			result = v
		}
	}

	fmt.Println(result)
}
