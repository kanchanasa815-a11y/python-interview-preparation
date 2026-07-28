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
num=int(input("Enter the number: "))
temp=num
digits=len(str(num))
total=0
while temp>0:
  digit=temp%10
  total+=digit**digits
  temp=temp//10
if total==num:
  print(num,"is an Armstrong Number")
else:
  print(num,"is not an Armstrong number")

#Factorial
num=int(input("Enter the number: "))
fact=1
for i in range(1,num+1):
  fact=fact*i
print("Factorial= ",fact)

#Count Vowel
string=input("Enter the string: ")   or  string=input("Enter the string: ").lower()
count=0                                  count=0                              
for ch in string:                        for ch in string:
  if ch in "aeiouAEIOU":                   if ch in "aeiou":   
    count+=1                                   count+=1
    print(count)                               print(count)

#Remove the duplicate element in the list
number=[2,3,4,2,5,2,4,5]
num=list(set(number))
print(num)

# Preserves original order while removing duplicates
my_list = [4, 2, 2, 1, 4]
unique_list = list(dict.fromkeys(my_list))
print(unique_list)  # [4, 2, 1]
          
          
        
