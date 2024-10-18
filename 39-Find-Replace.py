print("******welcome******".center(110))
filename=input("enter the file name with extension also place the file in same directory\n")
word=input("\nenter the word or group of word you want to search in file\n")
print(filename,word)
f=open(filename,"r")
no = 1
lines = f.readlines()  # Read all lines at once
found = False

for line in lines:
    if word in line:
        print(f"*found* in line {no}")
        found = True
    no += 1

if not found:
    print(f"'{word}' not found in the file.")
f.seek(0)
com=int(input("Select please.\n 1.replace\n 2.delete\n"))
read=f.read()
if com==1:
    new=input("enter new word\n")
    newfile=read.replace(word,new)
    f.close()
    f=open(filename,"w")
    f.write(newfile)
    print("Changes you made, have been saved to your file")
elif com==2:
    new=input("enter new word\n")
    newfile=read.replace(word,"")
    f.close()
    f=open(filename,"w")
    f.write(newfile)
    print("Changes you made, have been saved to your file")

else:
    print("enter valid command (1 or 2)")