# marks = input("Input your marks: ")
# marks = int(marks)
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
