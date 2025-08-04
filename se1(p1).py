a=10
b=-30
c=20
d=(b*b)-(4*a*c)
if d>=0:
    r1=(-b+d**0.5)/(2*a)
    r2=(-b-d**0.5)/(2*a)
    print("The real roots are:",r1,r2)
else:
    print("No real roots found")
