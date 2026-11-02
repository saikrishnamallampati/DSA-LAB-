"""Week 1 (A): Recursive countdown from n to 1, followed by 'launch'."""


def countdown(n):
    if n == 0:
        print("Launch!")
        return
    print(n)
    countdown(n - 1)


if __name__ == "__main__":
    n = int(input("Enter n: "))
    countdown(n)
