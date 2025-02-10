'''### **INPUT() FUNCTION**
The `input()` function allows users to take input from the keyboard. 
By default, all inputs are stored as **strings**, even if a number is entered.

#### **Example:**
```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```
If the user enters `Shaik`, the output will be:
```
Hello, Shaik!
```

#### **Converting Input to Other Types:**
```python
age = int(input("Enter your age: "))  # Converts input to an integer
height = float(input("Enter your height: "))  # Converts input to a float
print("Age:", age, "Height:", height)
```
'''

user=input("Enter your name:") #using input function to get the user entered name as string
print(user)

a=input("Enter Number one:")
b=input("Enter Number two:")
print("Number one is:",a)
print("Number two is:",b)

# For example if a=1, b=2 Then what would be the output?
a=input("Enter Number one:")
b=input("Enter Number two:")
print("sum of two numbers is:",a+b) 
#output=12(Because the whole a&b values will be taken as string.)

a=int(input("Enter number one:"))#Here it is converting any value in to int
b=int(input("Enter number two:"))#Here it is converting any value in to int
print("Sum of two numbers is:",a+b) #Here the sum of two value be 3



#Let's take age of the user

user1=input("Enter your age user1:") #By default input function will take any value as string
user2=int(input("Enter your age user2:")) #Here we should use int(input) as age is a number , so this will convert the value to integer,
print(user1,type(user1))
print(user2,type(user2))




