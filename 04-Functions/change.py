def input_string(message):
    return input(message)

def input_integer(message):
    return int(input(message))

def input_real(message):
    return float(input(message))

def input_boolean(message):
    answer = input(message).strip().lower()
    if answer == 'y':
        return True
    elif answer == 'n':
        return False
    return False

if __name__ == "__main__":
    print(input_boolean, input_integer, input_real, input_string)
