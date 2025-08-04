with open ('input1.txt','r') as f:
    lines=f.readline()
for line in lines:
    a,b,c=map(float,line.strip().split())
    d=(b*b)-(4*a*c)
    print(f"\n Equation:{a}x^2+{b}x+{c}=0")
    if d>=0:
        r1=(-b+d**0.5)/(2*a)
        r2=(-b-d**0.5)/(2*a)
        print("The roots are:",r1,r2)
    else:
        print("No real roots")