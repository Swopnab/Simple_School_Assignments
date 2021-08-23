#input any number and display the factors.
a=int(input("enter a number :"))
b=a
while a>0:
if b%a==0:
  print(a)
a-=1


#input any number and find sum of factors
a = int(input("enter a number :"))
b = a
c = 0
while a > 0:
  if b % a == 0:
    c += a

a -= 1
print(c)


#input any number and display the factorial
a=int(input("enter a number :"))
b=1
c=1
while b<=a:
 c=c*b
 b+=1
print (c)


#input any number and display the multiplication table
a=int(input("enter a number :"))
b=1
while b<=a:
 c=a*b
 print(f"{b} * {a}={c}")
 b+=1


#input any number and reverse it
a = int(input("Enter a number: "))
b = 0
while a > 0:
  c = a % 10
  b = b * 10 + c
  a = a // 10
print("Reverse is ", b)


#input any number and check whether the given no. is palindrome or not
a = input("enter a number ")
b = a[::-1]
if a == b:
  print("it is palendrome")
else:
  print("not palendrome")


#input any number and check whether the given no. is Armstrong or not
a = int(input("Enter a number: "))
c = 0
b = a
while b > 0:
  d = b % 10
  c += d ** 3
  b //= 10

if a == c:
  print("it is an Armstrong number")
else:
  print("it is not an Armstrong number")


#input number and find sum of digits
a = int(input("Enter a number: "))
c=0
while a>0:
 b=a%10
 a=a//10
 c+=b
print(c)


#input number and find sum of odd digits
a = int(input("Enter a number: "))
c=0
while a>0:
 b=a%10
 a=a//10
 if b%2!=0:
   c+=b
print(c)


#input number and find sum of even digits
a = int(input("Enter a number: "))
c=0
while a>0:
 b=a%10
 a=a//10
 if b%2==0:
   c+=b
print(c)


#input number and find sum of square of digits
a = int(input("Enter a number: "))
c=0
while a>0:
 b=a%10
 a=a//10
 c+=b**2
print(c)


#input number and find sum of square of even digits
a = int(input("Enter a number: "))
c=0
while a>0:
 b=a%10
 a=a//10
 if b%2==0:
   c+=b**2
print(c)


#input number and find sum of square of odd digits
a = int(input("Enter a number: "))
c=0
while a>0:
 b=a%10
 a=a//10
 if b%2!=0:
   c+=b**2
print(c)


#input number and find sum of cube of digits
a = int(input("Enter a number: "))
c=0
while a>0:
 b=a%10
 a=a//10
 c+=b**3
print(c)


#input number and find sum of cube of even digits
a = int(input("Enter a number: "))
c=0
while a>0:
 b=a%10
 a=a//10
 if b%2==0:
   c+=b**3
print(c)


#input number and find sum of cube of odd digits
a = int(input("Enter a number: "))
c=0
while a>0:
b=a%10
a=a//10
if b%2!=0:
  c+=b**3
print(c)


# input number and count total no. of digits
a = int(input("Enter a number: "))
c=0
while a>0:
 c+=1
 a=a//10
print(c)


#input number and count total no. of odd digits
a = int(input("Enter a number: "))
c=0
while a>0:
 if a%2!=0:
   c+=1
 a=a//10
print(c)


#input number and count total no. of even digits
a = int(input("Enter a number: "))
c=0
while a>0:
 if a%2==0:
   c+=1
 a=a//10
print(c)


#input number and check whether the given no. is prime or not
a = int(input("Enter a number: "))
b = a
c = 0
while a > 0:
  if b % a == 0:
    c += 1
  a -= 1

if c > 2:
  print("not prime")
else:
  print("prime")


#input number and check whether the given no. composite or not
a = int(input("Enter a number: "))
b = a
c = 0
while a > 0:
  if b % a == 0:
    c += 1
  a -= 1

if c > 2:
  print("composite")
else:
  print("not composite")


# input number and check whether the given no. is prime or composite
a = int(input("Enter a number: "))
b = a
c = 0
while a > 0:
  if b % a == 0:
    c += 1
  a -= 1

if c > 2:
  print("composite")
else:
  print("prime")


#display all prime numbers from 2 to 100
a=2
b=201
for i in range (a,b):
 if i>1:
   for j in range(2,i):
     if (i %j)==0:
         break
   else:
     print(i)


#enter any 10 numbers and sort in ascending order
b=[]
for i in range(10):
 a=int(input("enter a number :"))
 b.append(a)
 b.sort()
print (b)


#enter any 10 numbers and sort in descending order
b=[]
for i in range(10):
 a=int(input("enter a number :"))
 b.append(a)
 b.sort(reverse=True)
print (b)


#enter any 5 numbers and display its product
b=1
for i in range(5):
 a=int(input("enter a number :"))
 b=b*a
print (b)


#enter any two numbers and display the HCF and LCM
a, b=input("enter the numbers :").split()
a=int(a)
b=int(b)
if a>b:
 c=b
else:
 c=a
for i in range(1,c+1):
#c+1 because python takes (a,b,c,d) a as 0,b as 1 and so on
if a % i == 0 and b % i == 0:
  hcf = i
print(hcf)


#enter any 10 numbers and find the sum of numbers
b=0
for i in range(10):
 a=int(input("enter a number :"))
 b+=a
print(b)


#enter any number and display square of each individual digit
a=int(input("enter a number"))
s=[]
while a>0:
 b=a%10
 s.append(b**2)
 a=a//10
s=s[::-1]
print(s)


#enter any number and display cube of each individual digit
a=int(input("enter a number"))
s=[]
while a>0:
 b=a%10
 s.append(b**3)
 a=a//10
s=s[::-1]
print(s)