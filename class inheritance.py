#Chris Costa
#7/25/21
#Intro to Python Programming COP 4045
#A8
import math

## Create variables
class Shape(object):
  def __init__(self,r):
    self.r=float(r)
class Circle(Shape):
  def __init__(self,r):
    self.r=float(r)
  def area(self):
    self.a=3.1415*pow(self.r, 2)
    return self.a
  def perimeter(self):
    self.p=2*3.1415*self.r
    return self.p
class Polygon(Shape):
  def __init__(self,a,b,c):
    self.a=float(a)
    self.b=float(b)
    self.c=float(c)
class Triangle(Polygon):
  def __init__(self,a,b,c):
    
    self.a=float(a)
    self.b=float(b)
    self.c=float(c)

  def area(self):
    if self.a+self.b>self.c and self.a+self.c>self.b and self.c+self.b>self.a:
      
      self.aa=self.a
      self.bb=self.b
      self.cc=self.c
      self.area=0.25*(math.sqrt((self.aa+self.bb+self.cc)*(-self.aa+self.bb+self.cc)*(self.aa-self.bb+self.cc)*(self.aa+self.bb-self.cc)))
      return self.area
    else:
      self.aa=self.a
      self.bb=self.b
      self.cc=self.c
      return print("Error: Not a valid Triangle")
    
  def perimeter(self):
    self.p=self.aa+self.bb+self.cc
    return self.p
  
class Rectangle(Polygon):
  def __init__(self,l,w):
    self.l=float(l)
    self.w=float(w)
  def area(self):
    self.area=self.l*self.w
    return self.area
  def perimeter(self):
    self.p=self.l+self.l+self.w+self.w
    return self.p

class Pentagon(Polygon):
  def __init__(self,s):
    self.s=float(s)
  def area(self):
    self.ad=math.sqrt(5*(5+(2*math.sqrt(5))))*pow(self.s,2)
    self.a=0.25*self.ad
    return self.a
  def perimeter(self):
    self.p=5*self.s
    #+self.s+self.s+self.s+self.s
    return self.p

class Hexagon(Polygon):
  def __init__(self,s):
    self.s=float(s)
  def area(self):
    self.a=((3*math.sqrt(3))/2)*pow(self.s,2)
    return self.a
  def perimeter(self):
    self.p=6*self.s
    #+self.s+self.s+self.s+self.s+self.s
    return self.p

my_circle = Circle(2) 
# create a circle of radius = 2

my_trianglea = Triangle(3, 1.7, 4.9) 
# attempt to create a triangle with "incorrect" values
# should produce error message

my_triangle = Triangle(3, 7, 4.6) 
# create a triangle passing the length of each side

my_rectangle = Rectangle(3, 4.5) 
# create a rectangle of sides 3 and 4.5

my_pentagon = Pentagon(3) 
# create a pentagon with sides of equal length

my_hexagon = Hexagon(3) 
# create a hexagon with sides of equal length

############################################

## Print area and perimeter for each variable

print("Circle")
print("Area: ", my_circle.area())
print("Perimeter: ", my_circle.perimeter())
print("--------------------------")

print("Triangle")
print("Area: ", my_triangle.area())
print("Perimeter: ", my_triangle.perimeter())
print("--------------------------")

print("Triangle")
print("Area: ", my_trianglea.area())
print("Perimeter: ", my_trianglea.perimeter())
print("--------------------------")

print("Rectangle")
print("Area: ", my_rectangle.area())
print("Perimeter: ", my_rectangle.perimeter())
print("--------------------------")

print("Pentagon")
print("Area: ", my_pentagon.area())
print("Perimeter: ", my_pentagon.perimeter())
print("--------------------------")

print("Hexagon")
print("Area: ", my_hexagon.area())
print("Perimeter: ", my_hexagon.perimeter())
