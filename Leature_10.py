#Dictionaries use store a multipe value in key pair

studentInfo={
    'Fname':'Zakir Hussain',
     'Semester':7,
     "Subject":["P&DC","HCI","DS"],
     "MisId":39300,
}
print("Type of =",type(studentInfo))
#dictionaries convet to list
list1=list(studentInfo)
print(type(list1))
#dictionaries convet to tuple
tuple1=tuple(studentInfo)
print(type(tuple1))
#print one value
print("Fname = ",studentInfo["Fname"])
#change value
studentInfo["Fname"]="Zakir Ali"
print(" Change Fname = ",studentInfo["Fname"])
# print(studentInfo) print all vlaue
for ch in studentInfo:
    print(ch," = ",studentInfo[ch])
# Dictionaries Method 
#d.keys return all the key
key_Student=studentInfo.keys()
print("key =",key_Student)

#d.values retrun all vlaue
value_Student=studentInfo.values()
print("all values = ",value_Student)
# updata all value 
studentInfo.update({
    'city':"isbamabad"
})
print("updata ",studentInfo)