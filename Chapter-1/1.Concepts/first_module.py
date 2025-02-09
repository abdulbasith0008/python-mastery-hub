'''### MODULES
A module is a file containing Python code that can be imported and used in our programs. 
These modules can be built-in or external.

#### TYPES OF MODULES
1. **Built-in Modules** – Preinstalled in Python (e.g., `os`, `random`).
2. **External Modules** – Need to be installed using `pip` (e.g., `flask`, `tensorflow`).

---

### PIP – Python Package Installer
`pip` is the package manager for Python. It allows us to install external modules.

To install a module using `pip`, run:

```sh
pip install flask  # Installs the Flask module
```

---

just try to understand these program using chatgpt.

#Module- Module is something like using someone's already written's code.'''


#Example for extenal module usage

import pyjokes #External module to get jokes. To use , First install the module through command in terminal (pip install pyjokes).

print("Printing Jokes....!") #This prints the given value "Printing Jokes....!""

joke=pyjokes.get_joke() #This fucntion gets a random joke and assign it to joke variable.

print(joke) #This prints the value of joke variable. 



'''2️⃣ Modules
Problem: Import the random module and generate a random number between 1 and 100.

🔹 Hint: Use random.randint(a, b) to generate a random number.'''



#Example for internal module
import random
number=random.randint(1,100)
print(number)


''' PIP (Installing External Modules)
Problem: Install the emoji module using pip and print a smiley face emoji (😀).

🔹 Hint: Run pip install emoji, then use emoji.emojize().'''

import emoji
print(emoji.emojize("New Emoji is :thumbs_up:"))
print(emoji.emojize("New Emoji is :red_heart:"))

#Try different external modules using chatgpt. 
# Practice asking the chatgpt for 5 most used modules adn try it out.

