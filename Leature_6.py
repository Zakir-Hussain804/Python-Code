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