### **TYPE() FUNCTION AND TYPECASTING**
'''- The `type()` function is used to check the data type of a variable.
- Typecasting allows us to convert one data type into another.

#### **Example:**
```python
a = 31
print(type(a))  # Output: <class 'int'>

b = "31"
print(type(b))  # Output: <class 'str'>

# Typecasting examples
print(str(31))  # Converts integer to string
print(int("32"))  # Converts string to integer
print(float(32))  # Converts integer to float
```

---

### **IMPLICIT VS EXPLICIT TYPE CASTING**
#### **Implicit Type Casting:**
Python automatically converts one data type to another when necessary, without user intervention.

#### **Example:**
```python
x = 5  # Integer
y = 2.5  # Float
result = x + y  # Python implicitly converts 'x' to float
print(result, type(result))  # Output: 7.5 <class 'float'> Here user didn't change it manually .
```

#### **Explicit Type Casting:**
Explicit type conversion requires the programmer to manually convert one type to another using functions like `int()`, `float()`, or `str()`.

#### **Example:**
```python
num_str = "100"
num_int = int(num_str)  # Explicitly converting string to integer
print(num_int, type(num_int))  # Output: 100 <class 'int'>
```
'''


a=23
b="shaik"
c=True
d=345.76
e=None

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))


#Typecasting 

#1.Explicit Type casting

#*Changing from string to integer
shaik="23" #Assigned string value of 23
print(type(shaik)) #prints str
changed=int(shaik) #changed the shaik value of string in to integer and stored in changed
print(changed, type(changed)) #prints "23" and int type


#*Changing from integer to string

integer=45
print(integer,type(integer))
changed=str(integer)
print(changed, type(changed))

#*String to float
a="31.2"
b=float(a) #Here string value is being converted to float
print(b,type(b))

#float to string
a=23.44
b=int(a) #Here float value is converetd in to int
print(b, type(b))

#*None to string
a=None
b=str(a) #Here None value is converted in to string
print(b,type(b))

