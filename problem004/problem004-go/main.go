/*
 <p>A palindromic number reads the same both ways. The largest palindrome made from the product of two $2$-digit numbers is 9009 = 91 times 99$.</p>
 <p>Find the largest palindrome made from the product of two 3$-digit numbers.</p>
*/

package main

import (
	"fmt"
	"strconv"
)

func isPal(n int) bool {
	l := strconv.Itoa(n)
	switch len(l) {
	case 3:
		if l[0] == l[2] {
			return true
		}
	case 4:
		if l[0] == l[3] && l[1] == l[2] {
			return true
		}
	case 5:
		if l[0] == l[4] && l[1] == l[3] {
			return true
		}
	case 6:
		if l[0] == l[5] && l[1] == l[4] && l[2] == l[3] {
			return true
		}
	default:
		panic("out of range")
	}
	return false
}

func main() {
	result := 0
	for a := 100; a <= 999; a++ {
		for b := 100; b <= 999; b++ {
			v := a * b
			if isPal(v) && v > result {
				result = v
			}
		}
	}
	fmt.Println(result)
}
