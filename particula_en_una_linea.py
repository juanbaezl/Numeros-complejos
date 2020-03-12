import libreria
def probabilidad(ket,posicion):
    a=ket[posicion]
    b=(libreria.mod(a[0],a[1]))**2
    c=(libreria.norma_vect(ket))**2
    d=b/c
    res=round(d*100,2)
    return res
def transitar(ket1,ket2):
    res1=[]
    a=1/(libreria.norma_vect(ket1))
    b=1/(libreria.norma_vect(ket2))
    c=libreria.escal(ket1,a)
    d=libreria.escal(ket2,b)
    res=libreria.interno(d,c)
    num1=round(res[0],2)
    num2=round(res[1],2)
    res1=res1+[num1]
    res1=res1+[num2]
    return res1

