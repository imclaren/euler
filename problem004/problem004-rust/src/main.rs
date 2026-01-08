/*
 <p>A palindromic number reads the same both ways. The largest palindrome made from the product of two $2$-digit numbers is 9009 = 91 times 99$.</p>
 <p>Find the largest palindrome made from the product of two 3$-digit numbers.</p>
*/

fn is_pal(n: u64) -> bool {
	let l = n.to_string();
    match l.len() {
        3 => {
            if l.chars().nth(0) == l.chars().nth(2) {
                return true;
            }
        }
        4 => {
            if l.chars().nth(0) == l.chars().nth(3) && l.chars().nth(1) == l.chars().nth(2) {
                return true;
            }
        }
        5 => {
            if l.chars().nth(0) == l.chars().nth(4) && l.chars().nth(1) == l.chars().nth(3) {
                return true;
            }
        }
        6 => {
            if l.chars().nth(0) == l.chars().nth(5) && l.chars().nth(1) == l.chars().nth(4) && l.chars().nth(2) == l.chars().nth(3) {
                return true;
            }
        }
        _ => {
            panic!("out of range")
        }
    }
    return false
}

fn main() {
    let mut result: u64 = 0;
	for a in 100..999 {
		for b in 100..999 {
			let v = a * b;
			if is_pal(v) && v > result {
				result = v
			}
		}
	}
	 println!("{}", result);  
}