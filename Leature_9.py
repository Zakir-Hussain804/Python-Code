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
