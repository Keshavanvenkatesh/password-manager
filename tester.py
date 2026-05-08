import pickle
from user_class import users

# with open("user_data.txt","wb") as f:
#     a=[]
#     pickle.dump(a,f)
#     f.close()

with open("user_data.txt","rb") as f:
    a=pickle.load(f)
    for user in a:
        print(user.username,user.password,user.passwords)