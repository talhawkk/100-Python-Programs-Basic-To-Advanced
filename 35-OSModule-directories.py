import os
for i in range(0,101):
    os.mkdir(f"day/day{i}")
os.mkdir("day/day1/talha")

p=os.listdir("day")
for i in p:
    print(i)
    print(os.listdir(f"day/{i}"))