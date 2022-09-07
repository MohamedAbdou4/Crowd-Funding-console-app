
from optparse import check_choice
import time
def ProjectMenu(chosenusr):
    
        print("""choose your action from list:
            c) create project
            v) view all projects
            e) edit Your projects
            d) delete your own projects
            done) done with program""")
        choice = choosenAction()
        if (choice == "c"):
             createProject(chosenusr)
        elif (choice == "v"):
             viewproject()
        elif (choice == "e"):
            editProject(chosenusr)
        elif (choice == "d"):
            deleteProject(chosenusr)
        elif(choice=='done'):
            print("Thank you GoodBye")
            exit
        else:
            print("wrong answer please choose correct one")
            choosenAction()
"========================================="

def choosenAction():
    x = input("Enter Your Choice: ")
    if (x.isalpha() or not x in range(1,6)):
        return (x)
    return choosenAction()

def Title():
    x = input("Project Title : ")
    if (x.isalpha()):
        return x
    else:
        return Title()
"==========================================="
def projectDetails():
    x = input("project details : ")
    if (x.isalpha()):
        return x
    else:
        return projectDetails()
"==========================================="
def Totaltarget():
    x = input("Totaltarget : ")
    if (x.isdigit()):
        return x
    else:
        return Totaltarget()
"==========================================="
import datetime

def date():
    Date = input("Enter the date in format 'dd-mm-yy' : ")
    day, month, year = Date.split('-')
    isValidDate = True
    if (isValidDate):
        return Date
    else:
        return date()
"==========================================="
def NewProject(chosenusr):
    title = Title()
    details = projectDetails()
    totaltarget = Totaltarget()
    startdate=date()
    enddate=date()
    project_id = round(time.time())
    data=f"{chosenusr}:{project_id}:{title}:{details}:{totaltarget}:{startdate}:{enddate}\n"
    return data
"==========================================="
def createProject(chosenusr):
    data=NewProject(chosenusr)
    file=open("AllProjects.txt",'a')
    file.writelines(data)
    file.close()
"==========================================="
def viewproject():
    file=open("AllProjects.txt",'r')
    data=file.readlines()
    print(data)
"==========================================="
def editProject(chosenusr):
    name=input("enter your project title : ")
    file = open("AllProjects.txt", 'r')
    data = file.readlines()
    file.close()
    index=0
    for i in data:
        d=i.split(":")
        if(d[2]==name and d[0]== chosenusr):
            data[index]=NewProject(chosenusr)
        index +=1
    file = open("AllProjects.txt", 'w')
    file.writelines(data)
"==========================================="
def deleteProject(chosenusr):
    title = input("enter your project title: ")
    file = open("AllProjects.txt", 'r')
    data = file.readlines()
    index = 0
    for i in data:
        d = i.split(":")
        if (d[2] == title and d[0] == chosenusr):
            del data[index]
        index += 1
    file = open("AllProjects.txt", 'w')
    file.writelines(data)
"==========================================="