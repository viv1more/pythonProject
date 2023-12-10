# Find the Average height of students from the given list

student_height = input("Enter the height of all Students from the Class ").split()

# printing the height using list
for n in range(0, len(student_height)):  # used to iterate through the 0th index to the length of list index
    student_height[n] = int(student_height[n])  # converting input into int type to perform logic in future
print(student_height)

averageHeight = sum(student_height) / len(student_height)

print(f"Average Height for Students in this Class is {round(averageHeight, 2)}CM")
