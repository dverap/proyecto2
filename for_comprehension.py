#lista = [10,12,13,20]
# for elemento in lista:
#     print(elemento*2,end=" ")
# print()    
# print("invertida")
# for elemento in reversed(lista):
#     print(elemento,end=" ")
# print()    
# lon = len(lista) - 1
# for pos in range(len(lista)): 
#     if pos % 2 == 0 and pos !=0:
#         print(pos,lista[pos]*3,end=" ")
# print("\n Presenta la lista invertida")
# for pos in range(lon,-1,-1): 
#         print(lista[pos],end=" ")
# print()

# print("numeros del 0 al 9")
# for numero in range(10): #0,1,2,3,4,5,6,7,8,9
#     print(numero,end=" ")
# print("\nNumeros del 1 al 10")
# for numero in range(1,11): #0,1,2,3,4,5,6,7,8,9
#     print(numero,end=" ")
# print("\nNumeros pares del 2 al 20")
# for numero in range(2,22,2): 
#     print(numero,end=" ")
# print("\nNumeros multiplos de 3 del 30 al 3")
# for numero in range(30,0,-3): 
#     print(numero,end=" ")
# print("\nNumeros multiplos de 3 del 30 al 3")
# recorre toda la coleccion y en cada recorrido 
# retorna la posicion y el valor del elemento 
# lista = (10,12,13,20)
# for pos,elemento in enumerate(lista): 
#     #if pos % 2 == 0 and pos !=0:
#         print(pos,elemento*3,end=" ")

# nombres = ["Ana","Dan","Jose"]
# print(nombres) 
# nombres.append("Yady")
# print(nombres) 
# nombres.insert(1,"Juan")    
# print(nombres) 
# #del nombres
# del nombres[1]
# print(nombres) 
# nombres.append("Juan") # push = pila
# print(nombres) 
# nombres.pop()
# print(nombres)
# cadena = "clase de estructura"
#       #   0123456789
# print()
# for car in cadena:
#     print(car,end=" ")
# print()    
# for pos in range(len(cadena)):
#     print(pos,cadena[pos],end=" ")
# print()
# list1 = ['1','2','3','4']  
# cad = "-".join(list1) 
# print("join ",cad) 
# lista2 = cad.split("-")
# print("split ",lista2) 
# print()  
# lista = [10,12,13,20]
# def multiplo(valor,mul):
#     return valor*mul
 
# nueva_lista = [ multiplo(i,3) for i in lista ]
# print("comprehension",nueva_lista)
# nueva_lista2=[]
# for i in lista:
#     if i%2 == 0:
#         nueva_lista2.append(i)
#print("Sin comprehension",nueva_lista2)

# print("*"*20,"Diccionario","*"*20)
# diccionario = {"nombre":"Dan", "saludo":"Hola como estas",1:"Ok"}
# diccionario["edad"]=52
# print(diccionario,diccionario["nombre"])
# diccionario["nombre"]="Yady"
# print(diccionario,diccionario["nombre"])
# listas = [(2,3,4),["a","e"],{"nom":"xxx"},"Daniel",20,True]
# for elem in listas:
#     print(elem)
  
# listas2 = [(2,3,4),(1,5,7,8),(8,9)]
# for list in listas2:
#     print ("\n",list)
#     for ele in list:
#         print(ele,end=" ")
        
# items = diccionario.items()
# #print(items)
# nom = diccionario["nombre"]
# sal = diccionario["saludo"]
# clave y el valor
# for clave,valor in diccionario.items():
#     print("{} --> {} ".format(clave,valor))
# # solo clave
# for clave in diccionario:
#     print("[\"{}\"]".format(clave))
# # solo clave
# print()
# claves = diccionario.keys()
# print(claves)
# for clave in diccionario.keys():
#     print("[{}]".format(clave))
# # solo valores
# for valor in diccionario.values():
#     print("{}".format(valor))
notas = [30,50,40]
#        0   1  2  elemto enteros
#print(notas[0])
alumnos = [{"nombre":"Daniel","nota":30},{"nombre":"Erick","nota":50},{"nombre":"Yady","nota":40}]
#                       0                               1                             2 elementos diccionarios
#print(alumnos[0])
acu=0 
c=0
for alumno in alumnos:
    #print(alumno)
    #print(alumno['nombre'],alumno['nota'])
    acu = acu + alumno["nota"]
    c +=1
#print("Promedio={}".format(acu/len(alumnos)))    
acu = 0
# for alumno in alumnos:
#      for clave,valor in alumno.items():
#         print(clave,valor)  
#         if clave == "nota":
#             acu += valor
# print("Promedio={}".format(acu/len(alumnos)))            

lista = []
for num in range(1,11):
    if num%2 == 0:
       dic = {"Par":num} 
       lista.append(dic)
    else:
       lista.append({"Impar":num})
        
print(lista)
        