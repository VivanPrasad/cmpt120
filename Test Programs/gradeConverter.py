# gradeConverter.py

# Description:

# Author: M. Vivan Prasad
# Date: 9/15/23 F



#Asks user to enter a grade
grade : str = input("Please enter a grade (integer between 0 and 100?\n").strip()

#Validates if the grade is in the range between 0 to 100
while not grade in range(0,101) and not grade.isnumeric():
    grade = input("Must be between 0 and 100 and a valid number! Try again\n").strip()
letterGrade = {
    "A":range(90,101),
    "B":range(80,90),
    "C":range(70,80),
    "D":range(60,70),
    "E":range(50,60),
    "F":range(0,50)}

for letter in letterGrade.keys():
    if int(grade) in letterGrade[letter]:
        print(f"Your letter grade with a value of {int(grade)} is a '{letter}'!")
        break
#Get the user's grade (int)
# A -> 90-100
# B -> 80-89
# C -> 70-79
# D -> 60-69
# E -> 50-59
# F -> 0-49
