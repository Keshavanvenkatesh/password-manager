import pickle

class users:
    
    users={}

    #new user
    def __init__(self,username:str,password:str):
        self.username=username
        self.password=password

        self.passwords={}
        
    #make new password
    def new_password(self,name:str,password:str):
        if name in self.passwords.keys():
            print("this name already exists for a password")
            # show a error popup critcal messagebox
        else:
            self.passwords[name]=password

    def edit_password(self,name:str,new_password:str):

        # no saved passwords
        if self.passwords.keys()==[]:
            # show a error popup critcal messagebox
            pass

        for key in self.passwords.keys():
            if key==name:
                self.passwords[key]=new_password
                return
        # incorrect name 
        # show a error popup critcal messagebox
        print("incorrect name")

    def remove_password(self,name:str):
        if name in self.passwords.keys():

            # info message box asging are you sure if yes remove teh password 

            #if pressed no do nothing
            self.passwords.pop(name)
        else:
            #incorrect name
            # show a error popup critcal messagebox
            print("this name doesnt exists")
    
    def show_all(self):
        print()
        print("PASSWORDS:")
        passwords=""
        for key in self.passwords.keys():
            passwords+=f"{key}\n \t password: {self.passwords[key]}\n"
            print(f"{key},password: {self.passwords[key]}")
        return passwords

# keshavan=users("eightnormal","a")
# yashashwini=users("akshaya","b")

# print(users.users)

# print(keshavan.login("eightnormal","b"))
# keshavan.new_password("email","print")
# keshavan.show_password("email")
# keshavan.edit_password("email","pp")
# keshavan.show_password("email")
# keshavan.new_password("email2","print1")

# keshavan.remove_password("email3")
# keshavan.show_all()