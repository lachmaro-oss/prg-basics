#A computer program analyses the price of a product in an online store. If the product price decreases by at least 10%, the program prin    ts a purchase recommendation:

#Buy the product!!
#Product price reduced by 17%

Current_product_price = 140.00
reduction = 0 
helloshop = input('welcome do you wnat some extra priceses (;?  (Y/N) ')

for i in range(5):    #How many reductions (: 
    if helloshop == 'Y':
         gui = input(f'you have to wait for price reduction curent price: {Current_product_price} enter (S) to skip waiting time: ')
         reduction = Current_product_price - (Current_product_price * 0.90)
         if gui == 'S' and Current_product_price > reduction:
            Current_product_price = Current_product_price - reduction
            print(F'New Price {Current_product_price}')
         if Current_product_price < 140:
             print('Buy the Product!!')
             print(f'product reduced by 10 % ')
    

