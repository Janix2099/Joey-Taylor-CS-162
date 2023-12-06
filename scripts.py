# File for random dialogue scripts!

#############################################################

# RANDOM QUIZ QUESTIONS

#############################################################


quiz_questions = {
    "Q1": {
        "question": "What is the data type of [1, 2, 3]?",
        "options": ["A) String", "B) List", "C) Dictionary"],
        "answer": "B",
        "explanation": "The correct data type is a List. In Python, lists are defined by square brackets."
    },
    "Q2": {
        "question": "How do you print 'Hello World' in Python?",
        "options": ["A) echo('Hello World')", "B) print('Hello World')", "C) console.log('Hello World')"],
        "answer": "B",
        "explanation": "In Python, you use the print function to output text to the console."
    },
    "Q3": {
        "question": "Which keyword creates a function in Python?",
        "options": ["A) function", "B) def", "C) create"],
        "answer": "B",
        "explanation": "The keyword 'def' is used in Python to start a function declaration."
    },
    "Q4": {
        "question": "How can you access the first element of a list named 'myList'?",
        "options": ["A) myList[0]", "B) myList[1]", "C) myList[first]"],
        "answer": "A",
        "explanation": "List indices in Python are zero-based, so the first element is accessed with myList[0]."
    },
    "Q5": {
        "question": "What will be the output of 8 % 3 in Python?",
        "options": ["A) 2", "B) 2.67", "C) 3"],
        "answer": "A",
        "explanation": "The modulo operator % returns the remainder of the division, so 8 % 3 is 2."
    },
    "Q6": {
        "question": "Which of the following is a mutable data type?",
        "options": ["A) String", "B) Tuple", "C) List"],
        "answer": "C",
        "explanation": "Lists are mutable, meaning they can be changed after creation, unlike strings and tuples."
    },
    "Q7": {
        "question": "How do you create a dictionary with the keys 'a' and 'b'?",
        "options": ["A) {'a':1, 'b':2}", "B) ['a':1, 'b':2]", "C) ('a':1, 'b':2)"],
        "answer": "A",
        "explanation": "Dictionaries are created with curly braces and key-value pairs separated by colons."
    },
    "Q8": {
        "question": "What is a correct way to declare a comment in Python?",
        "options": ["A) // This is a comment", "B) <!-- This is a comment -->", "C) # This is a comment"],
        "answer": "C",
        "explanation": "In Python, comments start with a hash (#) symbol."
    },
    "Q9": {
        "question": "Which function can turn a string into an integer?",
        "options": ["A) int()", "B) strToInt()", "C) parse()"],
        "answer": "A",
        "explanation": "The int() function is used to convert a string to an integer, if possible."
    },
    "Q10": {
        "question": "What does the 'len' function do?",
        "options": ["A) Returns the length of an object", "B) Changes the value of an object", "C) Prints the type of an object"],
        "answer": "A",
        "explanation": "The len() function returns the number of items in an object."
    },
    "Q11": {
        "question": "How do you create a tuple in Python?",
        "options": ["A) ()", "B) []", "C) {}"],
        "answer": "A",
        "explanation": "A tuple is created by placing all the items inside parentheses (), separated by commas."
    },
    "Q12": {
        "question": "What is the output of 'Hello' + 'World'?",
        "options": ["A) HelloWorld", "B) 'HelloWorld'", "C) 'Hello World'"],
        "answer": "B",
        "explanation": "The + operator concatenates strings without adding space."
    },
    "Q13": {
        "question": "How do you handle exceptions in Python?",
        "options": ["A) try...catch", "B) try...except", "C) try...handle"],
        "answer": "B",
        "explanation": "The try...except block is used to handle exceptions in Python."
    },
    "Q14": {
        "question": "Which method adds an element to the end of a list?",
        "options": ["A) .append()", "B) .add()", "C) .push()"],
        "answer": "A",
        "explanation": "The .append() method adds an element to the end of a list."
    },
    "Q15": {
        "question": "What does the 'break' keyword do?",
        "options": ["A) Stops a loop", "B) Exits a program", "C) Breaks a line of code"],
        "answer": "A",
        "explanation": "The 'break' keyword is used to exit a loop before it has gone through all the items."
    },
    "Q16": {
        "question": "Which of the following is not a Python data type?",
        "options": ["A) list", "B) array", "C) dictionary"],
        "answer": "B",
        "explanation": "While lists and dictionaries are Python data types, arrays are not unless using a module like numpy."
    },
    "Q17": {
        "question": "What is the result of '3' * 2 in Python?",
        "options": ["A) '33'", "B) '32'", "C) 6"],
        "answer": "A",
        "explanation": "When a string is multiplied by an integer n, the string is repeated n times."
    },
    "Q18": {
        "question": "How do you create a set in Python?",
        "options": ["A) <>", "B) []", "C) {}"],
        "answer": "C",
        "explanation": "A set is created by placing all the items inside curly braces {}, separated by commas."
    },
    "Q19": {
        "question": "What does the 'continue' keyword do in a loop?",
        "options": ["A) Pauses the loop", "B) Skips to the next iteration", "C) Stops the loop"],
        "answer": "B",
        "explanation": "The 'continue' keyword skips the current iteration of a loop and continues with the next one."
    },
    "Q20": {
        "question": "What does the 'is' operator do?",
        "options": ["A) Compares values", "B) Compares identities", "C) Checks for membership"],
        "answer": "B",
        "explanation": "The 'is' operator checks whether two variables refer to the same object."
    },
    "Q21": {
        "question": "How is a class defined in Python?",
        "options": ["A) class ClassName:", "B) new ClassName:", "C) def ClassName:"],
        "answer": "A",
        "explanation": "A class is defined in Python by using the 'class' keyword followed by the class name and a colon."
    },
    "Q22": {
        "question": "What is the correct way to import a module named 'math'?",
        "options": ["A) include math", "B) using math", "C) import math"],
        "answer": "C",
        "explanation": "In Python, you use the 'import' statement to include a module."
    },
    "Q23": {
        "question": "What will be the output of the expression: 3 ** 2?",
        "options": ["A) 6", "B) 8", "C) 9"],
        "answer": "C",
        "explanation": "The ** operator is used for exponentiation in Python, so 3 ** 2 is 9."
    },
    "Q24": {
        "question": "Which of the following is the correct way to define a lambda function that returns its input plus 10?",
        "options": ["A) lambda x: x + 10", "B) x => x + 10", "C) function(x) { return x + 10; }"],
        "answer": "A",
        "explanation": "Lambda functions in Python are defined using the 'lambda' keyword."
    },
    "Q25": {
        "question": "How do you check if 'apple' is in the list ['banana', 'cherry', 'apple']?",
        "options": ["A) 'apple' in list", "B) list.contains('apple')", "C) 'apple' is list"],
        "answer": "A",
        "explanation": "The 'in' keyword is used in Python to check membership in a sequence."
    },
    "Q26": {
        "question": "What is slicing in Python?",
        "options": ["A) Cutting a list into half", "B) Removing an element from a list", "C) Getting a subset of a sequence"],
        "answer": "C",
        "explanation": "Slicing in Python is used to get a subset of items from a sequence types like lists, strings, or tuples."
    },
    "Q27": {
        "question": "What is the output of list('hello')?",
        "options": ["A) ['hello']", "B) ['h', 'e', 'l', 'l', 'o']", "C) SyntaxError"],
        "answer": "B",
        "explanation": "The list function will convert the string into a list of its characters."
    },
    "Q28": {
        "question": "How can you handle exceptions in Python?",
        "options": ["A) handle Exception", "B) except block", "C) try...except"],
        "answer": "C",
        "explanation": "The try...except block in Python is used to handle exceptions and errors."
    },
    "Q29": {
        "question": "What is the output of bool('')?",
        "options": ["A) True", "B) False", "C) None"],
        "answer": "B",
        "explanation": "Empty strings are considered False in Python when converted to a boolean."
    },
    "Q30": {
        "question": "What is the term for a function defined inside another function?",
        "options": ["A) Inner function", "B) Nested function", "C) Sub function"],
        "answer": "B",
        "explanation": "Functions defined inside other functions are known as nested functions."
    },
    "Q31": {
        "question": "What keyword is used to create an iterator in Python?",
        "options": ["A) iter", "B) for", "C) yield"],
        "answer": "C",
        "explanation": "The 'yield' keyword is used within a function to turn it into a generator, which is a type of iterator."
    },
    "Q32": {
        "question": "How do you create a virtual environment in Python?",
        "options": ["A) venv", "B) virtualenv", "C) Both A and B"],
        "answer": "C",
        "explanation": "Both 'venv' and 'virtualenv' are tools to create isolated Python environments."
    },
    "Q33": {
        "question": "Which method is called when an object is created?",
        "options": ["A) __init__()", "B) __start__()", "C) __create__()"],
        "answer": "A",
        "explanation": "The __init__() method is called a constructor and is automatically invoked when creating an object."
    },
    "Q34": {
        "question": "How do you declare a comment in Python?",
        "options": ["A) //", "B) #", "C) <!-- -->"],
        "answer": "B",
        "explanation": "Comments in Python are declared with a '#' symbol."
    },
    "Q35": {
        "question": "Which module can be used for serializing and deserializing objects in Python?",
        "options": ["A) json", "B) pickle", "C) Both A and B"],
        "answer": "C",
        "explanation": "Both 'json' and 'pickle' modules can be used for object serialization (turning objects into a byte stream) and deserialization in Python."
    },
    "Q36": {
        "question": "How do you remove duplicates from a list in Python?",
        "options": ["A) Using a set", "B) With a for loop", "C) Both A and B"],
        "answer": "C",
        "explanation": "You can use a set to remove duplicates or a loop to check and remove them."
    },
    "Q37": {
        "question": "What are decorators in Python?",
        "options": ["A) A way to change the appearance of the code", "B) Functions that modify the functionality of another function", "C) Tools to organize code"],
        "answer": "B",
        "explanation": "Decorators are a powerful aspect of Python programming, allowing you to modify the behavior of a function or method."
    },
    "Q38": {
        "question": "What does the 'pass' keyword do?",
        "options": ["A) Passes the execution to the next line", "B) Acts as a placeholder", "C) Passes a variable to a function"],
        "answer": "B",
        "explanation": "The 'pass' keyword does nothing and acts as a placeholder where syntactically some code is required."
    },
    "Q39": {
        "question": "Which operator is used for floor division in Python?",
        "options": ["A) /", "B) //", "C) %"],
        "answer": "B",
        "explanation": "The // operator is used for floor division, which rounds the result down to the nearest whole number."
    },
    "Q40": {
        "question": "What is a dictionary in Python?",
        "options": ["A) A list of words with definitions", "B) A mutable collection of key-value pairs", "C) A type of function"],
        "answer": "B",
        "explanation": "In Python, a dictionary is a collection of key-value pairs where each key is unique."
    },
    "Q41": {
        "question": "What method is used to add an element at a specific position in a list?",
        "options": ["A) .append()", "B) .insert()", "C) .add()"],
        "answer": "B",
        "explanation": "The .insert() method is used to add an element at a specified index in a list."
    },
    "Q42": {
        "question": "What is the purpose of the 'global' keyword?",
        "options": ["A) To create a global variable", "B) To access a global variable inside a function", "C) To make a function global"],
        "answer": "B",
        "explanation": "The 'global' keyword is used inside a function to refer to a variable defined outside the function."
    },
    "Q43": {
        "question": "What is the difference between '==' and 'is' in Python?",
        "options": ["A) '==' checks values, 'is' checks identities", "B) '==' checks identities, 'is' checks values", "C) No difference"],
        "answer": "A",
        "explanation": "'==' compares the values of objects, while 'is' compares their identities (memory locations)."
    },
    "Q44": {
        "question": "How can you concatenate two lists in Python?",
        "options": ["A) Using + operator", "B) Using .concat()", "C) Using .merge()"],
        "answer": "A",
        "explanation": "Lists in Python can be concatenated using the + operator."
    },
    "Q45": {
        "question": "What is slicing in Python?",
        "options": ["A) A technique to split a string", "B) Cutting a list into smaller parts", "C) Creating a subset of a sequence"],
        "answer": "C",
        "explanation": "Slicing is used to create a subset of a sequence (like a list or string) using indices."
    },
    "Q46": {
        "question": "How do you create a copy of a list in Python?",
        "options": ["A) list.copy()", "B) copy(list)", "C) list.clone()"],
        "answer": "A",
        "explanation": "The .copy() method creates a shallow copy of a list."
    },
    "Q47": {
        "question": "What is the purpose of the 'else' clause in a 'try...except' block?",
        "options": ["A) To catch all exceptions", "B) To execute code if no exceptions occur", "C) To run final cleanup actions"],
        "answer": "B",
        "explanation": "The 'else' clause in a 'try...except' block executes if no exceptions are raised in the try block."
    },
    "Q48": {
        "question": "What does the 'del' keyword do?",
        "options": ["A) Deletes an object", "B) Marks an object for garbage collection", "C) Declares a variable"],
        "answer": "A",
        "explanation": "The 'del' keyword is used to delete objects like variables, items in a list, or slices of a list."
    },
    "Q49": {
        "question": "What is a lambda function in Python?",
        "options": ["A) A high-order function", "B) An anonymous function", "C) A named function"],
        "answer": "B",
        "explanation": "Lambda functions are small anonymous functions defined using the lambda keyword."
    },
    "Q50": {
        "question": "How do you reverse a list in Python?",
        "options": ["A) list.reverse()", "B) reverse(list)", "C) list[::-1]"],
        "answer": "C",
        "explanation": "You can reverse a list by slicing with list[::-1]."
    },
    "Q51": {
        "question": "Which method removes and returns the last element of a list?",
        "options": ["A) .pop()", "B) .push()", "C) .drop()"],
        "answer": "A",
        "explanation": "The .pop() method removes and returns the last item of a list."
    },
    "Q52": {
        "question": "What does the 'enumerate' function do?",
        "options": ["A) Counts the number of elements in a sequence", "B) Adds a counter to an iterable", "C) Enumerates through a dictionary"],
        "answer": "B",
        "explanation": "'enumerate' adds a counter to an iterable and returns it as an enumerate object."
    },
    "Q53": {
        "question": "What is a list comprehension?",
        "options": ["A) A concise way to create lists", "B) A method to concatenate lists", "C) A tool for list sorting"],
        "answer": "A",
        "explanation": "List comprehensions provide a concise way to create lists from existing lists."
    },
    "Q54": {
        "question": "What does the 'range' function do?",
        "options": ["A) Generates a sequence of numbers", "B) Defines a range of values for a variable", "C) Sets the range for a loop"],
        "answer": "A",
        "explanation": "The 'range' function generates a sequence of numbers, often used in for loops."
    },
    "Q55": {
        "question": "What is the output of 'not True' in Python?",
        "options": ["A) True", "B) False", "C) None"],
        "answer": "B",
        "explanation": "The 'not' keyword in Python is a logical operator used to reverse the truth value."
    },
    "Q56": {
        "question": "What is 'self' in Python classes?",
        "options": ["A) Refers to the class itself", "B) Refers to the instance of the class", "C) A keyword for inheritance"],
        "answer": "B",
        "explanation": "'self' in Python classes refers to the instance of the class itself."
    },
    "Q57": {
        "question": "How do you create an empty dictionary?",
        "options": ["A) {}", "B) []", "C) ()"],
        "answer": "A",
        "explanation": "An empty dictionary is created using empty curly braces {}."
    },
    "Q58": {
        "question": "What does the 'zip' function do?",
        "options": ["A) Compresses files", "B) Concatenates lists", "C) Combines several iterables into tuples"],
        "answer": "C",
        "explanation": "The 'zip' function takes iterables and aggregates them into tuples."
    },
    "Q59": {
        "question": "What is a generator in Python?",
        "options": ["A) A tool to generate random numbers", "B) A type of collection", "C) A function that yields a sequence of values"],
        "answer": "C",
        "explanation": "Generators are functions that yield a sequence of values using the 'yield' keyword."
    },
    "Q60": {
        "question": "What is the purpose of '__main__' in Python?",
        "options": ["A) Indicates the start of the program", "B) Checks if a script is run directly", "C) Main function declaration"],
        "answer": "B",
        "explanation": "If __name__ == '__main__' is used to check if the script is being run directly or imported."
    },
    "Q61": {
        "question": "How do you create an instance of a class named MyClass?",
        "options": ["A) MyClass()", "B) new MyClass()", "C) create MyClass()"],
        "answer": "A",
        "explanation": "An instance of a class is created by calling the class name followed by parentheses."
    },
    "Q62": {
        "question": "What is the output of 1 == 1.0 in Python?",
        "options": ["A) True", "B) False", "C) TypeError"],
        "answer": "A",
        "explanation": "Python considers 1 (int) and 1.0 (float) equal in value."
    },
    "Q63": {
        "question": "How do you check the type of a variable in Python?",
        "options": ["A) type(variable)", "B) typeof(variable)", "C) varType(variable)"],
        "answer": "A",
        "explanation": "The type() function is used to get the type of a variable."
    },
    "Q64": {
        "question": "What is the correct syntax for defining a class method?",
        "options": ["A) def method(self):", "B) method() -> self:", "C) self.method():"],
        "answer": "A",
        "explanation": "Class methods in Python are defined using 'def' and must include 'self' as the first parameter."
    },
    "Q65": {
        "question": "What does the 'in' operator do when used with strings?",
        "options": ["A) Checks for substring", "B) Checks for character", "C) Both A and B"],
        "answer": "C",
        "explanation": "The 'in' operator checks if a character or substring is present in a string."
    },
    "Q66": {
        "question": "What are *args and **kwargs in function definitions?",
        "options": ["A) Special variables", "B) Ways to pass a variable number of arguments", "C) Error handlers"],
        "answer": "B",
        "explanation": "*args and **kwargs allow you to pass a variable number of arguments to a function."
    },
    "Q67": {
        "question": "What is the purpose of the 'else' clause in a for loop?",
        "options": ["A) To execute code if the loop has an error", "B) To execute code if the loop completes normally", "C) To always execute code after the loop"],
        "answer": "B",
        "explanation": "The 'else' clause in a for loop executes if the loop completes without encountering a 'break' statement."
    },
    "Q68": {
        "question": "What is a shallow copy in Python?",
        "options": ["A) A copy where only the reference is copied", "B) A copy where the entire object is duplicated", "C) A copy where only the first level elements are duplicated"],
        "answer": "C",
        "explanation": "A shallow copy creates a new object but doesn't create copies of nested objects."
    },
    "Q69": {
        "question": "What is the output of bool(0) in Python?",
        "options": ["A) True", "B) False", "C) None"],
        "answer": "B",
        "explanation": "The boolean value of 0 in Python is False."
    },
    "Q70": {
        "question": "How can you iterate over a dictionary in Python?",
        "options": ["A) Using a for loop", "B) Using the .items() method", "C) Both A and B"],
        "answer": "C",
        "explanation": "You can iterate over a dictionary using a for loop and the .items() method."
    },
    "Q71": {
        "question": "What does the 'yield' keyword do?",
        "options": ["A) Pauses function execution and returns a value", "B) Exits the function", "C) Yields error handling to the caller"],
        "answer": "A",
        "explanation": "The 'yield' keyword pauses function execution, returns a value, and resumes from where it left off."
    },
    "Q72": {
        "question": "What is a namespace in Python?",
        "options": ["A) A container for a set of identifiers", "B) A space for naming conventions", "C) A module name"],
        "answer": "A",
        "explanation": "A namespace is a container where names are mapped to objects."
    },
    "Q73": {
        "question": "What does the __name__ variable do?",
        "options": ["A) Stores the name of the module", "B) Stores the name of the function", "C) Both A and B"],
        "answer": "A",
        "explanation": "The __name__ variable in a module stores the name of the module."
    },
    "Q74": {
        "question": "How do you check if a file exists in Python?",
        "options": ["A) os.path.exists(file)", "B) file.exists()", "C) os.exists(file)"],
        "answer": "A",
        "explanation": "The os.path.exists() function is used to check if a file or directory exists."
    },
    "Q75": {
        "question": "What is pickling in Python?",
        "options": ["A) Saving objects to files", "B) Converting objects to a byte stream", "C) Both A and B"],
        "answer": "C",
        "explanation": "Pickling is the process of converting a Python object into a byte stream and optionally saving it to a file."
    },
    "Q76": {
        "question": "What does the 'finally' keyword do in try...except blocks?",
        "options": ["A) Executes final cleanup actions", "B) Handles any uncaught exceptions", "C) Runs as a final conditional check"],
        "answer": "A",
        "explanation": "The 'finally' clause is executed no matter what, often used for cleanup actions."
    },
    "Q77": {
        "question": "How do you define a global variable inside a function?",
        "options": ["A) Using the global keyword", "B) Declaring it outside of any function", "C) Both A and B"],
        "answer": "A",
        "explanation": "To define a global variable inside a function, use the 'global' keyword."
    },
    "Q78": {
        "question": "What is the difference between .py and .pyc files?",
        "options": ["A) .py are source files, .pyc are compiled files", "B) .py are scripts, .pyc are modules", "C) No difference"],
        "answer": "A",
        "explanation": ".py files are Python source files, while .pyc files are compiled Python files."
    },
    "Q79": {
        "question": "What does the os module in Python provide?",
        "options": ["A) Tools for OS-independent filesystem manipulation", "B) Functions to interact with the operating system", "C) Both A and B"],
        "answer": "C",
        "explanation": "The os module provides a way of using operating system dependent functionality and file system manipulation."
    },
    "Q80": {
        "question": "What is an abstract class in Python?",
        "options": ["A) A class that cannot be instantiated", "B) A class with only abstract methods", "C) A template for other classes"],
        "answer": "A",
        "explanation": "An abstract class in Python cannot be instantiated and often contains one or more abstract methods."
    },
    "Q81": {
        "question": "What is the result of 'Hello'.upper() in Python?",
        "options": ["A) 'hello'", "B) 'HELLO'", "C) Error"],
        "answer": "B",
        "explanation": "The .upper() method converts all characters in a string to uppercase."
    },
    "Q82": {
        "question": "What are f-strings in Python?",
        "options": ["A) File strings", "B) Formatted strings", "C) Function strings"],
        "answer": "B",
        "explanation": "F-strings, introduced in Python 3.6, provide a way to embed expressions inside string literals using curly braces."
    },
    "Q83": {
        "question": "What is the purpose of __str__ method in a class?",
        "options": ["A) For string representation of an instance", "B) For string conversion", "C) For memory allocation"],
        "answer": "A",
        "explanation": "The __str__ method returns a human-readable string representation of an object."
    },
    "Q84": {
        "question": "What does the os.walk() function do?",
        "options": ["A) Walks through a directory tree", "B) Calculates file size", "C) Renames files"],
        "answer": "A",
        "explanation": "The os.walk() function generates the file names in a directory tree by walking the tree either top-down or bottom-up."
    },
    "Q85": {
        "question": "How do you check for the presence of a key in a dictionary?",
        "options": ["A) 'key' in dict", "B) dict.has_key('key')", "C) dict.contains('key')"],
        "answer": "A",
        "explanation": "The 'in' keyword is used to check if a key exists in a dictionary."
    },
    "Q86": {
        "question": "What is the difference between lists and tuples in Python?",
        "options": ["A) Lists are immutable, tuples are mutable", "B) Lists are mutable, tuples are immutable", "C) No difference"],
        "answer": "B",
        "explanation": "Lists are mutable (can be changed), whereas tuples are immutable (cannot be changed)."
    },
    "Q87": {
        "question": "What does the 'import this' statement do in Python?",
        "options": ["A) Imports a module named 'this'", "B) Throws an error", "C) Displays the Zen of Python"],
        "answer": "C",
        "explanation": "'import this' displays the Zen of Python, a collection of principles for writing computer programs in Python."
    },
    "Q88": {
        "question": "How do you measure the execution time of a Python code snippet?",
        "options": ["A) Using timeit module", "B) Using timer function", "C) Using stopwatch"],
        "answer": "A",
        "explanation": "The timeit module provides a simple way to time small bits of Python code."
    },
    "Q89": {
        "question": "What is the use of the __call__ method?",
        "options": ["A) To call methods", "B) To make an object callable", "C) To call the constructor"],
        "answer": "B",
        "explanation": "The __call__ method enables Python programmers to write classes where the instances behave like functions and can be called like a function."
    },
    "Q90": {
        "question": "How do you check if a string contains only digits?",
        "options": ["A) .isdigit()", "B) .isnumeric()", "C) .containsDigits()"],
        "answer": "A",
        "explanation": "The .isdigit() method returns True if the string contains only digits."
    },
    "Q91": {
        "question": "What is slicing in Python?",
        "options": ["A) A method to replace elements in a list", "B) A way to select specific elements of a sequence", "C) A technique for sorting sequences"],
        "answer": "B",
        "explanation": "Slicing is used to select specific ranges of elements from a sequence like a list, tuple, or string."
    },
    "Q92": {
        "question": "How do you create a byte array in Python?",
        "options": ["A) bytearray()", "B) bytes()", "C) byte[]"],
        "answer": "A",
        "explanation": "The bytearray() function returns a byte array, which is a mutable sequence of integers in the range 0 <= x < 256."
    },
    "Q93": {
        "question": "What is the difference between shallow copy and deep copy?",
        "options": ["A) Shallow copy copies references, deep copy copies values", "B) Shallow copy copies values, deep copy copies references", "C) No difference"],
        "answer": "A",
        "explanation": "A shallow copy creates a new object but doesn't create copies of nested objects, whereas a deep copy creates copies of nested objects."
    },
    "Q94": {
        "question": "What does the 'yield from' statement do in Python?",
        "options": ["A) Pauses the function", "B) Returns from a function", "C) Delegates to a subgenerator"],
        "answer": "C",
        "explanation": "The 'yield from' statement is used for subgenerator delegation, a feature introduced in Python 3.3."
    },
    "Q95": {
        "question": "What is a context manager in Python?",
        "options": ["A) A tool for managing imports", "B) An object that manages a runtime context", "C) A module manager"],
        "answer": "B",
        "explanation": "A context manager in Python is a type of construct that manages the allocation and release of resources."
    },
    "Q96": {
        "question": "What is the use of the @staticmethod decorator?",
        "options": ["A) To create a static class", "B) To create a static method that does not receive an implicit first argument", "C) To declare a constant method"],
        "answer": "B",
        "explanation": "The @staticmethod decorator is used to declare a static method in a class that doesn't receive an implicit first argument."
    },
    "Q97": {
        "question": "How do you convert a string to lowercase in Python?",
        "options": ["A) .lower()", "B) .toLowerCase()", "C) .toLower()"],
        "answer": "A",
        "explanation": "The .lower() method converts all characters in a string to lowercase."
    },
    "Q98": {
        "question": "What is a namespace in Python?",
        "options": ["A) A space that stores names", "B) A built-in Python library", "C) A Python IDE"],
        "answer": "A",
        "explanation": "A namespace in Python is a container where names are mapped to objects, and it varies with the scope of names."
    },
    "Q99": {
        "question": "How do you iterate over a dictionary in Python?",
        "options": ["A) Using a for loop", "B) Using the .items() method", "C) Both A and B"],
        "answer": "C",
        "explanation": "You can iterate over a dictionary using a for loop along with the .items() method to access key-value pairs."
    },
    "Q100": {
        "question": "What is the output of round(3.14159, 2)?",
        "options": ["A) 3", "B) 3.14", "C) 3.1"],
        "answer": "B",
        "explanation": "The round() function rounds a number to a specified number of decimal places, so round(3.14159, 2) is 3.14."
    },
    "Q101": {
        "question": "What is the difference between a static method and a class method?",
        "options": ["A) No difference", "B) Static method doesn't have access to cls or self", "C) Class method can modify class state"],
        "answer": "B",
        "explanation": "Static methods don't have access to the cls (class) or self (instance) arguments, unlike class methods which can access cls."
    },
    "Q102": {
        "question": "How do you find the absolute value of a number in Python?",
        "options": ["A) abs()", "B) absolute()", "C) fabs()"],
        "answer": "A",
        "explanation": "The abs() function returns the absolute value of a number."
    },
    "Q103": {
        "question": "What is the output of bool(None)?",
        "options": ["A) True", "B) False", "C) None"],
        "answer": "B",
        "explanation": "The bool() function converts values to Boolean using the standard truth testing procedure, where None is False."
    },
    "Q104": {
        "question": "What does the .extend() method do in lists?",
        "options": ["A) Extends the list by appending all items from the iterable", "B) Adds a single element to the list", "C) Extends the list's size without adding elements"],
        "answer": "A",
        "explanation": "The .extend() method extends the list by appending all items from the provided iterable."
    },
    "Q105": {
        "question": "What is a decorator in Python?",
        "options": ["A) A variable", "B) A function that takes another function and extends its functionality", "C) A type of Python loop"],
        "answer": "B",
        "explanation": "A decorator in Python is a function that takes another function as an argument and extends its functionality without explicitly modifying it."
    },
    "Q106": {
        "question": "How do you create an infinite loop in Python?",
        "options": ["A) for i in infinity:", "B) while True:", "C) loop:"],
        "answer": "B",
        "explanation": "An infinite loop can be created with 'while True:', which continuously executes the block as long as the condition is true."
    },
    "Q107": {
        "question": "What is the purpose of the __name__ variable in Python?",
        "options": ["A) Stores the name of the module", "B) Indicates whether a module is being run as a script or imported", "C) Holds the function name"],
        "answer": "B",
        "explanation": "The __name__ variable indicates whether a module is being run as the main program or being imported into another module."
    },
    "Q108": {
        "question": "What is pickling in Python?",
        "options": ["A) A method of preserving code", "B) A technique for function optimization", "C) The process of converting a Python object into a byte stream"],
        "answer": "C",
        "explanation": "Pickling is the process of converting a Python object into a byte stream, typically for saving to a file or database."
    },
    "Q109": {
        "question": "What are *args and **kwargs in Python?",
        "options": ["A) Operators", "B) Special variables for variable-length arguments", "C) Error handling mechanisms"],
        "answer": "B",
        "explanation": "*args and **kwargs are used in function definitions to handle variable numbers of arguments: *args for non-keyword arguments, **kwargs for keyword arguments."
    },
    "Q110": {
        "question": "What is the purpose of the __init__ method in Python classes?",
        "options": ["A) Initializes a new instance of the class", "B) Used for memory allocation", "C) Indicates the start of class definition"],
        "answer": "A",
        "explanation": "The __init__ method is called automatically whenever a new instance of the class is created, initializing the instance."
    },
    "Q111": {
        "question": "How do you declare a variable as private in a Python class?",
        "options": ["A) Using the private keyword", "B) By prefixing the variable with an underscore", "C) Private variables are not supported"],
        "answer": "B",
        "explanation": "In Python, private variables are conventionally indicated by prefixing the name with an underscore."
    },
    "Q112": {
        "question": "What does the 'finally' block do in try-except?",
        "options": ["A) Executes as the last statement", "B) Runs only if an exception occurs", "C) Always executes, regardless of exceptions"],
        "answer": "C",
        "explanation": "The 'finally' block always executes, regardless of whether an exception occurred in the try block or not."
    },
    "Q113": {
        "question": "What is the output of '2 + 2 == 4 and not 2 == 5'?",
        "options": ["A) True", "B) False", "C) SyntaxError"],
        "answer": "A",
        "explanation": "The expression evaluates to True as both '2 + 2 == 4' and 'not 2 == 5' are True."
    },
    "Q114": {
        "question": "How do you check the type of an object in Python?",
        "options": ["A) type()", "B) typeof()", "C) checkType()"],
        "answer": "A",
        "explanation": "The type() function is used to determine the type of an object."
    },
    "Q115": {
        "question": "What are the different types of operators in Python?",
        "options": ["A) Arithmetic, Comparison, Assignment", "B) Logical, Functional, Relational", "C) Numeric, String, Boolean"],
        "answer": "A",
        "explanation": "Python has various operators including Arithmetic, Comparison, Assignment, Logical, Bitwise, Membership, and Identity operators."
    },
    "Q116": {
        "question": "What is a module in Python?",
        "options": ["A) A single Python file", "B) A collection of Python files", "C) A function in Python"],
        "answer": "A",
        "explanation": "A module in Python is a file containing Python definitions and statements. The file name is the module name with the suffix .py."
    },
    "Q117": {
        "question": "How can you create a multi-line string in Python?",
        "options": ["A) Using triple quotes", "B) Adding \\n at the end of each line", "C) Enclosing in square brackets"],
        "answer": "A",
        "explanation": "Multi-line strings in Python can be created by enclosing text in triple quotes (either ''' or \")."
    },
    "Q118": {
        "question": "What does the 'in' keyword check in Python?",
        "options": ["A) If an item is present in a sequence", "B) If a loop is inside another loop", "C) If a number is within a range"],
        "answer": "A",
        "explanation": "The 'in' keyword checks if an item is present in a sequence like a list, string, or tuple."
    },
    "Q119": {
        "question": "What is a key feature of Python's philosophy?",
        "options": ["A) Readability matters", "B) Speed is key", "C) Complexity is better than simplicity"],
        "answer": "A",
        "explanation": "Python emphasizes readability and simplicity, following the principle that 'Readability counts.'"
    },
    "Q120": {
        "question": "What is the output of 'not False or True'?",
        "options": ["A) True", "B) False", "C) None"],
        "answer": "A",
        "explanation": "The expression evaluates to True because 'not False' is True and 'True or anything' is always True."
    },
    "Q121": {
        "question": "What does 'list(range(3, 8))' return?",
        "options": ["A) [3, 4, 5, 6, 7, 8]", "B) [3, 4, 5, 6, 7]", "C) [3, 4, 5]"],
        "answer": "B",
        "explanation": "'range(3, 8)' generates numbers from 3 up to but not including 8."
    },
    "Q122": {
        "question": "How do you check if 'a' is not equal to 'b' in Python?",
        "options": ["A) a != b", "B) a <> b", "C) a == !b"],
        "answer": "A",
        "explanation": "The '!=' operator checks if two values are not equal in Python."
    },
    "Q123": {
        "question": "What is a correct syntax to output the type of a variable or object in Python?",
        "options": ["A) print(type(var))", "B) print(var.type())", "C) print(typeof(var))"],
        "answer": "A",
        "explanation": "The 'type()' function is used to get the type of a variable or an object in Python."
    },
    "Q124": {
        "question": "Which method converts a string to a float in Python?",
        "options": ["A) float()", "B) strToFloat()", "C) parse()"],
        "answer": "A",
        "explanation": "The 'float()' function converts a string to a floating-point number."
    },
    "Q125": {
        "question": "What is the correct way to create a set which includes elements 1, 3, and 5?",
        "options": ["A) {1, 3, 5}", "B) [1, 3, 5]", "C) (1, 3, 5)"],
        "answer": "A",
        "explanation": "Sets are created using curly braces with elements separated by commas."
    },
    "Q126": {
        "question": "What does the expression '5 // 2' return in Python?",
        "options": ["A) 2.5", "B) 2", "C) 3"],
        "answer": "B",
        "explanation": "'//' is the floor division operator, dividing and rounding down to the nearest integer."
    },
    "Q127": {
        "question": "What is the output of 'not True'?",
        "options": ["A) True", "B) False", "C) SyntaxError"],
        "answer": "B",
        "explanation": "The 'not' keyword is a logical operator used to reverse the truth value, so 'not True' is False."
    },
    "Q128": {
        "question": "Which of these data types is immutable?",
        "options": ["A) List", "B) Dictionary", "C) String"],
        "answer": "C",
        "explanation": "Strings in Python are immutable, meaning they cannot be changed after they are created."
    },
    "Q129": {
        "question": "What is the result of '2 ** 3' in Python?",
        "options": ["A) 6", "B) 8", "C) 9"],
        "answer": "B",
        "explanation": "'**' is the exponentiation operator, so '2 ** 3' is 2 raised to the power of 3, which is 8."
    },
    "Q130": {
        "question": "How do you check for the presence of an element in a list?",
        "options": ["A) 'element' in list", "B) list.contains('element')", "C) list.find('element')"],
        "answer": "A",
        "explanation": "The 'in' keyword checks for the presence of an element in a list."
    },
    "Q131": {
        "question": "What does the 'elif' keyword mean in Python?",
        "options": ["A) Else", "B) Else if", "C) Else iterate"],
        "answer": "B",
        "explanation": "'elif' is a contraction of 'else if', used for additional conditions in an if-else chain."
    },
    "Q132": {
        "question": "How do you remove the last item from a list?",
        "options": ["A) list.pop()", "B) list.removeLast()", "C) del list[-1]"],
        "answer": "A",
        "explanation": "The 'pop()' method removes and returns the last item from a list."
    },
    "Q133": {
        "question": "What is the output of 'bool([])'?",
        "options": ["A) True", "B) False", "C) None"],
        "answer": "B",
        "explanation": "An empty list is considered False in Python when converted to a boolean."
    },
    "Q134": {
        "question": "What is the purpose of the 'return' statement in a function?",
        "options": ["A) To exit the function", "B) To return a value from the function", "C) To print a value"],
        "answer": "B",
        "explanation": "The 'return' statement is used in a function to return a value back to the caller."
    },
    "Q135": {
        "question": "What does 'len('hello')' return?",
        "options": ["A) 4", "B) 5", "C) Error"],
        "answer": "B",
        "explanation": "The 'len()' function returns the length of the string, so 'len('hello')' returns 5."
    },
    "Q136": {
        "question": "What is the correct way to declare a variable in Python?",
        "options": ["A) var x = 10", "B) x = 10", "C) int x = 10"],
        "answer": "B",
        "explanation": "In Python, variables are declared by assigning a value to them, like 'x = 10'."
    },
    "Q137": {
        "question": "How do you import a specific function from a module?",
        "options": ["A) from module import function", "B) import function from module", "C) include function from module"],
        "answer": "A",
        "explanation": "Use 'from module import function' to import a specific function from a module."
    },
    "Q138": {
        "question": "What does the 'pass' statement do in Python?",
        "options": ["A) Passes control to the next line", "B) Does nothing at all", "C) Passes a variable to a function"],
        "answer": "B",
        "explanation": "The 'pass' statement is a null operation; it does nothing when executed."
    },
    "Q139": {
        "question": "What is an attribute in Python?",
        "options": ["A) A function inside a class", "B) A variable inside a class", "C) A module"],
        "answer": "B",
        "explanation": "An attribute in Python refers to a variable inside a class."
    },
    "Q140": {
        "question": "What will 'print(2 * 3 + 4)' output?",
        "options": ["A) 14", "B) 10", "C) 8"],
        "answer": "B",
        "explanation": "The expression will be evaluated as '2 * 3' first and then '4' added, giving 10."
    },
    "Q141": {
        "question": "What does the 'split()' method do to a string?",
        "options": ["A) Divides it into a list of characters", "B) Splits it into a list based on a delimiter", "C) Cuts off the end of the string"],
        "answer": "B",
        "explanation": "The 'split()' method divides a string into a list by separating it at each instance of a specified delimiter."
    },
    "Q142": {
        "question": "How do you represent an integer in binary format?",
        "options": ["A) bin(integer)", "B) int(integer, 2)", "C) binary(integer)"],
        "answer": "A",
        "explanation": "The 'bin()' function converts an integer to its binary representation as a string."
    },
    "Q143": {
        "question": "What is the correct syntax for defining a generator function in Python?",
        "options": ["A) def gen(): yield", "B) generator gen():", "C) def gen(): return"],
        "answer": "A",
        "explanation": "A generator function is defined like a normal function but uses the 'yield' statement instead of 'return'."
    },
    "Q144": {
        "question": "What is the purpose of the '__del__' method in Python?",
        "options": ["A) To delete an object from memory", "B) To define a destructor method", "C) To remove a variable"],
        "answer": "B",
        "explanation": "The '__del__' method in Python is a destructor and is called when an object is about to be destroyed."
    },
    "Q145": {
        "question": "What does 'list(set(myList))' do?",
        "options": ["A) Sorts myList", "B) Removes duplicates from myList", "C) Reverses myList"],
        "answer": "B",
        "explanation": "Converting a list to a set removes duplicates, and converting it back to a list maintains this property."
    },
    "Q146": {
        "question": "What is recursion in programming?",
        "options": ["A) When a function calls another function", "B) When a function calls itself", "C) A type of loop"],
        "answer": "B",
        "explanation": "Recursion is a technique where a function calls itself in its definition."
    },
    "Q147": {
        "question": "How is memory management handled in Python?",
        "options": ["A) Using manual allocation and deallocation", "B) Through the Garbage Collector", "C) Using reference counters"],
        "answer": "B",
        "explanation": "Python uses a garbage collector for automatic memory management."
    },
    "Q148": {
        "question": "What is slicing in Python?",
        "options": ["A) Removing an element from a sequence", "B) A method to iterate over a sequence", "C) Selecting a range of items from a sequence"],
        "answer": "C",
        "explanation": "Slicing in Python allows you to create a new sequence containing a subset of elements from an existing sequence."
    },
    "Q149": {
        "question": "What does 'dict.items()' do?",
        "options": ["A) Returns a list of keys in the dictionary", "B) Returns a list of values", "C) Returns a view of key-value pairs"],
        "answer": "C",
        "explanation": "'dict.items()' returns a view object displaying a list of a dictionary's key-value tuple pairs."
    },
    "Q150": {
        "question": "How can you catch multiple exceptions in a single block?",
        "options": ["A) Using multiple except blocks", "B) By separating the exceptions with a comma in an except block", "C) You can't catch multiple exceptions"],
        "answer": "B",
        "explanation": "You can catch multiple exceptions in a single except block by separating them with a comma."
    },
    "Q151": {
        "question": "What does 'import *' do?",
        "options": ["A) Imports all functions from a module", "B) Imports only the specified function", "C) Imports the entire module"],
        "answer": "A",
        "explanation": "'import *' imports all public names defined in a module."
    },
    "Q152": {
        "question": "How do you create a class inheritance in Python?",
        "options": ["A) class Subclass(Baseclass):", "B) class Subclass -> Baseclass:", "C) class Subclass inherits Baseclass:"],
        "answer": "A",
        "explanation": "In Python, class inheritance is created by passing the parent class as a parameter to the definition of the child class."
    },
    "Q153": {
        "question": "What is the difference between 'append()' and 'extend()' methods in lists?",
        "options": ["A) 'append()' adds an element, 'extend()' adds many elements", "B) 'append()' adds many elements, 'extend()' adds an element", "C) No difference"],
        "answer": "A",
        "explanation": "'append()' adds a single element to the end of a list, while 'extend()' can add multiple elements."
    },
    "Q154": {
        "question": "What does the 'break' statement do in a loop?",
        "options": ["A) Pauses the loop", "B) Exits the loop", "C) Skips the current iteration"],
        "answer": "B",
        "explanation": "The 'break' statement is used to exit the loop prematurely."
    },
    "Q155": {
        "question": "What is output of 'print(1, 2, 3, sep=':')'?",
        "options": ["A) 123", "B) 1:2:3", "C) 1 2 3"],
        "answer": "B",
        "explanation": "The 'sep' parameter in the print function determines the separator between the values, so it will print '1:2:3'."
    },
    "Q156": {
        "question": "How do you create a static method in a class?",
        "options": ["A) Using the @staticmethod decorator", "B) By declaring it outside the class", "C) Static methods cannot be created in Python"],
        "answer": "A",
        "explanation": "Static methods in Python are created using the '@staticmethod' decorator."
    },
    "Q157": {
        "question": "What is a lambda function in Python?",
        "options": ["A) A named function", "B) A type of exception", "C) An anonymous function"],
        "answer": "C",
        "explanation": "A lambda function in Python is an anonymous function defined with the lambda keyword."
    },
    "Q158": {
        "question": "What does 'enumerate()' do?",
        "options": ["A) Enumerates the keys in a dictionary", "B) Adds a counter to an iterable and returns it", "C) Creates a numbered list"],
        "answer": "B",
        "explanation": "'enumerate()' adds a counter to each item in an iterable and returns it, typically used in for loops."
    },
    "Q159": {
        "question": "What does 'set()' do?",
        "options": ["A) Creates an immutable set", "B) Sorts a sequence", "C) Creates a set which is a collection of unique elements"],
        "answer": "C",
        "explanation": "'set()' creates a set in Python, which is a collection of unique elements."
    },
    "Q160": {
        "question": "How do you execute a Python script from the command line?",
        "options": ["A) python script.py", "B) run script.py", "C) execute script.py"],
        "answer": "A",
        "explanation": "A Python script is executed from the command line using 'python script.py'."
    },
    "Q161": {
        "question": "How do you represent a hexadecimal number in Python?",
        "options": ["A) 0xHexValue", "B) hex(HexValue)", "C) #HexValue"],
        "answer": "A",
        "explanation": "Hexadecimal numbers in Python are represented by prefixing with '0x'."
    },
    "Q162": {
        "question": "What is the use of the '__repr__' method in Python?",
        "options": ["A) For debugging, official string representation of an object", "B) For user-friendly string representation", "C) To represent an object as a string"],
        "answer": "A",
        "explanation": "The '__repr__' method provides the official string representation of an object, often used for debugging."
    },
    "Q163": {
        "question": "What is a metaclass in Python?",
        "options": ["A) A class of a class", "B) A special method in a class", "C) A library for metadata"],
        "answer": "A",
        "explanation": "A metaclass in Python is a class of a class that defines how a class behaves."
    },
    "Q164": {
        "question": "What is the difference between '.py' files and '.pyw' files?",
        "options": ["A) No difference", "B) .pyw files are used for web development", "C) .pyw files do not open a console window when run"],
        "answer": "C",
        "explanation": "'.pyw' files are Python files that, when run, do not open a console window."
    },
    "Q165": {
        "question": "What is monkey patching in Python?",
        "options": ["A) Changing code at runtime", "B) Fixing a bug at runtime", "C) Dynamic modification of a class or module"],
        "answer": "C",
        "explanation": "Monkey patching is the dynamic modification of a class or module during runtime."
    },
    "Q166": {
        "question": "What is the purpose of the 'with' statement in Python?",
        "options": ["A) To ensure proper resource management", "B) For error handling", "C) To create a new scope"],
        "answer": "A",
        "explanation": "The 'with' statement in Python is used for resource management, ensuring that resources like files are properly cleaned up after use."
    },
    "Q167": {
        "question": "What does the 'globals()' function do in Python?",
        "options": ["A) Returns a list of all global variables", "B) Defines a global variable", "C) Returns a dictionary of the current global symbol table"],
        "answer": "C",
        "explanation": "'globals()' returns a dictionary representing the current global symbol table in Python."
    },
    "Q168": {
        "question": "What is the output of 'print(chr(65))' in Python?",
        "options": ["A) A", "B) 65", "C) Error"],
        "answer": "A",
        "explanation": "'chr()' function returns the string representing a character whose Unicode code point is the integer passed. 'chr(65)' returns 'A'."
    },
    "Q169": {
        "question": "How do you create a virtual environment named 'env' using venv in Python?",
        "options": ["A) python -m venv env", "B) venv -m python env", "C) virtualenv env"],
        "answer": "A",
        "explanation": "To create a virtual environment named 'env' using venv, the command is 'python -m venv env'."
    },
    "Q170": {
        "question": "What is the purpose of the '__doc__' attribute?",
        "options": ["A) To document a Python script", "B) To provide a documentation string for an object", "C) To document errors in code"],
        "answer": "B",
        "explanation": "The '__doc__' attribute contains the documentation string for an object, which is the first unassigned string in the object."
    },
    "Q171": {
        "question": "How can you merge two dictionaries in Python?",
        "options": ["A) Using the update() method", "B) By adding them", "C) Using the merge() method"],
        "answer": "A",
        "explanation": "The update() method merges the keys and values of one dictionary into another."
    },
    "Q172": {
        "question": "What is the output of 'bool([])' in Python?",
        "options": ["A) True", "B) False", "C) None"],
        "answer": "B",
        "explanation": "An empty list is considered False in Python when converted to a boolean."
    },
    "Q173": {
        "question": "How do you format a string in Python 3?",
        "options": ["A) Using the format() method", "B) With string concatenation", "C) Using printf-style formatting"],
        "answer": "A",
        "explanation": "In Python 3, strings can be formatted using the format() method, which is more versatile and easier to read than printf-style formatting."
    },
    "Q174": {
        "question": "What does the 'ord()' function do in Python?",
        "options": ["A) Converts a character to its ASCII value", "B) Orders characters alphabetically", "C) Finds the ordinal value of a number"],
        "answer": "A",
        "explanation": "'ord()' function converts a character into its Unicode code point/ASCII value."
    },
    "Q175": {
        "question": "What is the use of the '__slots__' attribute in Python classes?",
        "options": ["A) For memory optimization of class instances", "B) To reserve slots for future attributes", "C) To lock attribute assignment"],
        "answer": "A",
        "explanation": "'__slots__' is used to declare fixed attributes for a class, which can optimize memory usage for class instances."
    },
    "Q176": {
        "question": "How do you round a number to 2 decimal places in Python?",
        "options": ["A) round(number, 2)", "B) number.round(2)", "C) round(2, number)"],
        "answer": "A",
        "explanation": "The round() function rounds a number to a specified number of decimal places, so 'round(number, 2)' rounds to 2 decimal places."
    },
    "Q177": {
        "question": "What is the difference between the '==' operator and the 'is' operator?",
        "options": ["A) '==' compares values, 'is' compares identities", "B) '==' compares types, 'is' compares values", "C) No difference"],
        "answer": "A",
        "explanation": "'==' checks if the values of two objects are equal, whereas 'is' checks if they are the exact same object (identity)."
    },
    "Q178": {
        "question": "What does the 'locals()' function do in Python?",
        "options": ["A) Returns a list of all local variables", "B) Creates local variables dynamically", "C) Returns a dictionary of the current local symbol table"],
        "answer": "C",
        "explanation": "'locals()' returns a dictionary representing the current local symbol table, which holds information about all local variables."
    },
    "Q179": {
        "question": "What is the purpose of the '@property' decorator in Python?",
        "options": ["A) To define a class property", "B) To make an attribute read-only", "C) To define getters and setters for a class attribute"],
        "answer": "C",
        "explanation": "The '@property' decorator is used to define getters and setters for a class attribute, allowing encapsulation."
    },
    "Q180": {
        "question": "What is the output of 'print(0b101)' in Python?",
        "options": ["A) 101", "B) 5", "C) 0b101"],
        "answer": "B",
        "explanation": "'0b101' is a binary representation, and when printed, it will output its decimal equivalent, which is 5."
    },
    "Q181": {
        "question": "How do you check if a variable is an instance of a specific class or its subclass?",
        "options": ["A) isinstance(variable, class)", "B) type(variable) == class", "C) variable.instance(class)"],
        "answer": "A",
        "explanation": "'isinstance()' checks if a variable is an instance of a class or a subclass thereof."
    },
    "Q182": {
        "question": "What is a generator in Python?",
        "options": ["A) A type of collection", "B) A function that returns an iterable sequence", "C) A tool to generate random numbers"],
        "answer": "B",
        "explanation": "A generator is a function that returns an iterable sequence of values, yielding one value at a time."
    },
    "Q183": {
        "question": "What are anonymous functions in Python?",
        "options": ["A) Named functions", "B) Functions without a return statement", "C) Functions without a name"],
        "answer": "C",
        "explanation": "Anonymous functions, also known as lambda functions, are functions defined without a name."
    },
    "Q184": {
        "question": "What does the 'continue' keyword do in a loop?",
        "options": ["A) Exits the loop", "B) Pauses the loop", "C) Skips to the next iteration of the loop"],
        "answer": "C",
        "explanation": "The 'continue' keyword in a loop skips the current iteration and proceeds to the next iteration."
    },
    "Q185": {
        "question": "How do you declare a variable in a Python class shared by all instances?",
        "options": ["A) Instance variable", "B) Class variable", "C) Global variable"],
        "answer": "B",
        "explanation": "Class variables in Python are shared by all instances of the class."
    },
    "Q186": {
        "question": "What is the difference between a shallow copy and a deep copy of a list in Python?",
        "options": ["A) Shallow copy copies only the top level, deep copy copies everything", "B) No difference", "C) Shallow copy copies everything, deep copy copies only the top level"],
        "answer": "A",
        "explanation": "A shallow copy copies only the top-level elements of a list, while a deep copy copies all nested elements."
    },
    "Q187": {
        "question": "What is the output of 'print(type(lambda x: x))' in Python?",
        "options": ["A) <class 'function'>", "B) <class 'lambda'>", "C) <class 'method'>"],
        "answer": "A",
        "explanation": "Lambda functions in Python are of the type 'function'."
    },
    "Q188": {
        "question": "How do you create an alias for a module in Python?",
        "options": ["A) import module as alias", "B) alias = import module", "C) import module alias"],
        "answer": "A",
        "explanation": "The syntax 'import module as alias' creates an alias for a module."
    },
    "Q189": {
        "question": "What is the correct way to declare a multiline string in Python?",
        "options": ["A) Using triple single quotes", "B) Enclosing in square brackets", "C) Using triple double quotes"],
        "answer": "C",
        "explanation": "Multiline strings in Python can be declared using triple double quotes."
    },
    "Q190": {
        "question": "What does the 'isinstance()' function do?",
        "options": ["A) Checks if two objects are identical", "B) Determines if an object is an instance of a specific class", "C) Compares the value of two objects"],
        "answer": "B",
        "explanation": "'isinstance()' checks if an object is an instance of a specific class or a subclass thereof."
    },
    "Q191": {
        "question": "What is the purpose of a docstring in Python?",
        "options": ["A) To speed up code execution", "B) To write documentation for a function or class", "C) To declare variables"],
        "answer": "B",
        "explanation": "Docstrings in Python are used to write documentation for functions, classes, and modules."
    },
    "Q192": {
        "question": "How do you check if a list is empty in Python?",
        "options": ["A) len(list) == 0", "B) list.isEmpty()", "C) list == []"],
        "answer": "A",
        "explanation": "You can check if a list is empty by checking if its length is zero with 'len(list) == 0'."
    },
    "Q193": {
        "question": "What is the difference between 'append()' and 'extend()' in Python lists?",
        "options": ["A) 'append()' adds a single element, 'extend()' adds multiple elements", "B) 'append()' adds multiple elements, 'extend()' adds a single element", "C) No difference"],
        "answer": "A",
        "explanation": "'append()' adds a single element to the end of a list, while 'extend()' adds each element of an iterable to the list."
    },
    "Q194": {
        "question": "What does the 'del' statement do in Python?",
        "options": ["A) Deletes a variable or part of a list", "B) Deletes a file", "C) Declares a variable"],
        "answer": "A",
        "explanation": "The 'del' statement is used to delete objects in Python, like variables or list elements."
    },
    "Q195": {
        "question": "How do you square a number in Python?",
        "options": ["A) number ** 2", "B) number ^ 2", "C) square(number)"],
        "answer": "A",
        "explanation": "In Python, '**' is the exponentiation operator, so 'number ** 2' squares a number."
    },
    "Q196": {
        "question": "What is the purpose of the 'else' clause in Python loops?",
        "options": ["A) Runs if no break occurs in the loop", "B) Always runs after the loop", "C) Error handling"],
        "answer": "A",
        "explanation": "The 'else' clause in a loop runs only if no 'break' occurs in the loop."
    },
    "Q197": {
        "question": "What is the default return value of a Python function?",
        "options": ["A) 0", "B) False", "C) None"],
        "answer": "C",
        "explanation": "If no return statement is specified in a Python function, it returns 'None' by default."
    },
    "Q198": {
        "question": "How do you create an empty set in Python?",
        "options": ["A) {}", "B) set()", "C) []"],
        "answer": "B",
        "explanation": "An empty set is created using 'set()', as '{}' creates an empty dictionary."
    },
    "Q199": {
        "question": "What does the 'range(3, 10, 2)' function return?",
        "options": ["A) A list of numbers from 3 to 10, stepping by 2", "B) An error", "C) A range object representing numbers from 3 to 10, stepping by 2"],
        "answer": "C",
        "explanation": "'range(3, 10, 2)' returns a range object that generates numbers from 3 to 10 with a step of 2."
    },
    "Q200": {
        "question": "What is the purpose of the 'pass' statement in Python?",
        "options": ["A) To pass control to another part of the program", "B) To represent an empty block of code", "C) To exit a loop or function"],
        "answer": "B",
        "explanation": "The 'pass' statement is a null operation used to represent an empty block of code where syntactically some code is expected."
    },
    "Q201": {
        "question": "How do you convert a string to uppercase in Python?",
        "options": ["A) .toUpperCase()", "B) .upper()", "C) .capitalize()"],
        "answer": "B",
        "explanation": "The '.upper()' method converts all characters in a string to uppercase."
    },
    "Q202": {
        "question": "What is the output of 'bool(1)' in Python?",
        "options": ["A) True", "B) False", "C) 1"],
        "answer": "A",
        "explanation": "In Python, non-zero numbers are considered True when converted to a boolean, so 'bool(1)' is True."
    },
    "Q203": {
        "question": "What is the purpose of the '__iter__' method in Python?",
        "options": ["A) To iterate over a sequence", "B) To check for iteration compatibility", "C) To make an object iterable"],
        "answer": "C",
        "explanation": "The '__iter__' method is used to make an object iterable, allowing it to be used in loops and other iterable contexts."
    },
    "Q204": {
        "question": "How do you create a generator expression in Python?",
        "options": ["A) Using parentheses", "B) Using curly braces", "C) Using square brackets"],
        "answer": "A",
        "explanation": "Generator expressions are created using parentheses and are similar to list comprehensions but more memory efficient."
    },
    "Q205": {
        "question": "What is the difference between a method and a function in Python?",
        "options": ["A) No difference", "B) Methods are part of classes, functions are not", "C) Functions are called by objects"],
        "answer": "B",
        "explanation": "In Python, a method is a function that is associated with an object or class, while a function is independent of any object."
    },
    "Q206": {
        "question": "What does the 'super()' function do in Python?",
        "options": ["A) Returns the superclass of a class", "B) Calls a method from the parent class", "C) Checks for class superiority"],
        "answer": "B",
        "explanation": "The 'super()' function in Python is used to call methods from a parent class within a subclass."
    },
    "Q207": {
        "question": "What is the output of 'print(list(filter(lambda x: x % 2 == 0, [1,2,3,4])))'?",
        "options": ["A) [1, 3]", "B) [2, 4]", "C) [1, 2, 3, 4]"],
        "answer": "B",
        "explanation": "The 'filter' function applies a lambda function to filter out elements, in this case, returning only even numbers [2, 4]."
    },
    "Q208": {
        "question": "How do you swap two variables in Python?",
        "options": ["A) Using a temporary variable", "B) a, b = b, a", "C) swap(a, b)"],
        "answer": "B",
        "explanation": "In Python, you can swap two variables easily with the syntax 'a, b = b, a'."
    },
    "Q209": {
        "question": "What does the 'is' operator check in Python?",
        "options": ["A) If two variables have the same value", "B) If two variables are the same object", "C) If two variables are of the same type"],
        "answer": "B",
        "explanation": "The 'is' operator in Python checks if two variables point to the same object in memory."
    },
    "Q210": {
        "question": "What are dictionary comprehensions in Python?",
        "options": ["A) A way to iterate over dictionaries", "B) A method to create dictionaries", "C) A technique to merge two dictionaries"],
        "answer": "B",
        "explanation": "Dictionary comprehensions in Python provide a concise way to create dictionaries from iterables."
    },
    "Q211": {
        "question": "What is the output of 'print(3 * 'ab' + 'cd')'?",
        "options": ["A) 'abababcd'", "B) 'ababcdcd'", "C) 'ababcd'"],
        "answer": "A",
        "explanation": "This expression concatenates 'ab' three times with 'cd', resulting in 'abababcd'."
    },
    "Q212": {
        "question": "How do you read a file line by line in Python?",
        "options": ["A) Using a while loop", "B) Using the readlines() method", "C) With a for loop"],
        "answer": "C",
        "explanation": "Reading a file line by line in Python is commonly done with a for loop, iterating over the file object."
    },
    "Q213": {
        "question": "What is the purpose of the '__str__' method in Python?",
        "options": ["A) To convert an object to a string", "B) To print an object", "C) To compare two objects"],
        "answer": "A",
        "explanation": "The '__str__' method is used to define a human-readable string representation of an object."
    },
    "Q214": {
        "question": "What does the 'sorted()' function do in Python?",
        "options": ["A) Sorts a list in place", "B) Returns a new list that is sorted", "C) Checks if a list is sorted"],
        "answer": "B",
        "explanation": "The 'sorted()' function returns a new sorted list from the elements of any iterable, without modifying the original."
    },
    "Q215": {
        "question": "How do you create a multiline comment in Python?",
        "options": ["A) Using triple single quotes", "B) Using triple double quotes", "C) Using multiple '#' symbols"],
        "answer": "A",
        "explanation": "Multiline comments in Python can be created using triple single quotes (''' ''') or triple double quotes (\"\"\" \"\"\")."
    },
    "Q216": {
        "question": "What is a class in Python?",
        "options": ["A) A function template", "B) A blueprint for creating objects", "C) A method collection"],
        "answer": "B",
        "explanation": "A class in Python is a blueprint for creating objects, providing initial values for state and implementations of behavior."
    },
    "Q217": {
        "question": "How do you check if a key exists in a dictionary?",
        "options": ["A) 'key' in dict", "B) dict.contains('key')", "C) dict.has_key('key')"],
        "answer": "A",
        "explanation": "You can check if a key exists in a dictionary with the syntax 'key in dict'."
    },
    "Q218": {
        "question": "What is a closure in Python?",
        "options": ["A) A technique for data hiding", "B) A function returned by another function", "C) A way to close a file"],
        "answer": "B",
        "explanation": "A closure in Python is a function object that remembers values in enclosing scopes even if they are not present in memory."
    },
    "Q219": {
        "question": "How do you concatenate strings in Python?",
        "options": ["A) Using the + operator", "B) Using the concat() method", "C) With the join() method"],
        "answer": "A",
        "explanation": "Strings in Python are commonly concatenated using the + operator."
    },
    "Q220": {
        "question": "What is a decorator in Python?",
        "options": ["A) A tool for decorating code with comments", "B) A function that modifies the functionality of another function", "C) A way to style Python output"],
        "answer": "B",
        "explanation": "A decorator in Python is a function that takes another function as an argument and extends its behavior without explicitly modifying it."
    },
    "Q221": {
        "question": "How do you remove all elements from a list in Python?",
        "options": ["A) list.clear()", "B) del list[:]", "C) Both A and B"],
        "answer": "C",
        "explanation": "Both list.clear() and 'del list[:]' will remove all elements from a list in Python."
    },
    "Q222": {
        "question": "What is the purpose of the 'nonlocal' keyword in Python?",
        "options": ["A) To create a nonlocal variable", "B) To access a variable in an enclosing scope", "C) To declare a variable as immutable"],
        "answer": "B",
        "explanation": "The 'nonlocal' keyword is used in nested functions to refer to variables from the enclosing scope."
    },
    "Q223": {
        "question": "What is the difference between the '== operator and the 'is' operator?",
        "options": ["A) '==' checks values, 'is' checks identities", "B) '==' checks identities, 'is' checks values", "C) No difference"],
        "answer": "A",
        "explanation": "'==' compares the values of objects, while 'is' compares their identities (memory locations)."
    },
    "Q224": {
        "question": "What is the output of 'all([True, False, True])' in Python?",
        "options": ["A) True", "B) False", "C) Error"],
        "answer": "B",
        "explanation": "The 'all()' function returns True if all elements in the iterable are true. Since there's a False, the output is False."
    },
    "Q225": {
        "question": "How do you reverse a string in Python?",
        "options": ["A) reversed(string)", "B) string[::-1]", "C) string.reverse()"],
        "answer": "B",
        "explanation": "You can reverse a string in Python by slicing with the syntax 'string[::-1]'."
    },
    "Q226": {
        "question": "What is the purpose of the '__main__' in Python?",
        "options": ["A) It indicates the start of the program", "B) It checks if a script is run directly or imported", "C) It is the main function declaration"],
        "answer": "B",
        "explanation": "If __name__ == '__main__' is used to check if the script is being run directly or imported."
    },
    "Q227": {
        "question": "What is the output of 'type(lambda x: x)'?",
        "options": ["A) <class 'function'>", "B) <class 'lambda'>", "C) <class 'method'>"],
        "answer": "A",
        "explanation": "The lambda function is of the type 'function' in Python."
    },
    "Q228": {
        "question": "How can you generate a list of numbers from 0 to 9 in Python?",
        "options": ["A) list(0, 10)", "B) [0:10]", "C) list(range(10))"],
        "answer": "C",
        "explanation": "The expression 'list(range(10))' generates a list of numbers from 0 to 9."
    },
    "Q229": {
        "question": "What does 'list.append(x)' do?",
        "options": ["A) Inserts x at the beginning of the list", "B) Adds x to the end of the list", "C) Replaces an element with x"],
        "answer": "B",
        "explanation": "'list.append(x)' adds the item x to the end of the list."
    },
    "Q230": {
        "question": "How do you check if a string contains a particular substring in Python?",
        "options": ["A) 'substring' in string", "B) string.contains('substring')", "C) string.find('substring') > -1"],
        "answer": "A",
        "explanation": "You can check if a substring is present in a string using the syntax 'substring in string'."
    },
    "Q231": {
        "question": "What is a Python package?",
        "options": ["A) A way to organize python scripts", "B) A compressed file containing Python modules", "C) A built-in Python module"],
        "answer": "A",
        "explanation": "A Python package is a way to organize Python modules into a directory hierarchy."
    },
    "Q232": {
        "question": "How do you create a new instance of a class in Python?",
        "options": ["A) ClassName.new()", "B) new ClassName()", "C) ClassName()"],
        "answer": "C",
        "explanation": "An instance of a class is created in Python by calling the class name followed by parentheses, as in 'ClassName()'."
    },
    "Q233": {
        "question": "What is the result of '3 + 2 * 2' in Python?",
        "options": ["A) 10", "B) 7", "C) 5"],
        "answer": "B",
        "explanation": "According to Python's operator precedence, the multiplication is done first, resulting in '3 + 4', which equals 7."
    },
    "Q234": {
        "question": "How can you remove an item from a list by its index in Python?",
        "options": ["A) list.remove(index)", "B) del list[index]", "C) list.pop(index)"],
        "answer": "C",
        "explanation": "The 'list.pop(index)' method removes and returns the item at the given index."
    },
    "Q235": {
        "question": "What is an iterable in Python?",
        "options": ["A) Any Python object with an __iter__ method", "B) A function that iterates over a sequence", "C) A special type of loop"],
        "answer": "A",
        "explanation": "An iterable is any Python object capable of returning its members one at a time, permitting it to be iterated over in a loop."
    },
    "Q236": {
        "question": "What is the purpose of the 'return' keyword in Python?",
        "options": ["A) To exit a program", "B) To exit the current function and return a value", "C) To return control to the calling function without returning a value"],
        "answer": "B",
        "explanation": "The 'return' keyword is used to exit a function and return a value."
    },
    "Q237": {
        "question": "What does 'import os' do in Python?",
        "options": ["A) Imports operating system functionalities", "B) Checks the OS of the system", "C) Creates an OS object"],
        "answer": "A",
        "explanation": "'import os' brings the OS module into the script, allowing interaction with the operating system."
    },
    "Q238": {
        "question": "How do you get the length of a list in Python?",
        "options": ["A) list.length()", "B) len(list)", "C) list.size()"],
        "answer": "B",
        "explanation": "The 'len()' function is used to get the number of items in a list or other collections."
    },
    "Q239": {
        "question": "What is the output of 'print(2 ** 3)'?",
        "options": ["A) 6", "B) 8", "C) 9"],
        "answer": "B",
        "explanation": "'**' is the exponentiation operator in Python, so '2 ** 3' calculates 2 to the power of 3, which is 8."
    },
    "Q240": {
        "question": "How do you check if a number is even in Python?",
        "options": ["A) number % 2 == 0", "B) number / 2 == 0", "C) number.isEven()"],
        "answer": "A",
        "explanation": "To check if a number is even, you can use the modulo operator, as in 'number % 2 == 0'."
    }

}
#############################################################

# RANDOM EVENTS

#############################################################

random_events = [
            {
                "description": "You find a $20 bill on the ground. Do you pick it up?# Or are you too noble for such trivial gains?",
                "positive_outcome": "Congratulations, your integrity is still intact.# Plus,# you're $20 richer.",
                "negative_outcome": "Oh no, it had poop all over it! Now you need to wash your hands!# You lose some happiness.",
                "effect": {"finances": 20, "neg_happiness": -10},
                "positive_chance": 0.8
            },
            {
                "description": "A mysterious figure offers you a chance to invest in a# 'revolutionary'# startup.# Do you invest?",
                "positive_outcome": "Wow, it actually worked.# The startup succeeded, and your investment paid off!",
                "negative_outcome": "Surprise!## The startup was a bust. Better luck next time.",
                "effect": {"finances": 100, "neg_finances": -40},
                "positive_chance": 0.2
            },
            {
                "description": "You find a stray dog. Do you take it home?# It could be a loyal friend or a flea-ridden beast.",
                "positive_outcome": "The dog is a loving companion, boosting your happiness significantly.",
                "negative_outcome": "Turns out it's more demon than dog.# There goes your happiness.",
                "effect": {"happiness": 15, "neg_happiness": -10},
                "positive_chance": 0.7
            },
            {
                "description": "A street artist offers to draw your portrait for free.# Do you accept and pose?",
                "positive_outcome": "The portrait is stunning!# You feel a surge of happiness.",
                "negative_outcome": "The portrait looks nothing like you##... You hope.# How...# disappointing.",
                "effect": {"happiness": 10, "neg_happiness": -5},
                "positive_chance": 0.6
            },
            {
                "description": "You've been offered a questionable #'magic'# potion for free.# Do you drink it?",
                "positive_outcome": "Surprisingly,# you feel fantastic!# What was in that?",
                "negative_outcome": "You feel sick.# That was not a wise decision.",
                "effect": {"happiness": 20, "neg_happiness": -15},
                "positive_chance": 0.3
            },
            {
                "description": "A lost-looking tourist asks for directions.# Do you help them?",
                "positive_outcome": "They were so grateful, they gave you a gift!",
                "negative_outcome": "Turns out they were a pickpocket.## How unfortunate.",
                "effect": {"finances": 5, "neg_finances": -10},
                "positive_chance": 0.7
            },
            {
                "description": "A vending machine fails to dispense your snack.# Do you shake it violently or walk away?",
                "positive_outcome": "With a mighty shake, your snack falls, along with some extra change.# Victory!",
                "negative_outcome": "The machine topples over onto you.## How embarrassingly tragic.# \nUnfortunately, you only stub your toe.",
                "effect": {"finances": 10, "neg_happiness": -15},
                "positive_chance": 0.5
            },
            {
                "description": "You discover an unattended laptop in a cafe.# Do you turn it in?",
                "positive_outcome": "Your honesty is rewarded with heartfelt thanks and a free coffee!",
                "negative_outcome": "Oh dear!## You were caught touching the computer.# They consider you a thief and run you off.",
                "effect": {"happiness": 10, "neg_happiness": -10},
                "positive_chance": 0.8
            },
            {
                "description": "You're offered a chance to participate in a mystery taste test.# Do you accept?",
                "positive_outcome": "Delicious!# That was unexpectedly satisfying.",
                "negative_outcome": "Disgusting!# Your taste buds will never forgive you.",
                "effect": {"happiness": 10, "neg_happiness": -10},
                "positive_chance": 0.5
            },
            {
                "description": "A fortune teller offers to read your future for free.# Do you believe in such things?",
                "positive_outcome": "Her predictions are eerily accurate.# A future of joy, perhaps?",
                "negative_outcome": "Doom and gloom!## Hopefully,# it's all nonsense.",
                "effect": {"happiness": 10, "neg_happiness": -10},
                "positive_chance": 0.5
            },
            {
                "description": "You find a wallet full of cash.# Do you take it?",
                "positive_outcome": "Full of ones, but still# You got quite the haul for your lack of morals.",
                "negative_outcome": "Someone sees you reach for it.# You feel guilty and stop.## Coward.",
                "effect": {"finances": 50, "neg_happiness": -10},
                "positive_chance": 0.5
            },
            {
                "description": "You receive an email claiming you've won a prize.# Do you click the link?",
                "positive_outcome": "It's legitimate! You've won a small fortune!",
                "negative_outcome": "It's a scam. You should have known better.",
                "effect": {"finances": 1000, "neg_finances": -200},
                "positive_chance": 0.1
            },
            {
                "description": "You're given the chance to beta test a secret new game from your friend.# Do you accept?",
                "positive_outcome": "The game is amazing, and your feedback makes it into the final version!",
                "negative_outcome": "Your friend was hacked.# It even breaks your computer.",
                "effect": {"happiness": 20, "neg_finances": -600},
                "positive_chance": 0.7
            },
            {
                "description": "A stranger offers you a riddle.# Solve it and win a prize. Do you try?",
                "positive_outcome": "You solve it!# The prize is a delightful surprise.",
                "negative_outcome": "You can't solve it.# The stranger smirks and walks away.",
                "effect": {"happiness": 10, "neg_happiness": -5},
                "positive_chance": 0.5
            },
            {
                "description": "A local gym offers you a free trial membership.# Do you sign up?",
                "positive_outcome": "You feel healthier and more energized than ever!",
                "negative_outcome": "You pull a muscle on the first day.## Maybe exercise isn't for you.",
                "effect": {"happiness": 20, "neg_happiness": -10},
                "positive_chance": 0.7
            },
            {
                "description": "You're offered a ride in a self-driving car.# Do you get in?",
                "positive_outcome": "It's a smooth and fascinating ride.# The future is now!",
                "negative_outcome": "The car takes you to the wrong destination.## Not so smart after all.",
                "effect": {"happiness": 5, "neg_happiness": -5},
                "positive_chance": 0.7
            },
            {
                "description": "Your internet goes out right before an important virtual meeting.# Do you try to fix it yourself?",
                "positive_outcome": "You manage to fix it! The day is saved, and you're hailed as the office hero.##.. to yourself.",
                "negative_outcome": "You made it worse.# Now you're using your neighbor's unsecured Wi-Fi.",
                "effect": {"happiness": 10, "neg_happiness": -10},
                "positive_chance": 0.5
            },
            {
                "description": "Your neighbor's alarm has been blaring for hours.# Do you go knock on their door?",
                "positive_outcome": "Turns out they're on vacation and grateful you reached out.# You've made a new ally.",
                "negative_outcome": "They blame you for waking them up.# Neighborly relations have soured.",
                "effect": {"happiness": 10, "neg_happiness": -10},
                "positive_chance": 0.8
            },
                    {
                "description": "You're late for work and the only breakfast option is a gas station burrito.# Do you risk it?",
                "positive_outcome": "Surprisingly, it's delicious.# You start your day on a high note.",
                "negative_outcome": "As expected, it's a gastronomical disaster.## Your day just got longer.",
                "effect": {"happiness": 10, "neg_happiness": -15},
                "positive_chance": 0.5
            },
            {
                "description": "You find an old lottery ticket in a jacket pocket.# Do you check if it's a winner?",
                "positive_outcome": "Incredibly, it's a small jackpot!## Your forgotten ticket is now a windfall.",
                "negative_outcome": "It's a dud.# Just a reminder of your consistently bad luck in lotteries.",
                "effect": {"finances": 100, "neg_happiness": -5},
                "positive_chance": 0.1
            },
            {
                "description": "A friend offers you a share in a cryptocurrency venture.# Do you invest?",
                "positive_outcome": "The gamble pays off!# The value skyrockets overnight.",
                "negative_outcome": "The market crashes.# Your investment evaporates.",
                "effect": {"finances": 100, "neg_finances": -100},
                "positive_chance": 0.5
            },
            {
                "description": "A sidewalk vendor is giving away designer bags.# Do you buy one?",
                "positive_outcome": "It's a steal! High quality at a low price.#.. Free!",
                "negative_outcome": "It falls apart within days. You've been duped.",
                "effect": {"happiness": 20, "neg_happiness": -10},
                "positive_chance": 0.4
            },
            {
                "description": "A local store is going out of business and having a huge sale.# Do you check it out?",
                "positive_outcome": "You snag some great deals. Your savvy shopping pays off and you save on the usual groceries.",
                "negative_outcome": "The sale is a bust. Everything good is gone or overpriced.",
                "effect": {"finances": 50, "neg_happiness": -5},
                "positive_chance": 0.6
            },
            {
                "description": "You notice an unusual charge on your credit card statement.# Do you investigate?",
                "positive_outcome": "It's a bank error in your favor.# You get a small financial bonus.",
                "negative_outcome": "Hours on the phone resolve nothing.# The charge remains.",
                "effect": {"finances": 15, "neg_happiness": -10},
                "positive_chance": 0.5
            },
            {
                "description": "You've mustered the courage to ask your crush out on a date.# Do you go through with it?",
                "positive_outcome": "Surprisingly,### they say yes!# Your heart races with excitement and happiness.",
                "negative_outcome": "Well,## that didn't go as planned.# They say no, leaving you to nurse your heart.",
                "effect": {"happiness": 30, "neg_happiness": -20},
                "positive_chance": 0.5}
                #Add more as needed
]

#############################################################

# RANDOM INTRODUCTIONS

#############################################################

introductions = [
    {
        "text": "Welcome to the Life of .Py:# \na simulation that's as thrilling as watching paint dry.#\n"
                "Here, you'll experience the existential joy of being a Python programmer.#\n"
                "Embrace a world of monotony,# isolation,# \nand our special brand of cynicism.#\n"
                "You've somehow convinced someone to employ you.# Work from 9 AM to 9 PM for an \nextravagant $15 per hour.#\n"
                "Can't work late, though.# \nThe company locks the database after hours to protect its precious assets.#\n"
                "Promotion?# If you prove yourself,# perhaps.#\n"
                "Enjoy Silicon Valley's sunny despair with a mere $3,000 monthly rent that you must earn.#\n"
                "If you think you have financial acumen:# Bankruptcy's left you with cash-only options.#\n"
                "That yellow bar?# Your dwindling happiness.# Watch it plummet or keep it filled.#\n"
                "The finance meter is as barren as your bank account.# Aim to fill it, without the luxury of credit.#\n"
                "Your hobbies?# Expensive distractions from your bleak reality.#\n"
                "Best of luck. You'll need it.#\n"
                "It's 11 PM, Sunday.# Sleep or collapse, your choice.# Tomorrow, the grind begins.#"
    },
    {
        "text": "Ah, Life of .Py:# \n- where your programming dreams come to wither.#\n"
                "You're about to embark on a soul-sucking journey of coding in Python.#\n"
                "Get ready for a life filled with sarcasm,# solitude,# and the sweet scent of mediocrity.#\n"
                "Job acquired.# Your coding marathon runs from 9 AM to 9 PM,# earning a lavish $15 per hour.#\n"
                "But no overtime allowed. #\nThe database gets locked to prevent you from getting any bright ideas.#\n"
                "Aim for a promotion.# Or don't.## It probably won't matter.#\n"
                "Your humble abode?# Silicon Valley, land of the overpriced# and underwhelmed.# \nOnly $3,000 for rent by the end of the month.#\n"
                "Financially speaking,# your bankruptcy means no credit lines,# just hard-earned cash.#\n"
                "The yellow bar signifies your already meager happiness.#\n Try not to let it hit rock bottom.#\n"
                "Your financial bar beside it?# A pitiful sight. You cannot even tell it is green.# \nCredit isn't an option, so earn that green.#\n"
                "Hobbies are your costly escape from this virtual misery.#\n"
                "Survive if you can.#\n"
                "Tick-tock, it's 11 PM.# \nCollapse into bed or on the floor. Your choice.# Work looms tomorrow.#"
    },
    {
        "text": "Welcome to the Life of .Py:# \nwhere your programming aspirations come to die a slow death.#\n"
                "This game is as close to programmer life as you'll get\n## - a parade of tedium and solitude,# seasoned with sarcasm.#\n"
                "Congratulations on the job.#\nYou'll be coding from 9 AM to 9 PM for a king's ransom of $15 an hour.#\n"
                "Don't bother working late.# \nThe company zealously guards its database post-9 PM, fearing theft.#\n"
                "Promotions?# A distant fantasy in this digital dungeon.## But maybe.#\n"
                "Your residence?# Silicon Valley.# Enjoy paying $3,000 for the privilege of existing there for a month.#\n"
                "With your credit history in ruins,# borrowing is not an option.#\n"
                "The yellow bar is your happiness,# currently middling.# Don't let it crash.#\n"
                "Your finances?# A void as empty as your aspirations. No credit to rescue you here.#\n"
                "Hobbies:# the only expensive joys in your otherwise mundane existence.#\n"
                "Good luck, you'll desperately need it.#\n"
                "It's 11 PM, Sunday.# \nTime to rest your weary soul. Tomorrow, your mundane odyssey begins.#"
    }
        ]


