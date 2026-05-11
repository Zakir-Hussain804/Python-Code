# Topice of For Loop 
var  ="hello"
for l in var :
    print(l)


# check o include ya hai ya is string  use karta hai in operator

if "u" in var :
    print("include the a o")
else :
 print("not inculde ")
#sum of 1 to 10
sum=0
for i in range(0,10):
    sum+=i
print(sum)
#Break
for k in range(8):
   if k==3:
      break
   print(k)
#continu
for l in range(1,10):
   if l==4:
      continue
   print(l)

# count the vowel 
word='Pakistain'

count=0
for ch in word:
   if ch=="a" or ch=='e' or ch=='i' or ch=='o' or ch=='u':
      print(ch)
      count +=1
   print(count)