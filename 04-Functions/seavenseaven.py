def binary(n):
    n_str = str(n)  

    for char in n_str:
        if char not in ('0', '1'):
            return False  

    return True  


if __name__ == "__main__":
    print(binary(10001))  
    print(binary(1221))   