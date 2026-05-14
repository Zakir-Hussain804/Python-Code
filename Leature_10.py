#Dictionaries use store a multipe value in key pair

studentInfo={
    'Fname':'Zakir Hussain',
     'Semester':7,
     "Subject":["P&DC","HCI","DS"],
     "MisId":39300,
}
print("Type of =",type(studentInfo))
#print one value
print("Fname = ",studentInfo["Fname"])
#change value
studentInfo["Fname"]="Zakir Ali"
print(" Change Fname = ",studentInfo["Fname"])