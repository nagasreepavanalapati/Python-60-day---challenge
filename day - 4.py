n=int(input("Enter the total number of scores:"))
scores=[0]*n
for i in range(n):
    a =int(input(f"enter the score of {i+1}:"))
    scores[i]=a
low_risk=[]
medium_risk=[]
high_risk=[]
critical_risk=[]
invalid=0
for i in range(n):
    if scores[i]<0:
        invalid+=1
    elif 0<=scores[i]<=30:
        low_risk+=[scores[i]]
    elif 31<=scores[i]<=60:
        medium_risk+=[scores[i]]
    elif 61<=scores[i]<=100:
        high_risk+=[scores[i]]
    else: critical_risk+=[scores[i]]
D=int(input("Register Digit(D): "))
print("Low Risk:",low_risk)
print("Medium Risk:",medium_risk)
print("High Risk:",high_risk)
print("Critical Risk:",critical_risk)
print("After personalized Filtering:")
removed=0
if D%2==0:
    removed = len(low_risk)
    low_risk=[]
else:
     removed=len(critical_risk)
     critical_risk=[]
print("Low Risk:",low_risk)
print("Medium Risk:",medium_risk)
print("High Risk:",high_risk)
print("Critical Risk:",critical_risk)

print("Total valid entries:",n-invalid)
print("Ignored Entries:",invalid)
print("Removed Due to Personalization:",removed)





