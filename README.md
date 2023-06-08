# e_python_task

Fibonaccier:  Read positive (>0) number n (from stdin or cmdline).

Make 2 asynchronous/concurrent calls to a function fib(...) which
(a) includes a random delay of up to 1 second
(b) calculates and returns the fibonacci number calculated using the following recursive formula:

Fib(0) = 0
Fib(1) = 1
Fib(n) = Fib(n-1) + Fib(n-2)

Wait until both of the asynchronous calls finish.

Print out the resulting Fibonacci number Fib(n), and which one of the two calls finished out first.

If you are unsure how to go about it, consider implementing the solution incrementally e.g. as follows:
1. Implement a synchronous Fibonacci function without the random delay. Verify it produces the correct result.
2. Change it into an async function. Verify it still works.
3. Add the random delay into the function.
4. Implement the 2 concurrent async calls to this function


