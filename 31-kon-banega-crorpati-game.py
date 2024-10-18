name=str(input("enter your name:"))
# print(name)
score=int(0)
q=["who discover america?","how many countries are there on earth?","how many days in one year?","largest country of world?","biggest city of world?"]
a=["columbus","205","365","russia","tokyo"]
s=list()
for x in range(0,5):
    print(f"Question no.{1+x}\n",q[x])
    inp=input()
    s.append(inp)
    if s[x]==a[x]:
        score+=5
        print(f"Correct answer, your score is {score}")
    else:
        print(f"wrong answer, your score is {score}")

print(f"Congratulations {name}, your score is {score}")        
