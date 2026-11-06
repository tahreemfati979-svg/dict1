email = "tahreemfati@gmail.com"
password = "2914"

while True :
    user_email = input ("enter your e_mail:")
    user_password = input("enter password:")
    if (email == user_email):
        print("correct email")
    else :
        print ("not valid")
    if (password == user_password):
        print ("correct password")
    else:
        print ("incorrect password")

    if (email == user_email and password == user_password):
        print ("access")
        break 
    print("not valid") 



