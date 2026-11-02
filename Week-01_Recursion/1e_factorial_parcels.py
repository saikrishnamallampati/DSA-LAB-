"""Week 1 (E): Recursive factorial (n!) for parcel arrangement.

n parcels can be arranged in n! different ways.
"""


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    n = int(input("Enter number of parcels: "))
    print(f"{n} parcels can be arranged in {factorial(n)} ways ({n}! = {factorial(n)})")
