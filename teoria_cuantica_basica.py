import libreria
import math
import numpy
def media(matriz,vector):
    bra=libreria.accion(matriz,vector)
    res=libreria.interno(bra,vector)
    return res
def varianza (matriz,vector):
    med=media(matriz,vector)
    un=libreria.matin(len(matriz))
    medmat=libreria.mult_escal(un,med[0])
    medmat1=libreria.invmat(medmat)
    delta=libreria.addmat(matriz,medmat1)
    res=libreria.multimat(delta,delta)
    total=media(res,vector)
    return(total)
