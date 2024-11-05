import re

def checker(password):
    score=0
    length=len(password)>=8
    uppercase=re.search(r'[A-Z]',password)
    lowercase=re.search(r'[a-z]',password)
    number=re.search(r'[0-9]',password)
    special=re.search(r'[!@#$%^&*()?><]',password)

    if length:
        score+=1
    if uppercase:
        score+=1
    if lowercase:
        score+=1
    if number:
        score+=1
    if special:
        score+=1

    if score == 5:
        print("Password Strength : Strong")
    elif score>3 and score<5:
        print("Password Strength : moderate")
    else:
        print("Password Strength : weak")
    
password=input("enter password : ")
checker(password)