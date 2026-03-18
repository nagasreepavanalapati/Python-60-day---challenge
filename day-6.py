transactions=[100,200,300,-6,400]
digit = int(input("Enter last digit of register number: "))
category={
    "normal":[],"large":[],"high-risk":[],"invalid":[]
}
for i in transactions:
    if i<=0:
        category["invalid"].append(i)
    elif 1 <= i <= 500:
        category["normal"].append(i)
    elif 501 <= i <= 2000:
        category["large"].append(i)
    else :
        category["high-risk"].append(i)

valid=[i for i in transactions if i>0]

summary =(sum(valid),len(transactions))
if  digit % 2 == 0:
    freqlimit = 5
    spendlimit = 5000
else:
    freqlimit = 4
    spendlimit = 4000

frequent = len(transactions)>freqlimit
largespending = summary[0] > spendlimit
suspicious=len(category["high-risk"])>= 3

if suspicious :
    risk = "High Risk"
elif frequent or largespending:
    risk = "Moderate Risk"
else:
    risk = "Low Risk"
print("\nCategorized Transactions:", category)
print("Total Transaction Value:", summary[0])
print("Number of Transactions:", summary[1])
print("Final Risk:", risk)
