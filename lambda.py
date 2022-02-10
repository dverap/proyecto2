# funcion = lambda parametro_1,parametro_2,etc : logica
def mul_10(num):
    return num*10

def sumar(datos):
    acu=0
    for num in datos:
        acu += num
    return acu
    
mul10 = lambda numero: numero*10

suma = lambda *datos: sumar(datos)
print(suma(2,4,6))

resp1 = mul10(5)
resp2 = mul_10(5)
print(resp1,resp2)

def potencia(base,exponente):
    return pow(base,exponente)
exp = 2                         
potencias = lambda numero,exponente : potencia(numero,exponente+1)
print(potencias(2,4))
