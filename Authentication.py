import uuid
from project import ProjectMenu

def Options():
    x = input("Please Enter Your option: ")
    if (x.isalpha() or not x ["r", "l"]):
        return (x)
    return Options()
"======================================="
def FName():
    x = input("Please Enter your First Name : ")
    if (x.isalpha() or not x):
        return x
    else:
        return FName()


def LName():
    x = input("Please Enter your Lasr Name: ")
    if (x.isalpha() or not x):
        return x
    else:
        return LName()

"======================================="
import re
def Youremail():
    x = input("Please Enter  your e-mail : ")
    if emailcheck(x):
        return x
    else:
        return Youremail()


def emailcheck(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (re.fullmatch(regex, email)):
        return True
    else:
        return False
"======================================="
def Password():
    x = input("Please Enter Password : ")
    if  not x or x.isspace():
        return Password()
    else:
        Confirmed_password = PasswordConfirm(x)
        if Confirmed_password:
            return x
        else:
            return Password()


def PasswordConfirm(Password):
    x = input("Re write your password : ")
    if (Password == x or not x):
        return True
    else:
        return False

"==================================="
def PhoneNumber():
    x = input("Please Enter Your Phone with egypt key : ")
    if (re.match(r"^20[0-1]\d{1,10}$", x)):
        return x
    else:
        return PhoneNumber()

def NewUser(info):
    file = open('userinfo.txt', 'a')
    file.writelines(info)
    file.close
"======================================="
def Register():
    FirstName = FName()
    LastName = LName()
    Email = Youremail()
    password = Password()
    phone = PhoneNumber()
    id =str(uuid.uuid4())

    #round(time.time())
    info = f"{id}:{Email}:{password}:{FirstName}:{LastName}:{phone}\n"
    NewUser(info)

def ifexist(email,password):
    file = open("userinfo.txt", "r")
    info = file.readlines()
    for i in info:
        f = i.split(":")
        if (f[1] == email and f[2] == password):
            return f[0]
        else:
            print("wrong info")
            return Login()
"======================================="
def Login():
    email=input("E-mail : ")
    password=input("Password: ")
    chosenusr=ifexist(email,password)
    ProjectMenu(chosenusr)
"======================================="
def mainmenu():
    print("""choose an option 
    r ===> Register
    l ===> Login """)
    choice = Options()
    if (choice == "r"):
        Register()
    elif (choice == "l"):
        Login()
