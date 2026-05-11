def hello():
    print("hello word function")
hello()

def calc_avg(a,b,c):
    average=(a+b+c)/3
    return average
result=calc_avg(22,3,12)
print('average = ',result)
 
#Lambda Function
sum=lambda a,b,c:a+b+c
print("sum = ",sum(33,2,2))


def Factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
var=int(input("Enter the Number"))
print(Factorial(var))