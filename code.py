import json
def signup():
        name=input("Enter the name:- ")
        password=input("Enter the password:- ")
        list=[]
        dic={}
        d={}
        d["name"]=name
        d["password"]=password
        list.append(d)
        s={}
        s["descriprtion"]="Hello my name is", name ,"and I Love travelling!!"
        dic["user"]=list
        d["profile"]=s
        with open("Signup and Login.text","w") as f:
            json.dump(dic,f,indent=8)  
        if len(password)>8:
            if "@" in password or "#" in password or "$" in password:
                if "0"  not in password or "1"  not in password or "2"  not in password or "3"  not in password or "4" not in password or "5" not in password or "6" not in password or "7"not in password or "8"not in password or "9"not in password:
                    password2=input("Re-enter the password again:- ")
                    if password==password2:
                        DOB=int(input("Enter your Date of Birth:- "))
                        Gender=input("Enter your gender f/m:-  ")
                        Hobbies= input("Enter your hobbies:-  ")
                        d["DOB"]=DOB
                        d["Hobby"]=Hobbies
                        d["Gender"]=Gender
                        f=open("Signup and Login.text","a")
                        f.write(name+","+password+"\n")
                        print("Congrats!",name,"Successful") 
                                                    
                    else:
                        print("Both  Password are not same")
                else:
                    print("Password should contain  at least one number")
            else:
                 print("Password should contain at least one special character")
        else:
            print(" Password is too short")
user=input("Signup or Login:- ")
if user=="Signup":
    signup()
elif user=="Login":
    signup()
        




 
    
        
           