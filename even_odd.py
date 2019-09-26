# Write a Python program that will accept two lists of integer.
# Your program should create a third list such that it contain only odd numbers from the first list and even numbers from the second list.

list1 = []
list2 = []
list3 = []

list1 = input("Enter a set of number separated by space.")
new_list1 = list1.split(" ")

list2 = input("Enter a set of numbers separated by space.")
new_list2 = list2.split(" ")

for even in new_list2:
    if int(even) % 2 == 0:
        list3.append(even)


for odd in new_list1:
    if int(odd) % 2 != 0:
        list3.append(odd)

print("List 1 = " + str(new_list1))
print("list 2 = " + str(new_list2))
print("list 3 = " + str(list3))
