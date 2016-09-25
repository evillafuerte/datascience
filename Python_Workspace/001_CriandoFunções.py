def Square(x):
    return x*x
    
def Quadratic(x):
    return Square(x)*Square(x)
    
def DoSomething(f, x):
    return f(x)
    
print Square(25)
print Quadratic(25)

def Cube(x):
    return x*x*x
print Cube(4)

print DoSomething(Cube, 6)
print DoSomething(Square, 15)
print DoSomething(Quadratic, 6)
