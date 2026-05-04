#Tyoe Converstion
# 2 two type of type converstion 
#(A) Implicit Type Conversion
#Python khud automatically convert karta hai
#Jab different types use hote hain
x=10
y=3.2
print(float(x)) # int convert to float
print(type(x)) # float 
print (str(x)) #int covert to String 
print(type(x)) #String
print(int(y))  # float  convert to int 
z="100"
print(int(z)) #String convert to int 
print(type(z)) #int 

#userInput Python
Name=input("Enter the Your Name :")
print(type(Name))
print("WellCome To :",Name)

number=input("Enter Number")
print(type(number)) #string
number2=int(input("Enter Number"))
print(type(number)) #int

#average two number in user input 
a=float(input("Enter the your Number 1 :"))
b=float(input("Enter the your Number 2 :"))
avarage=(a+b)/2
print(avarage)