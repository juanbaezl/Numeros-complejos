import math

def suma (a,b):
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
    matriz = len (a)*[([],[])]
    for i in range (0,len (a)):
        matriz[i] = suma (a[i],b[i])
    return(matriz)

def men (a):
    return (-(a[0]),-(a[1]))

def inverse (a):
    matriz =len(a)*[([],[])] 
    i=0
    for i in range (0,len(a)):
        matriz [i] = men(a[i])
    return (matriz)

def multi (a,b):
    
    return (a*b[0],a*b[1])


def escal (a,b):
    matriz = len (a)*[([],[])]
    for i in range (0,len(a)):
           matriz[i] = multi(b,(a[i]))
    return (matriz)
    
def addmat (a,b):
    matriz= len(a)*[len(a)*[([],[])]]
    for i in range (0,len(a)):
        for j in range (0,len(a)):
            matriz[i] = suma (a[i][j],b[i][j])
    return (matriz)

def invmat (a):
    matriz: [[[],[]],[[],[]]]
    for i in range (0,len (a)):
        for j in range (0, len (a)):
            matriz = men (a[i][j])
            print(matriz)

def mult_escal (b,a):
    matriz: [[[],[]],[[],[]]]
    for i in range (0,len (b)):
        for j in range (0, len (b)):
            matriz= (multi(a,(b[i][j])))
            print (matriz)

def trans (a):
    matriz: [[[],[]],[[],[]]]
    for i in range (0,len (a)):
        for j in range (0, len (a)):
            matriz = a[j][i]
            print (matriz)
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
            print (matriz)

matriz= 3*[3*[([],[])]]
d=[(1,2),(1,2),(1,2),(1,2)]
v=[(1,2),(1,2),(1,2),[1,2]]
f=4
print (matriz)
            

