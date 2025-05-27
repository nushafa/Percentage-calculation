#take marks as input from user
print("Enter marks of 4 subjects out of 100 marks: ")
english = int(input("English: "))
math = int(input("Math: "))
science = int(input("Science: "))
bangla = int(input("Bangla: "))

#  Let's claculate the percentage of marks
sum = english + math + science + bangla
print("The sum of all the subjects is: ", sum)

perc = (sum / 400) * 100
print(end="Percentage Marks = ")
print(perc)