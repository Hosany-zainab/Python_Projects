# Write a Python program that will accept four lists of four values.
# Then your program should find the list whose sum of elements is the highest and display the list.

counter = 1
total1 = 0
total2 = 0
total3 = 0
total4 = 0
list1 = []
list2 = []
list3 = []
list4 = []

list1 = input("Enter a set of number of 4 elements: ")
newList1 = list1.split(" ")
count1 = newList1.__len__()

list2 = input("Enter a set of number of 4 elements ")
newList2 = list2.split(" ")
count2 = newList2.__len__()

list3 = input("Enter a set of number of 4 elements ")
newList3 = list3.split(" ")
count3 = newList3.__len__()

list4 = input("Enter a set of number of 4 elements ")
newList4 = list4.split(" ")
count4 = newList4.__len__()

if (count1 == 4) and (count2 == 4) and (count3 == 4) and (count4 == 4):
    for values1 in newList1:
        total1 += int(values1)

    for values2 in newList2:
        total2 += int(values2)

    for values3 in newList3:
        total3 += int(values3)

    for values4 in newList4:
        total4 += int(values4)
else:
    print("Invalid number of length")
highest = max(total1, total2, total3, total4)

if total1 == highest:
    print("The highest sum in the list is " + str(newList1))
elif total2 == highest:
    print("The highest sum in the list is " + str(newList2))
elif total3 == highest:
    print("The highest sum in the list is " + str(newList3))
else:
    print("The list with the highest sum is " + str(newList4))
