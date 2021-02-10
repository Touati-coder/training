'''
write a simple code to take 2 numbers from the user 
and print the numbers between them
'''

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
print("------------")

for number in range(number1, number2+1):
    print(number)