**CHAPTER 2 – VARIABLES AND DATA TYPES**

A variable is a named memory location that stores a value in a program. For example:

```python
a = 30  # 'a' is a variable storing an integer
b = "Shaik"  # 'b' is a variable storing a string
c = 71.22  # 'c' is a variable storing a floating-point number
```

### **DATA TYPES IN PYTHON**
Python automatically detects the type of data we assign to a variable. The primary data types in Python are:

1. **Integers** (`int`) – Whole numbers (e.g., `71`, `1000`)
2. **Floating point numbers** (`float`) – Numbers with decimals (e.g., `88.44`, `3.14`)
3. **Strings** (`str`) – Sequence of characters (e.g., `"Shaik"`)
4. **Booleans** (`bool`) – Represents `True` or `False`
5. **None** (`NoneType`) – Represents a null value or no value at all

#### **Example:**
```python
a = 71  # 'a' is an integer
b = 88.44  # 'b' is a float
name = "Shaik"  # 'name' is a string
print(type(a), type(b), type(name))
```

---

### **RULES FOR CHOOSING A VARIABLE NAME (IDENTIFIER)**
- A variable name can contain alphabets, digits, and underscores.
- A variable name can **only** start with an alphabet or an underscore (`_`).
- A variable name **cannot** start with a digit.
- Spaces **are not allowed** inside a variable name.

#### **Examples of valid variable names:**
```python
shaik, one8, seven, _seven, my_var
```
#### **Examples of invalid variable names:**
```python
8one (cannot start with a number)
my var (contains a space)
my-var (hyphens are not allowed)
```

---

### **OPERATORS IN PYTHON**
Operators are symbols that perform operations on values and variables. 
Some commonly used operators are:

1. **Arithmetic Operators**: `+`, `-`, `*`, `/`, `%`, `**` (exponentiation)
2. **Assignment Operators**: `=`, `+=`, `-=`, `*=`, `/=`
3. **Comparison Operators**: `==`, `!=`, `>`, `<`, `>=`, `<=`
4. **Logical Operators**: `and`, `or`, `not`

#### **Example:**
```python
a = 10
b = 5
print(a + b)  # Addition
print(a > b)  # Comparison
print(a > 5 and b < 10)  # Logical operation
```

---

### **TYPE() FUNCTION AND TYPECASTING**
- The `type()` function is used to check the data type of a variable.
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

---

### **INPUT() FUNCTION**
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

---

This concludes Chapter 2. Stay tuned for more Python concepts in upcoming chapters!

*By Shaik*

