student_name=input("Enter the student name: ")
student_age=int(input("Enter the student age: "))
student_mark=int(input("Enter the student mark: "))
#f-string->that means formatted string which is used to use the variable inside the string
if student_mark >= 80 and student_mark <= 100:
    print(f"{student_name} has passed the exam with Distinction (mark: {student_mark}).")
elif student_mark >= 60:
    print(f"{student_name} has passed the exam with First Class (mark: {student_mark}).")
elif student_mark >= 50:
    print(f"{student_name} has passed the exam with Second Class (mark: {student_mark}).")
elif student_mark >= 35:
    print(f"{student_name} has passed the exam (mark: {student_mark}).")
else:
    print(f"{student_name} has failed the exam with a mark of {student_mark}.")

