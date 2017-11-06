def fib(n):
    """
    The fibonacci numbers are [0, 1, 1, 2, 3, 5, 8, 13, ....]. Except the first 2
    terms in this sequence, every term = the sum of the 2 previous terms, for example
    13 = 8 + 5.
    In this algorithm, we store the results we obtain in order not to compute them again
    this technique is called dynamic programming
    this algorithm works in O(n).
    This solution is much faster than the solution that uses divide and conquer technique
    (which you can view in 'Divide & Conquer' folder). That algorithm works roughly in O(2 ^ n)
    """

    # If the given number is 0 or 1 then the result is 0 or 1 respectively
    if (n == 0 or n == 1):
        return n
    # If not, initialze the array to store the results that are needed to compute fib(n)
    fibonacci = [None] * (n + 1)
    fibonacci[0] = 0
    fibonacci[1] = 1
    for i in range(2, n + 1):
        fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2]
    return fibonacci[n]

n = input("Please enter a non negative integer\n")
print("fib({0}) = {1}".format(n, fib(n)))
