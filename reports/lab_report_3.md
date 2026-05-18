# Lab Report 3

## Title
Control Flow in Python: Conditionals and Loops

## Theory
Control flow dictates the order in which statements are executed in a script.
- **Complex Conditionals (`if-elif-else`):** Used to check multiple conditions sequentially. The program executes the block of the first true condition and skips the rest.
- **Loops (`for` loop):** Used to iterate over a sequence (like a list, tuple, or range). The `range()` function generates a sequence of numbers, which is particularly useful for executing a block of code a specific number of times.

## Algorithms
- Multiple Conditional Branching (Grading logic)
- Iterative loop with a counter

## Code Implementation
```python
marks = int(input("Input your marks: "))
if(marks>=40):
    print("You Passed")
    if(marks>=80):
        print("Grade: A+")
    elif(marks>75):
        print("Grade: A")
    elif(marks>70):
        print("Grade: A-")
    elif(marks>65):
        print("Grade: B+")
    elif(marks>60):
        print("Grade: B")
    elif(marks>55):
        print("Grade: B-")
    elif(marks>50):
        print("Grade: C+")
    elif(marks>45):
        print("Grade: C")
    elif(marks>40):
        print("Grade: D")
else:
    print("You Failed\nGrade: F")

num = int(input("Input how many times the loop should run: "))
for x in range(num+1):
    print(x)
```

## Output
*(Example Output based on user input)*
```
Input your marks: 85
You Passed
Grade: A+
Input how many times the loop should run: 3
0
1
2
3
```

## Discussion
The nested `if-elif` ladder ensures that only the highest applicable grade condition is executed, demonstrating mutually exclusive conditional logic. The `range(num+1)` function within the `for` loop efficiently generates numbers from 0 up to `num`. This eliminates the need to manually track iteration variables using a `while` loop, keeping the code clean.

## Conclusion
We successfully implemented a grading system and a counting loop, cementing our understanding of how to control program flow effectively for decision making and repetitive tasks.
