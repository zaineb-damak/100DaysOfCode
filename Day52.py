import os, time

myPizza = []

try:
    f = open("pizza_shop.txt", "r")
    myPizza = eval(f.read())
    f.close()
except:
    print('error : No existing pizza list, using a blank list')
    time.sleep(1)
    os.system("clear")


def addPizza():
    time.sleep(1)
    os.system("clear")
    name = input("Name: ")
    toppings = input("Toppings: ")
    size = input("size (s/m/l): ").lower()
    while True :
        try:
            qty = int(input("Quantity: "))
            break
        except:
            print("error : Quantity must be a whole number")
    cost = 0
    if size == "s":
        cost = 5.0
    elif size == "m":
        cost = 7.0
    else:
        cost = 14.99
    total = cost*qty
    row = [name, toppings, size, qty, total]
    myPizza.append(row)

def viewPizza():
    v1 = "Name"
    v2 = "Topping"
    v3 = "Size"
    v4 = "Quantity"
    v5 = "Total"
    print(f"{v1:^10}{v2:^10}{v3:^10}{v4:^10}{v5:^10}")

    for row in myPizza:
        print(f"{row[0]:^10}{row[1]:^10}{row[2]:^10}{row[3]:^10}{row[4]:^10}")
        

while True :
    print("Pizza Shop")
    print()
    menu = input("1: Add Pizza\n2: View Pizzas\n")
    if menu == "1":
        addPizza()
    else:
        viewPizza()
    
    f = open("pizza_shop.txt","w")
    f.write(str(myPizza))
    f.close()

