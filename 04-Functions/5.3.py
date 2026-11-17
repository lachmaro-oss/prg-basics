###
# Functions to read any data type from the keyboard
#
def input_string(message):
    x = input(message)
    return x

def input_integer(message):
    y = int(input(message))
    return y

def input_real(message):
    z = float(input(message))
    return z

def input_boolean(message):
    v = bool(input(message))
    if v == 'y':
        return True
    elif v =='n':
        return False

    return v



if __name__ == "__main__":
    print(input_boolean , input_integer , input_real, input_string)
