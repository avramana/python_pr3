import re
class User:
    def __init__(self,name=None,phoneNumber=None,password=None,email=None):
        self.name = name
        self.phoneNumber = phoneNumber
        self.password = password
        self.email = email

    def displayUserDetails(self):
        print("Name : "+self.name)
        print("PhoneNumber : "+self.phoneNumber)
        print("password : "+self.password)
        print("email : "+self.email)

    def validatePhoneNumber(self,pno):
        #if re.match('((?=.*\\d).{10,})',pno):
        if re.match(r'\d{10}',pno):
            if len(pno) == 10:
                return 1
        return 0

    def validatePassword(self,pw):
        if re.match('((?=.*\\d)(?=.*[a-z])(?=.*[A-Z)(?=.*[$#@%]).{8,})',pw):
            if len(pw)>=8:
                return 1
        return 0

    def validateEmail(self,em):
        if re.match('[^@]+@[^@]+\.[^@]+',em):
            return 1
        return 0
