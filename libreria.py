import math

def Suma (a,b):
    return (a[0]+b[0], a[1]+b[1])

def prettyPrinting (a):
    print (a[0],"+",a[1],"i")

def resta (a,b):
    return (a[0] -b[0], a[1]- b[1])

def mult (a,b):
    return ((a[0]*b[0])+((-1)*a[1]*b[1]), (a[0]*b[1])+(a[1]*b[0]))

def div (a,b):
    return (((a[0]*b[0])+(a[1]*b[1]))/((b[0]*b[0])+(b[1]*b[1])), ((a[1]*b[0])- (a[0]*b[1]))/ ((b[0]*b[0])+(b[1]*b[1])))

def conjug (a):
    return (a[0], -(a[1]))

def mod (a,b):
    return ((a**2)+(b**2))**0.5

def pol (a,b):
    return (mod (a,b), math.degrees(math.atan2(b,a)))

def fase (a,b):
    return (math.degrees(math.atan2(b,a)))


            
