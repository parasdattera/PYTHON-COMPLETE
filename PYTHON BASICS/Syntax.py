'''
What is Python Syntax?
Python syntax refers to the set of rules that defines the combinations of symbols that are considered to be correctly structured programs in the Python language. These rules make sure that programs written in Python should be structured and formatted, ensuring that the Python interpreter can understand and execute them correctly.

'''

# python program to print "Hello World" 
print("Hello World")



'''

Indentation in Python
Python Indentation refers to the use of whitespace (spaces or tabs) at the beginning of a line of code in Python. It is used to define the code blocks. Indentation is crucial in Python because, unlike many other programming languages that use braces “{}” to define blocks, Python uses indentation. It improves the readability of Python code, but on other hand it became difficult to rectify indentation errors. Even one extra or less space can leads to identation error.

'''


'''

Python Variables
Variables in Python are essentially named references pointing to objects in memory. Unlike some other languages, in Python, you don't need to declare a variable's type explicitly. Based on the value assigned, Python will dynamically determine the type. In the below example, we create a variable 'a' and initialize it with interger value so, type of 'a' is int then we store the string value in 'a' it become 'str' type. It is called dynamic typing which means variable's data type can change during runtime.

'''


'''
Python Identifiers
In Python, identifiers are the building blocks of a program. Identifiers are unique names that are assigned to variables, functions, classes, and other entities. They are used to uniquely identify the entity within the program. They should start with a letter (a-z, A-Z) or an underscore “_” and can be followed by letters, numbers, or underscores. In the below example “first_name” is an identifier that store string value.

'''


'''
Python keywords
Keywords in Python are reserved words that have special meanings. For example if, else, while, etc. They cannot be used as identifiers. Below is the list of keywords in Python.


False       await         else          import          pass
None       break         except     in                   raise
True        class           finally      is                    return
and         continue    for            lambda        try
as            def              from        nonlocal       while
assert     del              global      not                 with
async      elif              if               or                   yield

'''


'''
Comments in Python
Comments in Python are statements written within the code. They are meant to explain, clarify, or give context about specific parts of the code. The purpose of comments is to explain the working of a code, they have no impact on the execution or outcome of a program.

Single line comments are preceded by the “#” symbol.


Python doesn't have a specific syntax for multi-line comments. However, programmers often use multiple single-line comments, one after the other, or sometimes triple quotes (either ”’ or “””), 
'''

'''
Multiple Line Statements
Writing a long statement in a code is not feasible or readable. Writing a long single line statement in multiple lines by breaking it is more readable so, we have this feature in Python and we can break long statement into different ways such as:

Using Backslashes (\)
In Python, you can break a statement into multiple lines using the backslash (\). This method is useful, especially when we are working with strings or mathematical operations.

'''