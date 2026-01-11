/*
<p>The sum of the squares of the first ten natural numbers is,</p>
$$1^2 + 2^2 + ... + 10^2 = 385.$$
<p>The square of the sum of the first ten natural numbers is,</p>
$$(1 + 2 + ... + 10)^2 = 55^2 = 3025.$$
<p>Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.</p>
<p>Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.</p>
*/

// Fibinacci struct
struct Primes {
    count: f64,
}

// Struct new() helper method
impl Primes {
    fn new() -> Primes {
        Primes { 
            count: 0.0,
        }
    }
}

// Iterator
impl Iterator for Primes {

    // Yield u64 responses 
    type Item = f64;

    // Yield 2 then check odd numbers starting at 3
    fn next(&mut self) -> Option<Self::Item> {
        match self.count {
            0.0 => {
                self.count = 1.0; // So the next iteration will be 3
                Some(2.0)
            }
            _ => {
                loop {
                    self.count += 2.0;
                    if is_prime(self.count) {
                        break;
                    }
                }
                Some(self.count)
            }
        }
    }
}

fn is_prime(v: f64) -> bool {
	let mut a = 2.0;
	loop {
		if a > v.sqrt() {
			break;
        }
		if v % a == 0.0 {
			return false;
        }
		a += 1.0;
    }
	return true;
}

fn main() {
    let mut primes = Primes::new();

	let mut result: f64 = 0.0;
	let mut i = 0;
    while result == 0.0 {
		i+=1;

        let v = primes.next();
        if let Some(v) = v {
			if i == 10001 {
				result = v;
				break;
			} 
		}
    }
    println!("{}", result);    
}