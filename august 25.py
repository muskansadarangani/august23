Assignment 25 August
Ans : 1 
#password validation
c,s,u,d =0,0,0,0
n=input("enter the password:")
capitalletters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallletters="rstuvwxyz"
specialchar="$@#"
digits="0123456789"
if(len(n)>=6,15):
  for i in n:
    if(i in capitalletters):
       c=c+1
    if(i in smallletters):
       s=s+1
    if(i in specialchar):
       u=u+1
    if(i in digits):
       d=d+1
if(c>=1 and s>=1 and u>=1 and d>=1):
   print("valid password")
else:
   print("invalid password")

Ans : 2 
# print *
for i in range(4,0,-1):
  for k in range(1,5,-i):
      print(" ",end="")
  for j in range(1,i-1):
      print("*",end="")
  print(" ")

Ans : 3
# print ABC
for i in range(65,68):


  for j in range(65,i+1):
        print(chr(j),end="")
        i=i+1

   print("")

Ans : 4 
#print ABCDEFGHI
n=65
for i in range(0,4):

  for j in range(0,i+1):
        print(chr(n),end=" ")
        n=n+1

  print(" ")

Ans : 5 
# print 123
for i in range(1,5):

    for j in range(1,i+1):
        print(j,end="")

    print("")
Ans : 6
# print 123456
n=1
for i in range(1,4):


  for j in range(1,i+1):
        print(n,end="")
        n=n+1

  print("")
Ans : 7 
#find unique word from a string
x=input("enter the string: ").split(' ')
list=[]
for i in x:
  if i not in list:
      list.append(i)
print(list)