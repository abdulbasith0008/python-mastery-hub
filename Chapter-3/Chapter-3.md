**CHAPTER 3 – STRINGS**

A string is a data type in Python that represents a sequence of characters enclosed in quotes. Strings can be defined using:

```python
a = 'shaik'  # Single-quoted string
b = "shaik"  # Double-quoted string
c = '''shaik'''  # Triple-quoted string
```

### **STRING SLICING**
String slicing allows us to extract a part of a string using index positions. The index starts from `0` to `length - 1` in Python.

#### **Basic Slicing Syntax:**
```python
word = "amazing"
print(word[1:6])  # Output: "mazin"
```

#### **Negative Indices:**
Negative indices start from the end of the string:
```python
word = "amazing"
print(word[-3:-1])  # Output: "in"
```

#### **Slicing with Skip Value:**
We can provide a skip value to select characters at regular intervals:
```python
word = "amazing"
print(word[1:6:2])  # Output: "mzn"
```

#### **Other Advanced Slicing Techniques:**
```python
word = "amazing"
print(word[:7])  # Equivalent to word[0:7] → Output: "amazing"
print(word[0:])  # Equivalent to word[0:7] → Output: "amazing"
```

---

### **STRING FUNCTIONS**
Python provides various built-in functions to manipulate strings. Let's consider a string:
```python
str = "shaik"
```

#### **1. `len()` – Length of the String**
Returns the number of characters in the string:
```python
print(len(str))  # Output: 5
```

#### **2. `endswith(substring)` – Checks if String Ends with Given Substring**
```python
print(str.endswith("aik"))  # Output: True
```

#### **3. `count(character)` – Counts Occurrences of a Character**
```python
print(str.count("a"))  # Output: 1
```

#### **4. `capitalize()` – Capitalizes the First Character**
```python
print(str.capitalize())  # Output: "Shaik"
```

#### **5. `find(substring)` – Finds First Occurrence of a Substring**
```python
print(str.find("ai"))  # Output: 2
```

#### **6. `replace(old, new)` – Replaces Substring with Another**
```python
print(str.replace("a", "o"))  # Output: "shoik"
```

---

### **ESCAPE SEQUENCE CHARACTERS**
Escape sequence characters start with a backslash (`\`) and allow special formatting inside strings.

| Escape Sequence | Description              |
|----------------|--------------------------|
| `\n`          | New Line                 |
| `\t`          | Tab Space                |
| `\'`          | Single Quote             |
| `\"`         | Double Quote             |
| `\\`         | Backslash                 |

#### **Example:**
```python
print("Hello\nWorld")  # Output:
# Hello
# World
```

This concludes Chapter 3. Stay tuned for more Python concepts! 🚀

