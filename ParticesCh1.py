#ask the user to enter two integers and one float. Convert them all to floats and print their average.
num1=int(input("Enter the any Interger"))
num2=int(input("Enter the any Interger"))
num3=float(input("Enter the any float"))
#covert int to float
num1=float(num1)
num2=float(num2)
# calculate average
AverageResult=(num1+num2+num3)/3
# print result
print("Result Average :" ,AverageResult)

# Write a program to  swap values of two numbers entered by the user
a=10
b=20
print("Before  \n a=", a,"b=",b )
temp=a
a=b
b=temp

print("After  \n a=", a,"b=",b )