# topice List mutable sequence value
# List is used to store the multiple value in single variable
marks=[89,66,77,90,66,43,22,11]
print(marks)
print("Length Marks List =",len(marks))
print('the value of this index marks[3]=',marks[3])
marks[3]=55
print("print marks List use a for ")
print('replace the value of this index marks[3]',marks[3])
for ch in marks:
    print(ch)

# # Slicing
print(marks[2:4:])
print(marks[2:len(marks)])
print(marks[1:-1])

# List Method 
List1=[2,333,45,67,1,6,]
print("List1 = {}".format(List1))

#List .append add the value of end
List1.append(33)
print("add new value for last index use append(33)  = {}".format(List1))
List1.insert(1,0) #replace value
print("replace value for index num use insert(1,0)  = {}".format(List1))
List1.sort()
print("Sort of a List  = {}".format(List1))
List1.reverse()
print("reverse of a List  = {}".format(List1))