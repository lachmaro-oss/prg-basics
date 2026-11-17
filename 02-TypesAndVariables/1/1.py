def f(amount_to_pay):
    coins_5 = amount_to_pay // 5
    remainder = amount_to_pay % 5
    coins_2 = remainder // 2
    coins_1 = remainder % 2
    return coins_5 + coins_2 + coins_1


if __name__ == "__main__":
    print(f(23))
    print(f(8))