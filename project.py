#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys
import copy

filename = "students.txt"
args = sys.argv
if len(args) == 2:
    filename = sys.argv[1]
else :
    filename = filename

#filename = "students.txt"
f = open(filename, "r")
student_list = []

def made_average(x):
    x_mean = (int(x[2]) + int(x[3])) / 2
    return x_mean

def made_grade(x):
    if x[4] >= 90 :
        return "A"
    elif x[4] >= 80 :
        return "B"
    elif x[4] >= 70 :
        return "C"
    elif x[4] >= 60 :
        return "D"
    else :
        return "F"

def show(x):
    x = sort_values(x)
    print("{:<10} {:<12} {:<8} {:<6} {:<8} {:<5}".format("student", "Name", "Midterm", "Final", "Average", "Grade"))
    print("-" * 58)
    for i in x:
        print("{:<10} {:<12} {:<8} {:<6} {:<8} {:<5}".format(*i))

def sort_values(x):
    x = sorted(x, reverse=True, key = lambda x : x[4])
    return x

def search(x):
    student_id = int(input("Student ID: "))
    student_id_list =  [int(row[0]) for row in x]
    
    if student_id in student_id_list:
        indexs = student_id_list.index(student_id)
        student_info = x[indexs]
        print("{:<10} {:<12} {:<8} {:<6} {:<8} {:<5}".format("student", "Name", "Midterm", "Final", "Average", "Grade"))
        print("-" * 58)
        print("{:<10} {:<12} {:<8} {:<6} {:<8} {:<5}".format(*student_info))
    else :
        print("NO SUCH PERSON.")

def changescore(x):
    student_id = int(input("Student ID: "))
    student_id_list = [int(row[0]) for row in x]
    
    if student_id in student_id_list:
        indexs = student_id_list.index(student_id)
        
        while True:
            exam = input("Mid/Final? ")
            
            if exam.lower() == "mid":
                midscore = int(input("Input new score: "))
                if 0 <= midscore <= 100:
                    student_info = x[indexs]
                    student_infos = copy.deepcopy(student_info)
                    print("{:<10} {:<12} {:<8} {:<6} {:<8} {:<5}".format("student", "Name", "Midterm", "Final", "Average", "Grade"))
                    print("-" * 58)
                    print("{:<10} {:<12} {:<8} {:<6} {:<8} {:<5}".format(*student_infos))
                    print("Score changed.")
                    student_info[2] = midscore
                    student_info[4] = made_average(student_info)
                    student_info[5] = made_grade(student_info)
                    print("{:<10} {:<12} {:<8} {:<6} {:<8} {:<5}".format(*student_info))
                    x[indexs] = student_info
                    break  
                else:
                    break
                
            elif exam.lower() == "final":
                finalscore = int(input("Input new score: "))
                if 0 <= finalscore <= 100:
                    student_info = x[indexs]
                    student_infos = copy.deepcopy(student_info)
                    print("{:<10} {:<12} {:<8} {:<6} {:<8} {:<5}".format("student", "Name", "Midterm", "Final", "Average", "Grade"))
                    print("-" * 58)
                    print("{:<10} {:<12} {:<8} {:<6} {:<8} {:<5}".format(*student_infos))
                    print("Score changed.")
                    student_info[3] = finalscore
                    student_info[4] = made_average(student_info)
                    student_info[5] = made_grade(student_info)
                    print("{:<10} {:<12} {:<8} {:<6} {:<8} {:<5}".format(*student_info))
                    x[indexs] = student_info
                    break  
                else:
                    break
            
            else:
                break  
        
    else:
        print("NO SUCH PERSON.")

def add(x):
    student_id = int(input("Student ID: "))
    student_id_list = [int(row[0]) for row in x]
    
    if student_id in student_id_list:
        print("ALREADY EXISTS.")
    else :
        new_name = input("Name: ")
        new_mid = input("Midterm Score: ")
        new_final = input("Final Score: ")
        print("Student added.")
        new_list = [student_id, new_name, new_mid, new_final]
        new_list.append(made_average(new_list))
        new_list.append(made_grade(new_list))
        x.append(new_list)

def searchgrade(x):
    grades = input("Grade to search: ")
    if grades not in ["A", "B", "C", "D", "F"]:
        return
    
    grade_list = [row[5] for row in x]
    new_list = []
    
    if grades in grade_list :
        for i in x:
            if i[5] == grades:
                new_list.append(i)
        
        new_list = sort_values(new_list)
        print("{:<10} {:<12} {:<8} {:<6} {:<8} {:<5}".format("student", "Name", "Midterm", "Final", "Average", "Grade"))
        print("-" * 58)
        for i in new_list :
            print("{:<10} {:<12} {:<8} {:<6} {:<8} {:<5}".format(*i))
    else :
        print("NO RESULTS.")

def remove(x):
    
    if not x:
        print("List is Empty.")
    else :
        student_id = int(input("Student ID: "))
        student_id_list = [int(row[0]) for row in x]
        if student_id in student_id_list:
            del x[student_id_list.index(student_id)]
            print("Student Removed.")
        else :
            print("NO SUCH PERSON.")

def quit(x):
    yesno = input("Save data? [yes/no] ")

    if yesno == "no":
        return True  
    elif yesno == "yes":
        
        filenames = input("File name: ")
        x = sort_values(x)
        with open(filenames, "w") as fr:
            for i in x:
                fr.write('\t'.join(map(str, i[:4])) + '\n')
        return True  
    else :
        print("yes/no만 가능")
        return True  

def command():
    while True:
        co = input("#")
        co = co.lower()
        if co == "show":
            show(student_list)
            print("")
        elif co == "search":
            search(student_list)
            print("")
        elif co == "changescore":
            changescore(student_list)
            print("")
        elif co == "add":
            add(student_list)
            print("")
        elif co == "searchgrade":
            searchgrade(student_list)
            print("")
        elif co == "remove":
            remove(student_list)
            print("")
        elif co == "quit":
            if quit(student_list):
                break  
        else:
            pass

for line in f:
    line_list = line.strip().split("\t")
    line_list.append(made_average(line_list))
    line_list.append(made_grade(line_list))
    student_list.append(line_list)

command()

