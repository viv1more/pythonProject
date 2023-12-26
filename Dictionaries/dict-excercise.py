student_marks = {

    "Gaurav": 90,
    "Vivek": 87,
    "Mangesh": 95,
    "ABCD": 700

}

print(student_marks)

student_grades = {}

for key in student_marks:

    if 91 <= student_marks[key] <= 100:
        student_grades[key] = "Outstanding"
    elif 81 <= student_marks[key] <= 90:
        student_grades[key] = "A+"
    elif 65 <= student_marks[key] < 90:
        student_grades[key] = 'A'
    elif 40 <= student_marks[key] < 65:
        student_grades[key] = 'B'
    elif student_marks[key] < 40:
        student_grades[key] = 'Failed'
    else:
        student_grades[key] = "Invalid"

print(student_grades)
