

def hide(card_number):
    card_str = str(card_number)
    result = ""

    for i in range(16):
        if i < 2 or i >= 12:
            if i < len(card_str):
                result += card_str[i]  # Zostają indeksy 0, 1 oraz 12, 13, 14, 15
            else:
                result += "*"          # Gdyby podany numer był krótszy niż 16 znaków
        else:
            result += "*"              # Środek (indeksy od 2 do 11) to 10 gwiazdek

    return result


if __name__ == "__main__":
    print(f"code is {hide(1234567812345678)}")
        