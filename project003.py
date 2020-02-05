print('welcom to the receipt program')
total=0.0
while True:
    price=input("Enter the value for the seat ['q' to quit]:")
    price1=price.replace('.','')
    if price == 'q':
        break
    while not price1.isdigit():
        print("I'm sorry,but'{}' isn't valid.Please try again".format(price))
        price=input("Enter the value for the seat ['q' to quit]:")
    total=total+float(price)
print(round(total,1))

    
