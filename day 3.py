n = int(input("Enter total number of students: "))
marks = [0]*n
for i in range(n):
    marks[i] = int((input(f"Enter marks of the student {i + 1}: ")))
ch = int(input("Enter your registration numbers last digit: "))
if ch % 2 == 0:
    for i in range(n):
        marks[i]+=2
else:
    for i in range(n):
        marks[i]-=1
count=0
flag=0
print("marks after updation:",marks)
for i in marks:
    if 0<=i<=39:
        print(f"{i}-Fail")
        count+=1
    elif 40<=i<=59:
        print(f"{i}-Average")
    elif 60<=i<=74:
        print(f"{i}-Good")
    elif 75<=i<=89:
        print(f"{i}-Very Good")
    elif 90<=i<=100:
        print(f"{i}-Excellent")
    else:
        print(f"{i}-Invalid")
        flag+=1
print("Total Valid students:",n-flag)
print("Total Failed students:",count)

