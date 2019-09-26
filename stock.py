# Write a Python program for the stock of a pharmacy, with menu:
# 1. Add an item to stock pharmacy,
# 2. Remove item from stock,
# 3. Insert item at specified position.
# Your program should do all the operations. Hint: use list.

while True:
    stock = ['stock1', 'stock2', 'stock3', 'stock4', 'stock5', 'stock6']

    print("what do yo want to do?")
    print("Press 1 to Add an item\nPress 2 to remove an iem\nPress 3 to insert an item")

    choice = int(input("Enter your decision : "))

    if choice == 1:
        add_item = input("Enter your item: ")
        stock.append(add_item)
        print(stock)
    elif choice == 2:
        remove_item = input("Which item do you want to remove: ")
        stock.remove(remove_item)
        print(stock)
    elif choice == 3:
        insert_item = input("Enter the item you want to insert: ")
        position = int(input("Enter the position you want to insert the item: "))
        stock.insert(position - 1, insert_item)
        print(stock)
    else:
        print("You enter the wrong choice")

    print("Do you want to continue, choose 1 to continue or 2 to stop: ")
    reply = int(input("Enter your choice: "))
    if reply == 2:
        print("You are exiting the program.")
        break