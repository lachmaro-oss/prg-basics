def f(sentence):
    vowels = "aeiouy"
    return sum(1 for char in sentence if char in vowels)


if __name__ == "__main__":
    print(f("water"))
    print(f("hello world"))