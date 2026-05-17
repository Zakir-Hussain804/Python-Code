arr=[1,23,4,7,8,3,2]
idx=0
n=2
sum=0
# n multipe of this array
for i in arr:
    print('multipe of 2',i*n)
  
# total sum of this array
for i in arr:
     sum +=i
    
print("sum Number of this array",sum)
# find max number of this array
max=0
for i in arr:
     if i>max:
        max =i
print("max Number of this array =",max)