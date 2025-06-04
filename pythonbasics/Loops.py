# for i in range/sequence:
#     statement 1
#     statement 2 
#     statement 3

#print first 10 numbers using for loop
for i in range(1,11):   #range(start, end) -> start is inclusive, end is exclusive
    print(i)

#in range if i want to make end inclusive then I can do this
for i in range(1,11+1):   #range(start, end) -> start is inclusive, end is exclusive
    print(i)    

for i in range(10,21):
    if i % 2 == 0:  #if i is even
        print(i)    

#do the same without using if
for i in range(10,21,2):  #range(start, end, step)-> start is inclusive, end is exclusive, step is the increment

    print(i)

#print sum of all even numbers from 10 to 20
sum=0
for i in range(10,21,2):  #range(start, end, step)-> start is inclusive, end is exclusive, step is the increment
    sum=sum+i
print(f"Sum of all even numbers from 10 to 20 is: {sum}")    

#print sum of all odd numbers from 1 to 20
sum = 0
for i in range(11, 21, 2):
    sum = sum + i
print("The sum of odd numbers between 10 and 20 is:", sum)

numbers= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print all numbers in the list
for i in numbers:
    print(i**i) #use ** operator to print the power of the number

   
 #Range function
for i in range(1,6):
     print(i) #prints 1 to 5

#while loop
count=1
#condition: Run loop while count is less than or equal to 5
while count <= 5:
    print(count)
    count = count+1  #increment count by 1

#Break and Continue ,Pass Statements
numbers=[10,40,100,230]
for i in numbers:
    if i>100:
        break
    print("Current number is:", i)

# continue statement
for i in numbers:
    if i == 100:
        continue  # skip the rest of the loop for this iteration
    print("Current number is:", i)  
# Problem Description: Lucky Number Guessing Game
# Objective
# Create a Python program that allows the user to play a "lucky number guessing game." 
# The program will randomly select a number between 1 and 10 (inclusive), and the user must guess the number. 
# The program will provide feedback after each guess, indicating whether the guess was too low, too high, or correct. 
# The game continues until the user guesses the correct number, and the program will display the total number of attempts taken.

# Requirements
# Random Number Generation

# The program should generate a random integer between 1 and 10 (inclusive) at the start of the game.
# User Input

# The program should repeatedly prompt the user to guess the lucky number.

# Feedback

# If the user's guess is lower than the lucky number, print:
# "Too low! Try again."
# If the user's guess is higher than the lucky number, print:
# "Too high! Try again."
# If the user's guess is correct, print:
# "Congratulations! You've guessed my lucky number {number} in {attempts} attempts."
# (Replace {number} and {attempts} with the actual values.)
# Attempts Counter

# The program should keep track of the number of guesses the user makes.
# Looping

# The guessing process should continue until the user guesses the correct number.
# Input Validation (Optional Enhancement)

# Optionally, handle invalid inputs (e.g., non-integer values or numbers outside the range 1–10) gracefully.



#hands on 2
#create a program to print the multiplication table values from 1 to 10
# sample output:
# Multiplication Table of 1
# 1 2 3 4 5 6 7 8 9 10
# # Multiplication Table of 2
# # 2 4 6 8 10 12 14 16 18 20
# Multiplication Table of 3
# # 3 6 9 12 15 18 21 24 27 30
#  