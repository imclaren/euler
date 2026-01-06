/*
<p>If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3, 5, 6$ and $9$. The sum of these multiples is $23$.</p>
<p>Find the sum of all the multiples of $3$ or $5$ below $1000$.</p>
*/

package main

import (
	"fmt"
	"iter"
)

type Item int64

func Items() iter.Seq[Item] {
	return func(yield func(Item) bool) {
		a := Item(1)
		b := Item(2)

		count := 0
		for {
			count += 1

			v := Item(0)
			switch count {
			case 1:
				v = a // 1
			case 2:
				v = b // 2
			default:
				old_b := b
				b = a + b
				a = old_b
				v = b
			}
			if !yield(v) {
				return
			}
		}
	}
}

func main() {
	result := Item(0)

	for v := range Items() {
		if v >= 4000000 {
			break
		}
		if v%2 == 0 {
			result += v
		}
	}

	fmt.Println(result)
}
