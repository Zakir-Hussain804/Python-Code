#Condition Statement  :if elif else
#Check User Age 
age=int(input("Enter Age :"))
#age=18
if age<13:
    print("Child")
elif age >= 13 and age < 18:
    print("Teenager")
else:
    print("adult")

# Check user Login enter username and password 
userName=input("userName :")
password=input("passoword :")

if (userName=="user" and password=="pass"):
    print("Login SuccessFully")
elif userName !="user":
    print("Wrong userName")
else :
    print("Wrong user and Password")


#  Python Case In Match 
# check user enter color

color=input("Enter Color :") 
match color :
    case "red":
        print("Stop")
    case 'yellow':
        print("ready ")
    case "green":
        print("run")
    case _:
        print('wrond enter color')
