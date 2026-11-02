"""Week 1 (B): Recursive calculation of P^n (compound interest growth factor).

P = growth factor per year (e.g. 1.05 for 5% interest), n = number of years.
"""


def power(p, n):
    if n == 0:
        return 1
    return p * power(p, n - 1)


if __name__ == "__main__":
    p = float(input("Enter growth factor P (e.g. 1.05): "))
    n = int(input("Enter number of years n: "))
    print(f"P^n = {power(p, n):.4f}")
