#Enter price: 24.72
#Enter discount %: 15
#Price with discount: 21.01
#Reduction: 3.71

enterprice = float(input("enter price without discount"))
enterdiscount = float(input("enter discount"))
pricewithdisc = enterprice * enterdiscount
reduction1 = enterprice - pricewithdisc
reduction2 = enterprice - reduction1
print(f"{enterprice:.2f}")
print(f"{enterdiscount:.2f}")
print(f"{reduction1:.2f}")
print(f"{reduction2:.2f}")