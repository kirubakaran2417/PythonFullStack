# name=input("Enter your name: ")
# age=input("Enter your age: ")
# salary=input("Enter your salary: ")
# mobile=input("Enter your mobile number: ")

# print("Name:", name)
# print("Age:", age)
# print("Salary:", salary)

# print("mobile:", mobile)

# print(type(age))  # prints the type of age
# If you want to comment multiple lines you can select and press control+/

name,age,salary,mobile = input("Enter your name, age, salary, and mobile number separated by commas: ").split(',')
print("\n")
print("user details: ",name,",", age, salary, mobile)
