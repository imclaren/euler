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

fn main() {
    let mut result: f64 = 20.0;
	let mut done = false;
	while !done {
		done = true;
		result += 20.0;
		for a in 1..20 {
			let v = result / (a as f64);
			if v % 1.0 != 0.0 {
				done = false;
				break;
			}
		}
	}
    println!("{}", result);    
}