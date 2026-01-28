name=input("Enter your Full name: ")
EmailId=input("Enter your Email ID: ")
Mobnum=input("Enter your Mobile Number: ")
Age=int(input("Enter your Age: "))
if name.count(" ")>=1 and name[0]!=" " and name[-1]!=" ":
   if EmailId.count("@")!=0 and EmailId.count(".")!=0 and EmailId[0]!="@":
        if len(Mobnum)==10 and Mobnum[0]!='0' and Mobnum.isdigit()==1:
            if Age>=18 and Age<=60:
                print("User Profile is VALID")
            else:print("User Profile is INVALID")
        else:print("User Profile is INVALID")
   else:print("User Profile is INVALID")
else:print("User Profile is INVALID")