/*
A number is a perfect square, or a square number, if it is the square of a positive integer.
For example, 25 is a square number because 5^2 = 5 times 5 = 25 - it is also an odd square.
The first 5 square numbers are: 1, 4, 9, 16, 25, and the sum of the odd squares is 1 + 9 + 25 = 35.
Among the first 513 thousand square numbers, what is the sum of all the odd squares
*/

fn main() {
    let mut result: f64 = 0.0;

    let mut i: f64 = 0.0;
    while i < 826000.0 {
        i+=1.0;

        // Get the square of i
        let x = i.powf(2.0);

        // Check if odd
        if x % 2.0 != 0.0 {

            // Sum of odd squares
            result += x;
        }
    }

    println!("{}", result);
}