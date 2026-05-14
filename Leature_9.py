#Tuple is collection which order unchangeable
tup=(1,23,4,55,1,)
print(tup)
print('type =',type(tup))
tup2=(4) #single value of not a tuple 
print('type =',type(tup2))
#tup[3]=3 not allow
print(tup[3])
#Slicing a Tuple
print(tup[1:4])

#sum all value in the tuple
sum=0
for va in tup:
    sum +=va
print("Tuple all value of Sum {}".format(sum))

#updata tuple  or change value of tuble 
tup3=("apple", "banana", "cherry")
print("before tup3 =",tup3)
#tuple convert to list
x=list(tup3)
x[2]="kiwi"
#list convert to tuple
tup3=tuple(x)
print("after tup3 =",tup3)
#########################################################################
tuple1=("ali","hussain","azam","usman")
print("tuple =",tuple1)
#add new  value a last index
#first tuple convert to list 
list1=list(tuple1)
#use the append method
list1.append("Zakir")
#second list convet to tuple 
tuple1=tuple(list1)
print("add new value in last index = {}".format(tuple1))
#use the while loop
i=0
while i<len(tuple1):
    print(tuple1[i])
    i+=1

#tuple Method 
num=(1,234,21,1,3,4,5,6,7,844,3,2,3,)
print("count of 1 = ",num.count(1))
print("find the index of =",num.index(6))