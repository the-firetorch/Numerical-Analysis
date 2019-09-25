import math

def f(x0,h):
 y=y0
 c=1
 m=0
 x=x0
 while x < xn:
  print "f(x",m,",y",m,") =",g(x,y)
  y=y+(h*g(x,y))
  print" "
  print "y",c,"=",y
  x=x+h
  c+=1
  m+=1

 


def g(x,y):
 return (x+(y/x))

x0=input("enter initial value of x i.e x0 = ")
y0=input("enter the  value of y at x0 = ",)
h=input("enter step length")
xn=input("final value of x = ")

f(x0,h)

  
