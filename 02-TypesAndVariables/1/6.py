def f(number, even):
    total = 0
    for digit in str(abs(number)):
        d = int(digit)
        if even and d % 2 == 0:
            total += d
        elif not even and d % 2 != 0:
            total += d
    return total


if __name__ == "__main__":
    print(f(3124, True))
    print(f(3124, False))
    print(f(20576, False))
    print(f(20576, True))
    print(f(13115, True))