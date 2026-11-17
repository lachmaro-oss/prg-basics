def f(sentence):
    return sum(ord(char) for char in sentence) % 3 == 0


if __name__ == "__main__":
    print(f("hello world"))
    print(f("university"))
    print(f("student"))