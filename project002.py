inventory1 = ['pepperoni','sausage','cheese','peppers']
inventory2 = []
item1 = input("please give me a topping:")
if item1 in inventory1:
    print('yes,we have that')
    inventory2.append(item1)
else:
    print('no,we don\'t have {}'.format(item1))
    
item2 = input("please give me one more topping:")
if item2 in inventory1:
    print('yes,we have that')
    inventory2.append(item2)
else:
    print("no,we don't have that")

print("here are your toppings:")
print(inventory2)
