def multiplicar(inicio,*args,**kwargs):
    print(inicio,args,kwargs)
    for valor in args:
        #print(valor)
        inicio += valor
    return inicio    

def multiplicar2(*args,**kwargs):
    #args = list(args)
    lista = []
    print(args,kwargs)
    for valor in args:
        print(valor)
        lista.append(valor)
    print(kwargs["nombre"],kwargs["edad"])
    print(lista)
#  print(multiplicar(4,6,2))    
acu = multiplicar(4,6,2,nombre="Daniel",edad=52)
acu = acu * 2
print(acu)
multiplicar2(1,2,3,4,nombre="Erick",edad=4,estudios="Primaria")    

def listas(*args):
    lista = []
    for datos in args:
        lista.append(datos)
    return lista
nums = (2,4,5,6,7,8)
numeros = listas(2,4,6,8,10)  
print(numeros)  
