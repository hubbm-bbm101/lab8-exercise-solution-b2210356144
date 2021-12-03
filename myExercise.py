import sys

with open(f"{sys.argv[1]}","r+") as text:
    info =  text.read().split("\n")
    dic1 = {}
    for i in info:
        student, school = i.split(":")
        dic1[student] = school
for j in sys.argv[2].split(","):
    try:
        print(f"Name: {j}, University: {dic1[j]}")
    except:
        print(f"No record of {j} was found!")

