function fib(n){
	/*
    The fibonacci numbers are [0, 1, 1, 2, 3, 5, 8, 13, ....]. Except the first 2
    terms in this sequence, every term = the sum of the 2 previous terms, for example
    13 = 8 + 5.
    In this algorithm, we store the results we obtain in order not to compute them again
    this technique is called dynamic programming
    this algorithm works in O(n).
    This solution is much faster than the solution that uses divide and conquer technique
    (which you can view in 'Divide & Conquer' folder). That algorithm works roughly in O(2 ^ n)
    */

    // If the given number is 0 or 1 then the result is 0 or 1 respectively
    if (n === 0 || n === 1)
		return n;

    // Compute the result of the 2 previous terms and add them together
    return fib(n - 1) + fib(n - 2);
}

var n = prompt("Please enter a non negative integer", "");
console.log(`fib(${n}) = ${fib(n)}`);
