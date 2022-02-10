class Ejercicios:
    def __init__(self,msg="Fin del Programa"):
        self.menj=msg
    def divisores(self,num):  
        cont = 1    
        while cont < num: 
            rec = num % cont   
            if rec == 0:
                print(cont)  
            cont = cont +1
        print(self.menj)  
   
    def divisoresReturn(self,num):  
        cont = 1
        divisores = []    
        while cont < num: 
            rec = num % cont   
            if rec == 0:
                divisores.append(cont)  
            cont = cont +1
        return divisores  
  
# crear la funcion o metodo(clase)  
# def divisores1():  
#   num = int(input("ingrese numero"))
#   cont = 1    
#   while cont < num: 
#     rec = num % cont   
#     if rec == 0:
#         print(cont)  
#     cont = cont +1
#   print("fin del programa")



#divisores1()
# numero = int(input("ingrese numero: "))
# divisores(numero)
# divisores(7)

ejer = Ejercicios()
# lista = [4,3,5]
# for nume in lista:
#     ejer.divisores(nume)
list = ejer.divisoresReturn(12)
print(list)
for n in list:
    print(n)