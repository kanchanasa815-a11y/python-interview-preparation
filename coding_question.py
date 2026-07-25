#Reverse the string
text=input("Enter the string: ")
print(text[::-1])

#check pailandrom
text=input("Enter the string: ")
if text==text[::-1]:
  print("Pailandrom")
else:
  print("Not a pailandrom")

#fibonacci
n=int(input("Enter the number of terms:"))
a=0
b=1
print("fibonacci series:")
for i in range(n):
  print(a,end=" ")
  c=a+b
  b=a
  a=c
#fibonacci using recursion
def fibonacci(n):
  if n<=1:
    return n
  return fibonacci(n-1)+fibonacci(n-2)
item=int(input("Enter the number: "))
for i in range(item):
         print(fibonacci(i),end=" ")

# Prime NUmbers
num=int(input("Enter the number: "))
if num > 1:
    for i in range(2,num):
        if num % i==0:
           print(num,"Is is not a prime number")
          break
    else:
        print(num,"Is is Prime number")
else:
  print(num,"It is not a Prime number")

# Armstrong
num=int(input("Enter the number"))
temp=num
digits=len(str(num))
total=0
while temp>0:
  digit=temp%10
  sum+=digit**digits
  tem=temp//10
if sum==num:
  print(num,"os an Armstrong Number")
else:
  print(num,"is not an Armstrong number")
  

          
          
        
