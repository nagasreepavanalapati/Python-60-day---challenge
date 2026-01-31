studentID=input("Enter student ID:")
emailID=input("Enter email ID:")
password=input("Enter password:")
referralcode=input("Enter referral code:")
if  (studentID[0:3]=="CSE" and
        studentID[3]=="-" and
        studentID[4:].isdigit()):
    if (emailID.count("@")==1 and
            emailID.count(".")==1 and
            emailID[0]!="@" and
            emailID[-1]!="@" and
            emailID[-4:]==".edu"):
        if ((len(password))>=8 and
        "A"<= password[0] <="Z" and
        ("0" in password or "1" in password or
         "2" in password or
         "3"in password or
         "4" in password or
         "5" in password or
         "6" in password or
         "7" in password or
         "8" in password or
         "9" in password)):
                if (referralcode[0:3]=="REF" and
                        referralcode[3:5].isdigit() and
                        referralcode[-1]=="@"):
                                print("APPROVED")
                else: print("REJECTED")
    else:print("REJECTED")
else:print("REJECTED")



