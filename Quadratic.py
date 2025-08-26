import cmath
a=int(input("Enter the co_effiecient of x^2(a):"))
b=int(input("Enter the co_effiecient of x(b):"))
c=int(input("Enter the constant value(c):"))
d=b**2-4*(a)*(c)
root1=(-b+cmath.sqrt(d))/2*a;
root2=(-b-cmath.sqrt(d))/2*a;
print("Roots of quadratic equation are:",root1,root2)

