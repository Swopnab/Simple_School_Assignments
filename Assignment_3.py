#input any string and reverse it
a = str(input("enter a string: "))
b = a[::-1]
print(b)


#input any string and check whether the given string is palindrome or not
a=str(input("enter a string: "))
b=a[::-1]
if a==b:
 print('palindrome')
else:
 print('not palindrome')


#input any string and count total no. of vowels
a=str(input("enter a string: "))
b=0
c=len(a)
for i in range (c):
 if a[i] =='a' or a[i] =='e' or a[i] =='i' or a[i] =='o' or a[i] =='u':
   b=b+1
print(b)


#input any string and display only vowels
a=str(input("enter a string: "))
b=0
c=len(a)
for i in range (c):
if a[i] =='a' or a[i] =='e' or a[i] =='i' or a[i] =='o' or a[i] =='u':
 print(a[i])


#input any string and count total no. of consonants
a=str(input("enter a string: "))
b=0
c=len(a)
for i in range (c):
if a[i] !='a' and a[i] !='e' and a[i] !='i' and a[i] !='o' and a[i] !='u':
   b=b+1
print(b)


#input any string and display only consonants
a=str(input("enter a string: "))
b=0
c=len(a)
for i in range (c):
if a[i] !='a' and a[i] !='e' and a[i] !='i' and a[i] !='o' and a[i] !='u':
 print(a[i])


# input any string and count total no. of vowels and consonants
a=str(input("enter a string: "))
x=0
y=0
c=len(a)
for i in range (c):
 if a[i] =='a' or a[i] =='e' or a[i] =='i' or a[i] =='o' or a[i] =='u':
   x=x+1
 else:
   y=y+1
print(f"total number of vowel {x}")
print(f"total number of consonant {y}")


#input any string and count total no. of vowels , consonants, words and sentences
a=str(input("enter a string: "))
b=0
c=0
d=1
e=0
x=len(a)
for i in range (x):
 if a[i]!='a' and a[i]!='e' and a[i]!='i' and a[i]!='o' and a[i]!='u':
  if a[i]!=" " and a[i]!=".":
   b=b+1
 else:
   c=c+1
 if a[i]==" ":
   d=d+1
 if a[i]==".":
   e=e+1
print(f"total number of consonant: {b}")
print(f"total number of vowel: {c}")
print(f"total number of word: {d}")
print(f"total number of sentence: {e}")

