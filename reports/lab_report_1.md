# Lab Report 1

## Title
Introduction to Python Programming Basics

## Theory
This lab covers the fundamentals of Python programming, focusing on syntax, variables, basic input/output operations, and conditional statements. Python is an interpreted, high-level programming language known for its readability. Understanding how to declare variables and manage basic control flow using `if` statements is the first step toward building complex AI systems.

## Algorithms
The concepts applied here are sequential execution and conditional branching.
- **Sequential Execution:** Instructions are executed line by line.
- **Conditional Branching:** Execution paths change based on whether a boolean condition evaluates to true or false.

## Code Implementation
```python
print("hello")
variable = 5
print("printing string with variable of value: ",variable)
print(f"alternative print syntax:\nvariable of value: {variable}")

true = 1

if(true):
    print("true line 1")
    print("true line 2")

if(true): {print("true line 3"),print("true line 4")}

if(true): print("true line 5")
```

## Output
```
hello
printing string with variable of value:  5
alternative print syntax:
variable of value: 5
true line 1
true line 2
true line 3
true line 4
true line 5
```

## Discussion
The implementation demonstrates different ways to output text in Python, including string concatenation and the modern f-string formatting (`f"..."`), which makes inserting variables into strings highly readable. Additionally, we explored how the `if` statement evaluates a truthy value (in this case, `1` representing `True`) to conditionally execute blocks of code. 

## Conclusion
We successfully learned the basic syntax of Python, how to declare variables, print them to the console, and use conditional statements to control code execution.
