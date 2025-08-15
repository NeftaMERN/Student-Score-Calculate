import os

Fill_NAME = "grades.txt"

def add_student():

    name = input("Enter Your Name: ")
    score = input("Enter Your Score: ")
    score_list = [int(s.strip()) for s in score.split(',')] # the score change to int use for

    avarage = sum(score_list) / len(score_list)

    with open(Fill_NAME, "a") as f:
        f.write(f"{name}: {",".join(map(str, score_list))}:{avarage:.2f}\n") # change the int to str with .join

        print(f"{name} Your Score {avarage:.2f}") # .2f is float
def viwe_student():
    if not os.path.exists(Fill_NAME): # not os.path.exists the score dose note in the fill
        print(f"No student data not foun")
        return
    
    with open(Fill_NAME, 'r') as f:
        lines = f.readlines()

    print("\n Student Recourd")

    for line in lines:
        name, score, ave = line.strip().split(':')
        print(f"{name} Score:{score} avarage:{ave}")

def mnue():
    while True:
        print("\n 1, Add Student")
        print("\n 2, View Student")
        print("\n 3, Exit")
        choice = input("Choice Your: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            viwe_student()
        elif choice == "3":
            print("Goodbye")
            break
        else:
            print("Invalid choice, try again!")
mnue()        