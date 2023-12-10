# Find the Marks of students from the given list

student_marks = input("Enter Marks of all Students from the Class ").split()

# printing the marks using list
for n in range(0, len(student_marks)):  # used to iterate through the 0th index to the length of list index
    student_marks[n] = int(student_marks[n])  # converting input into int type to perform logic in future
print(student_marks)
'''
#Using Max Function
MaximumMarks = max(student_marks)

# noinspection PyTypeChecker
print(f"Maximum for Students in this Class is {MaximumMarks}") '''


# Without Using Max Function

highestScore = 0  # created variable which will be used later

for eachscore in student_marks:  # will iterate through each element of list student_marks
    if eachscore > highestScore:  # checks for condition , if satisfy it will assign value to highestscore
        highestScore = eachscore

print(f"Highest Score is {highestScore}")
