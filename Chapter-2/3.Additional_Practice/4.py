'''4. Type Casting (Explicit & Implicit)
Problem:
Write a Python program that demonstrates both implicit and explicit typecasting.'''

#Explicit
a=23
b=str(a)
print(b,type(b))

#Implicit
num1=23
num2=34.87
check=num1*num2
print(check, type(check)) #Here check value is automatically set out to float.