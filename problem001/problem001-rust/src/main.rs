/*
<p>If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3, 5, 6$ and $9$. The sum of these multiples is $23$.</p>
<p>Find the sum of all the multiples of $3$ or $5$ below $1000$.</p>
*/

fn main() {
    let mut result: u64 = 0;

    let mut i: u64 = 0;
    while i < 999 {
        i+=1;

        if i % 3 == 0 || i % 5 == 0  {
            result += i;
        }
    }

    println!("{}", result);
}