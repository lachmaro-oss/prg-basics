#In one of the online stores, a 25% discount is charged for each product purchased over two. Write a program that calculates the amount to be paid. Read the number of purchased products and the product price from the keyboard. Sample result:

#Number of products purchased: 5
#Product price: 40
#Amount to pay: 170.00


Number_of_products = int(input("How many products you wanna buy?: "))
product_price = float(input("Enter price of the product: "))
discount = 0
even = 0 

if Number_of_products % 2 == 0:
    print('discount 25%')
elif Number_of_products % 2 == 1:
    print('one discount for two products and one product with normal price')

else:
    print('no disocunt')



if Number_of_products == 1: 
    print(f'You bougt one product so yore paying normal price of {product_price} PLN')
elif Number_of_products == 2:
    product_price *= 2  
    discount = product_price * 0.25
    print(f'Product price {product_price}')
    print(f'your buying 2 products with 25% discount so final price is {product_price - discount} ')
elif Number_of_products > 2:
    


    print(f'Product price {product_price}')
    print(f'your buying {Number_of_products} products with 25% discount so final price is {product_price - discount} ')