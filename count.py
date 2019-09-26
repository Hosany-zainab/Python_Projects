# Write a simple program that will prompt user to input a sentence.
# Your program will  count  all  lower  case  alphabets,  upper  case  alphabets,  digits,  and  special symbols.
# Then your program will display the all the counts on screen.

lower = 0
upper = 0
digits = 0
special = 0

sentence = input("Enter a sentence: ")
for word in sentence:
    if word.islower():
        lower += 1
    elif word.isupper():
        upper += 1
    elif word.isdigit():
        digits += 1
    else:
        special += 1
print("The number of lower case letter in sentence is : " + str(lower))
print("The number of upper case letter in sentence is : " + str(upper))
print("The number of digits in sentence is : " + str(digits))
print("The number of special symbols in sentence is : " + str(special))
