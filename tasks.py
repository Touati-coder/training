# define new variable with name x and value 2.0
x = 2.0

# prove that this variable is float
print(type(x))

# convert this variable to int
x = int(x)
print(x)

# increase the x value by 6 using assignment operator
x += 6
print(x)

# get the module of the new x by 3
print(x % 3)



# write a simple ternary operator
# if number 8 is odd or not
is_odd = True if x%2 > 0 else False
print(is_odd)

print("-----------")
# in elif , python will check all the conditios no matter what ?
qustion = "in elif , python will check all the conditios no matter what ?"
print(qustion)
print("no! if python finds a correct elif, the rest elif is ignored.")

print("-----------")

# in elif we use else for ... ?
qustion = "in elif we use else for ... ?"
print(qustion)
print("to run a code block (anyway) if all statments are false")

print("-----------")



'''
- if we have this list [2,4,6,8,10] :
	- check to see if 4 in this list or not 
	- check to see if 4 and 6 in this list on not 
	- check to see if 3 or 6 in this list 
    - check to see if 2 , 4 and 5 in this list
'''
myList = [2,4,6,8,10]

if 4 in myList:
    print("4 is in the list")
else:
    print("4 is not in the list")

if all([4 in myList, 6 in myList]):
    print("4 and 6 are in the list")
else:
    print("not both 4 and 6 in the list")

if any([3 in myList, 6 in myList]):
    print("4 or 6 in the list")
else:
    print("neither 4 nor 6 in the list")

if all([2 in myList, 4 in myList, 5 in myList]):
    print("2 , 4 and 5 are in the list")
else:
    print("2 , 4 and 5 no one of them in the list")