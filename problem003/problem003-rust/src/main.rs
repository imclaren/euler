/*
<p>The prime factors of 13195 are 5, 7, 13$ and $29.</p>
<p>What is the largest prime factor of the number 600851475143?</p>
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
    let target: f64 = 600851475143.0;
    let mut result: f64 = 0.0;

    let mut primes = Primes::new();
    loop {
        let v = primes.next();

        if let Some(v) = v {
            if v > target.sqrt() {
                break;
            }
            if (target / v) % 1.0 == 0.0 {
                result = v
            }
        } 
    }
    println!("{}", result);    
}