"""Week 1 (C): Recursive program to print the first n terms of the Fibonacci series."""


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    n = int(input("Enter number of terms: "))
    print("Fibonacci series:", end=" ")
    for i in range(n):
        print(fib(i), end=" ")
    print()
