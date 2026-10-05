def add_item(cart):
    itemname=input("Enter Item Name :: ")
    cart.append(itemname)
    print("Item Added Successfully !!! ")


def remove_item(cart):
    itemname=input("Enter Item Name :: ")
    if itemname in cart:
        cart.remove(itemname)
        print("Item has been deleted from cart !!! ")
    else:
        print("Item Not FOund ")

def show_cart(cart):
    print("Cart Items :: ",cart)


cart=[]

while True:
    print("1. Add Item \n2. Remove Item \n3. Show \n4. Exit")
    choice=int(input("Enter Choice :: "))
    if choice==1:
        add_item(cart)
    elif choice==2:
        remove_item(cart)
    elif choice==3:
        show_cart(cart)
    elif choice==4:
        print("Thank YOu ")
        break
    else:
        print("Invalid Choice ")
