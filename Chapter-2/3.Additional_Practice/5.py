'''Problem:
Write a program that takes a user's name, age, and height as input and
 prints a formatted message including these details.'''

name=input("Enter your name:")
age=int(input("Enter your age:"))
height=float(input("Enter your height:"))
print(f"Hi {name},Your age is {age} and {height} feet tall ") #Here we have used the 'f' string. It is used to inlcude the values of variables inside the string directly.