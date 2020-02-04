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

def addvect (a,b):
    matriz = [[],[]]
    for i in range (0,len (a)):
        matriz = suma (a[i],b[i])
        prettyPrinting (matriz)

def men (a):
    return (-(a[0]),-(a[1]))

def inverse (a):
    matriz= [[]]
    for i in range (0,len(a)):
        matriz = (men(a[i]))
        prettyPrinting (matriz)

def multi (a,b):
    return (a*b[0],a*b[1])


def escal (a,b):
    matriz= [[],[]]
    for i in range (0,len(a)):
           matriz= multi(b,(a[i]))
           prettyPrinting (matriz)
    
def addmat (a,b):
    matriz= [[[],[]],[[],[]]]
    res= [[[],[]],[[],[]]]
    for i in range (0,len(a)):
        for j in range (0,len(a)):
            matriz = suma (a[i][j],b[i][j])
            res[i][j]= matriz
            print (res)

def invmat (a):
    matriz: [[[],[]],[[],[]]]
    for i in range (0,len (a)):
        for j in range (0, len (a)):
            matriz = men (a[i][j])
            prettyPrinting(matriz)

def mult_escal (b,a):
    matriz: [[[],[]],[[],[]]]
    for i in range (0,len (b)):
        for j in range (0, len (b)):
            matriz= (multi(a,(b[i][j])))
            prettyPrinting (matriz)

def trans (a):
    matriz: [[[],[]],[[],[]]]
    for i in range (0,len (a)):
        for j in range (0, len (a)):
            matriz = a[j][i]
            prettyPrinting (matriz)
def conmat (a):
    matriz: [[[],[]],[[],[]]]
    for i in range (0,len (a)):
        for j in range (0, len (a)):
            matriz = conjug (a[i][j])
            prettyPrinting (matriz)

def adjunt (a):
    matriz: [[[],[]],[[],[]]]
    for i in range (0,len (a)):
        for j in range (0, len (a)):
            matriz = conjug (a[j][i])
            prettyPrinting (matriz)
            
