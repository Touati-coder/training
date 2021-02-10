'''
write a simple code to take a number from the use then check
if this number is less 20 or not if it is less than 20
print the numbers from this number to 50 but increasing by 3 
if it is not less than 20 print the numbers between this number
and 50 but increasing by 2
'''

number = int(input("Enter the number: "))
print("------------")

if number < 20:
    for x in range(number, 51, 3):
        print(x)
else:
    for x in range(number, 51, 2):
        print(x)