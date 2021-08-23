#input 10 numbers in a single dimension array and display them
from array import *
a= array('i',[])
n=int(input("enter number of digits:"))
for i in range(n):
 b=int(input("enter a number:"))
 a.append(b)
for i in range(len(a)):
 print(a[i])


#input 10 numbers and count the number of positive and negative number
from array import *
a=array('i',[])
e=0
o=0
for i in range(10):
 c=int(input("enter a number :"))
 a.append(c)
print(a)
for i in range(len(a)):
 if a[i]>0:
   e+=1
 else:
   if a[i]<0:
     o+=1
print("total positive numbers=",e)
print("total negative numbers=",o)


#find sum and average of 10 numbers
from array import *
a=array('i',[])
d=0
b=0
for i in range(10):
 c=int(input("enter a number :"))
 a.append(c)
for i in range(len(a)):
 d+=a[i]
b=d/10
print("sum=",d)
print("average=",b)


#input n numbers and display the even numbers only
from array import *
a=array('i',[])
x=int(input("enter the number of values :"))
for i in range(x):
 c=int(input("enter a number :"))
 a.append(c)
for i in range(len(a)):
 if a[i]%2==0:
   print(f'{a[i]} is an even number')


#input n numbers and find the sum and average of even and odd numbers
from array import *
a=array('i',[])
avg=0
Avg=0
o=0
O=0
e=0
E=0
x=int(input("enter the number of values :"))
for i in range(x):
c=int(input("enter a number :"))
a.append(c)
for i in range(len(a)):
if a[i]%2==0:
  e+=a[i]
  E+=1
else:
  o+=a[i]
  O+=1
avg=e/E
Avg=o/O
print(f'sum of even numbers is ={e} and the average is {avg} ')
print(f'sum of odd numbers is ={o} and the average is {Avg} ')


#enter n numbers and display the largest and smallest among them
from array import *
a=array('i',[])
large=0
x=int(input("enter the number of values :"))
for i in range(x):
 c=int(input("enter a number :"))
 a.append(c)
small=c
for i in range(len(a)):
 if a[i]>large:
   large=a[i]
 else:
   if a[i]<small:
     small=a[i]
print(f'largest number={large} and smallest number={small}')


#enter n numbers and sort them in ascending order
from array import *
a=array('i',[])
d=0
n=int(input('enter the number of values :'))
j=0
for i in range(n):
 c=int(input("enter a number :"))
 a.append(c)
for i in range(0,n):
 for j in range(i+1,n):
     if (a[i]>(a[j])):
       d=a[i]
       a[i]=a[j]
       a[j]=d
for i in range(n):
 print(a[i]


#enter n numbers and sort then in descending order
from array import
a=array('i',[])
d=0
n=int(input('enter the number of values :'))
j=0
for i in range(n):
 c=int(input("enter a number :"))
 a.append(c)
for i in range(0,n):
 for j in range(i+1,n):
     if (a[i]<(a[j])):
       d=a[i]
       a[i]=a[j]
       a[j]=d
for i in range(n):
 print(a[i])


#input a 2D array of order 2 x 3 and display in matrix form
a=[[0, 0, 0]
 ,[0, 0, 0]]
for i in range (len(a)):
 for j in range (len(a[0])):
   print(f'enter the value for row{i+1} and column{j+1}')
   a[i][j]=int(input())
for x in a: print(x)


#input a 2D array of order 2 x 3 and display its transpose
a=[[0, 0, 0]
 ,[0, 0, 0]]

for i in range (len(a)):
 for j in range (len(a[0])):
   print(f'enter the value for row{i+1} and column{j+1}')
   a[i][j]=int(input())
result = [[0,0],
        [0,0],
        [0,0]]


for i in range(len(a)):

  for j in range(len(a[0])):
      result[j][i] = a[i][j]

for r in result:
  print(r)


#input 2 matrices of order 3 x 3, add them and display the resultant matrix
a=[[0, 0, 0]
 ,[0, 0, 0]]
b=[[0, 0, 0]
 ,[0, 0, 0]]
for i in range (len(a)):
 for j in range (len(a[0])):
   print(f'enter the value for row{i+1} and column{j+1}')
   a[i][j]=int(input())
result = [[0, 0, 0],
        [0, 0, 0]]
for x in a: print(x)

for i in range (len(b)):
 for j in range (len(a[0])):
   print(f'enter the value for row{i+1} and column{j+1}')
   b[i][j]=int(input())

for i in range(len(a)):

  for j in range(len(a[0])):
      result[i][j] = a[i][j] + b[i][j]
for x in b: print(x)
for r in result:
  print(r)