import User1

name = raw_input("Enter the name:\n")
print(name)
pn = raw_input("Enter the phone number:\n")
valid=0
ut = User.User()
while 1:
    valid = ut.validatePhoneNumber(pn)
    if valid == 1:
        break
    else:
        print("Invalid phone number")
        pn = raw_input("Enter the valid phone number:\n")

pw = raw_input("Enter the password\n")
while 1:
    valid = ut.validatePassword(pw)
    if valid == 1:
        break
    else:
        print("Invalid password")
        pw = raw_input("Enter the password\n")

em = raw_input("Enter the email address\n")
while 1:
    valid = ut.validateEmail(em)
    if valid == 1:
        break
    else:
        print("Invalid email")
        em = raw_input("Enter the email address\n")

ud = User.User(name,pn,pw,em)
ud.displayUserDetails()