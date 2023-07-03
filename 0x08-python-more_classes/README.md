###Project Requirements:

Allowed editors: vi, vim, emacs
All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.8.5)
All files should end with a new line
The first line of all files should be #!/usr/bin/python3
A README.md file is mandatory
Code should adhere to the pycodestyle (version 2.8.*) guidelines
All files must be executable
The length of your files will be tested using wc command

###Learning Objectives:
By the end of this project, you should be able to explain the following concepts without external assistance:
Why Python programming is awesome

Python programming is awesome because it has a simple and readable syntax, a large standard library, and a vibrant community. It supports various programming paradigms, including OOP, functional programming, and procedural programming. Python's versatility and ease of use make it a popular choice for a wide range of applications.

What is Object-Oriented Programming (OOP)

Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects, which are instances of classes. It focuses on creating reusable and modular code by encapsulating data and behavior within objects. OOP promotes concepts such as inheritance, polymorphism, and encapsulation to enhance code maintainability and reusability.

"First-class everything" concept in Python

"First-class everything" is a concept in Python that treats all entities, such as functions, classes, and objects, as first-class citizens. It means they can be assigned to variables, passed as arguments to functions, returned from functions, and stored in data structures. This flexibility allows for powerful and expressive programming in Python.

Understanding classes and objects

A class is a blueprint or template that defines the structure and behavior of objects. It specifies the attributes (data) and methods (functions) that objects of the class will possess. An object is an instance of a class, created using the class's constructor. Objects can access the attributes and methods defined in their class.

Difference between a class and an object or instance

A class is a blueprint that defines the structure and behavior of objects. It is like a template. An object, on the other hand, is an instance of a class. It is a concrete entity created from the class. In simple terms, a class is a definition, and an object is the actual instantiation of that definition.

Attributes in Python

Attributes in Python are the properties or data associated with an object. They can be variables or fields that hold data. Attributes define the characteristics or state of an object and can be accessed using dot notation (object.attribute).

Usage of public, protected, and private attributes

In Python, the concept of public, protected, and private attributes is achieved through naming conventions. By convention, attributes starting with an underscore (_) are considered protected, indicating that they should not be accessed directly outside the class. Attributes starting with two underscores (__) are considered private, indicating they should not be accessed or modified directly from outside the class. Public attributes, not using any special naming conventions, can be accessed and modified freely.

Understanding the self parameter

The self parameter in Python is a reference to the current instance of a class. It allows accessing the attributes and methods of the object within the class. It is the first parameter of instance methods and must be explicitly included in the method definition.

Methods in Python

Methods in Python are functions defined within a class. They define the behavior or actions that objects of the class can perform. Methods can access and modify the object's attributes and interact with other objects.

Special __init__ method and its usage

The __init__ method is a special method in Python classes that is automatically called when an object is created from the class. It is used to initialize the object's attributes or perform any necessary setup during object creation.

Data Abstraction, Data Encapsulation, and Information Hiding

Data abstraction is a principle of OOP that focuses on exposing only essential information and hiding the internal implementation details. It allows us to define the interface of a class without exposing its internal complexity. Data encapsulation is the practice of bundling data and the methods that operate on that data within a single entity, i.e., an object. Encapsulation promotes information hiding and ensures that the object's internal state remains consistent.

Properties and their usage

Properties in Python provide a way to define computed or calculated attributes. They allow getting, setting, or deleting values as if they were regular attributes, but behind the scenes, they execute methods called getters, setters, and deleters.

Difference between an attribute and a property in Python

An attribute in Python is a variable associated with an object or class, holding data. A property, on the other hand, is a special attribute that has associated methods, such as getters, setters, and deleters, allowing controlled access to the attribute.

Pythonic way of writing getters and setters

In Python, the use of properties is considered a Pythonic way of implementing getters and setters. By defining getter and setter methods as properties, we can access and modify attributes in a controlled manner, providing abstraction and encapsulation.

Special __str__ and __repr__ methods and their usage

The __str__ and __repr__ methods are special methods in Python classes. They provide a string representation of an object. __str__ is used for creating human-readable string representations, while __repr__ is used for generating unambiguous string representations that can be used to recreate the object.

Difference between __str__ and __repr__

The main difference between __str__ and __repr__ is their intended purpose. __str__ is used for creating readable representations of an object, primarily for end-users. __repr__, on the other hand, is used for creating unambiguous representations of an object that can be used to recreate the object.

Class attributes and object attributes

Class attributes are attributes associated with a class itself rather than with its instances. They are shared among all instances of the class. Object attributes, also known as instance attributes, are specific to each instance of the class.

Difference between object attributes and class attributes

Object attributes are specific to each instance of a class and vary from object to object. Class attributes, on the other hand, are shared among all instances of a class and remain the same for all objects.

Class methods and their usage

Class methods in Python are methods that are bound to the class rather than its instances. They can access class-level attributes and perform operations related to the class itself.

Static methods and their usage

Static methods in Python are methods that belong to a class but do not have access to instance-specific or class-specific attributes. They are primarily used as utility methods or functions related to the class.

Dynamically creating arbitrary new attributes for existing instances of a class

Python allows dynamically creating new attributes for existing instances of a class by assigning values to attribute names using dot notation.

Binding attributes to objects and classes

In Python, attributes can be bound to objects by assigning values to attribute names using dot notation. Similarly, class attributes can be bound by assigning values directly to the class name.

Understanding the __dict__ attribute of a class and an instance

The __dict__ attribute is a dictionary that contains the attributes of an object or class. For an instance, it holds the instance-specific attributes, while for a class, it includes the class-level attributes.

How Python finds attributes of an object or class

Python finds attributes of an object or class by following the attribute resolution order, also known as the method resolution order (MRO). It first checks the object's dictionary, then the class's dictionary, and continues up the inheritance hierarchy until the attribute is found or an AttributeError is raised.

Usage of the getattr function

The getattr function in Python is used to retrieve the value of an attribute from an object. It takes the object and the attribute name as arguments and returns the attribute's value if found, or a default value if specified.
###Implementation Steps:

Create a new folder for the project.
Set up your preferred editor (vi, vim, emacs) for editing the project files.
Ensure you have Python 3 (version 3.8.5) installed on your system.
Inside the project folder, create a README.md file(this file) to document your project.
Start implementing the solutions for the tasks mentioned in the learning objectives. Create separate Python files for each task or group of related tasks.
Follow the provided guidelines for each file, such as adding the shebang line (#!/usr/bin/python3), using pycodestyle for code formatting, and ensuring all files are executable.
Test your code thoroughly to ensure it meets the project requirements and produces the expected results.
Check the length of your files using the wc command to ensure they are within the allowed limits.
Update the README.md file with relevant information about the project, including a brief description, instructions to run the code, and any additional details you deem necessary.
Double-check your code and documentation to ensure everything is in order and meets the project requirements.
Submit your project on time.

