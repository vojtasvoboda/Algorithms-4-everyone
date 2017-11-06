def fib(n):
    """
    The fibonacci numbers are [0, 1, 1, 2, 3, 5, 8, 13, ....]. Except the first 2
    terms in this sequence, every term = the sum of the 2 previous terms, for example
    13 = 8 + 5.
    This algorithm is very simple, if the input is 0 or 1 then the answer is 0 or
    1 respectively, if not then get the fib of the 2 previous numbers and add them.
    This algorithm uses the Divide and Conquer technique as the problem is divided
    into 2 subproblems. Unfortunately this technique is not good at all with problems
    like this one in terms of time complexity as this algorithm roughly works in big
    O(2 ^ n) as it repeats all the computations many times (except for fib(n) and
    fib(n - 1) themselves which are computed once).
    See the FibonacciSequenceDP file in 'Dynamic Programming' folder to see a more
    optimized solution that works in O(n)
    """

    if (n == 0 or n == 1):
        # The input is actually one of the base cases so return the result
        return n

    # Compute the result of the 2 previous terms and add them together
    return fib(n - 1) + fib(n - 2)

n = input("Please enter a non negative integer\n")
print("fib({0}) = {1}".format(n, fib(n)))
