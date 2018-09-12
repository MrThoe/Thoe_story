"""
Write a program that will take a number (Integers only) and 
return a statement that will let the user know if it is even or odd
"""
x = float(input("Please enter a number (Integer please): "))
if (x%2 == 0):
    print ("This is an EVEN number! ")

elif (x%2 == 1):
    print ("This is an ODD number! ")

else:
    print ("This is NOT an integer! ")