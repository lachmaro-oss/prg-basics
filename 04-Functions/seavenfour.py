

def how_many_e_in_text(text):
    
    e = 0
     
    for char in text:
        if char == 'e':
            e += 1

    return e


def range(x , y): 
    if x >= 0 and y <= 12:
      return "yes"
    else:       
      return "no" 

    return range



if __name__ == "__main__":
    print(f"e in text eliza {how_many_e_in_text('eeliza'  )}")   
    print(f"e is in range? {range(2 , 12)}")   
           