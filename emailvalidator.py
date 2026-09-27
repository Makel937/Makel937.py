email = input("Enter email :")
email = email.strip()

if email.lower :
    if email.find("@") :
        print ("Your email is valid")
    else :
        print("This email is not valid")
else :
    print("Use proper capitalization")