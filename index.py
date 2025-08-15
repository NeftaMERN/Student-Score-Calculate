import os

Fill_NAME = "gread.txt"

def add_student():

    name = input("Enter Your Name: ")
    score = input("Enter Your Score: ")
    score_list = [int(s.strip()) for s in score.split(',')]

    avarage = sum(score_list) / len(score_list)

    with open("Fill_NAME", "a") as f:
        f.write(f"{name}: {",".join(map(str, score_list))}:{avarage:.2f}\n")

        print(f"{name} Your Score {avarage:.2f}")

add_student()