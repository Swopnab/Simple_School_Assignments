#sum of 2 integers

a = int(input("enter a number"))
b = int(input("enter a number"))
c = a + b
print(c)

#sum,product,difference and quotient of 2 integers
a = int(input("enter the greater number "))
b = int(input("enter the another number "))
c = a + b
d = a * b
e = a - b
f = a // b
print(f"the sum is {c} \nthe product is {d} \nthe difference is {e} \nthe quotient is {f}")

#square and square root of any number
a = int(input("enter a number "))
b = a ** 2
c = a ** (1. / 2.)
print(f"the square is {b} \nthe square root is {c}")


#cube and cube root of any number
a = int(input("enter a number "))
b = a ** 3
c = a ** (1. / 3.)
print(f"the cube is {b} \nthe cube root is {c}")


#area and perimeter of a rectangle
a = int(input("enter length "))
b = int(input("enter breadth "))
print(f"the area is {a * b} \nthe perimeter is {2 * (a + b)}")


#volume of a sphere
a = int(input("enter radius "))
print(f"the volume is {(4 / 3) * (3.14) * (a ** 3)}")


#area and circumference of a circle
r = int(input("enter radius "))
print(f"the area is {3.14 * r ** 2} \nthe circumference is {2 * 3.14 * r}")


#distance between two points using distance formula
a, b = input("enter the coordinates of a point ").split()
c, d = input("enter the coordinates of another point ").split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
print(f"the distance between the point is {((c - a) ** 2 + (d - b) ** 2) ** 1 / 2}")


#roots of a quadratic equation
import cmath

print('ax2 + bx + c=0')
x, y, z = input("enter the vaue of a ,b and c from the equation").split()
a = float(x)
b = float(y)
c = float(z)
d = (b ** 2) - (4 * a * c)
x1 = (-b - cmath.sqrt(d)) / (2 * a)
x2 = (-b + cmath.sqrt(d)) / (2 * a)
print(f"the solution are {x1} and {x2}")


#simple interest and amount of any principal amount
p = int(input("enter principal "))
t = int(input("enter time "))
r = int(input("enter rate of interest "))
si = (p * t * r) / 100
sa = (si + p)
print(f"the simple interest is {si} \nthe amount is {sa}")


#area of a triangle using Heron’s formula
a = int(input("enter first side of triangle "))
b = int(input("enter second side of triangle  "))
c = int(input("enter third side of triangle  "))
s = (a + b + c) / 2
ar = (((s * (s - a) * (s - b) * (s - c)) / (1. / 2.)))
print(f"the area of triangle is {ar} ")


#temperature in Celsius and convert into Fahrenheit
c = int(input("enter celsius "))
f = ((c / (5 / 9)) + 32)
print(f"the output is {f} ")


#area of 4 walls.[A=2H(L+B)]
l = int(input("enter lenght "))
b = int(input("enter breadth  "))
h = int(input("enter height  "))
ar = (2 * h) * (l + b)
print(f"the area if 4 walls {ar}")


# area of 4 walls and ceiling.[A=2H(L+B)+LB]
l = int(input("enter lenght "))
b = int(input("enter breadth  "))
h = int(input("enter height  "))
ar = ((2 * h) * (l + b) + (l * b))
print(f"the area if 4 walls {ar}")


#volume of hemisphere.[V=(2/3)πR3]
r = int(input("enter radius "))
v = ((2 / 3) * (3.14) * (r ** 3))
print(f"the volume is {v}")


#Nepali currency into Dollar and Indian Currency
nrs = int(input("enter currency in nepali "))
usd = nrs / 115
ic = nrs * 1.6
print(f"the currency in us dollar is{usd} \nthe the currency in indian currency is {ic}")


#cost price and selling price and calculate profit. [P=SP-CP]
cp = int(input("enter cost price "))
sp = int(input("enter selling price "))
p = sp - cp
print(f"the profit is {p}")


#cost price and selling price and calculate profit percentage. [PP=((SP-CP)/CP)*100]
cp = int(input("enter cost price "))
sp = int(input("enter selling price "))
pp = ((sp - cp) / cp) * 100
print(f"the profit percentage is {pp}")


#cost price and selling price and calculate loss percentage.[LP=((CP-SP)/CP)*100]
percentage.[LP = ((CP - SP) / CP) * 100]
cp = int(input("enter cost price "))
sp = int(input("enter selling price "))
lp = ((cp - sp) / cp) * 100
print(f"the loss percent is {lp}")


# distance.[S=UT+1/2(AT2)]
u = int(input("enter initial velocity "))
a = int(input("enter acceleration "))
t = int(input("enter time taken "))
s = ((u * t) + (1. / 2.) * (a * (t ** 2)))
print(f"the distance is {s}")


#potential energy of body. [PE=MGH where G=9.8]
G = 9.8]
m = int(input("enter mass of the body "))
g = 9.8
h = int(input("enter height "))
pe = m * g * h
print(f"the potential energy is {pe}")


# selling price where profit percentage and cost price is given. [SP=CP(100+PROFIT%)/100]
cp = int(input("enter cost price "))
pp = int(input("enter profit percent "))
sp = (cp * (100 + pp) / 100)
print(f"the selling price is {sp} ")


#time in seconds and convert into hours, minutes and seconds
a = int(input("enter time in seconds "))
h = a // 3600
m = ((a // 60) - (h * 60))
s = a - ((h * 60 * 60) + (m * 60))
print(f"{h} hours \n {m} minutes \n {s} seconds ")


#time in hours and convert into second and minutes
h = float(input("enter time in hours "))
m = h * 60
s = h * 3600
print(f"the conversion on minutes is {m} \n and in seconds is {s}")


#distance in kilometers and convert into metres and centimeters
k = float(input("enter distance in kilometer "))
m = k * 1000
c = m * 100
print(f"the conversion in meter is {m} \n and in centimeter is {c}")


#distance in meters and convert into kilometers and centimeters
m = float(input("enter distance in meter "))
k = m / 1000
c = m * 100
print(f"the conversion in kilometer is {k} \n and in centimeter is {c}")
