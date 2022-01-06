class Ejercicio:
    def __init_(self):
        pass
    def bitPar(self,binario):
        n1 = int(binario[0])
        n2 = int(binario[1])
        n3 = int(binario[2])
        n4 = int(binario[3])
        cont = n1+n2+n3+n4
        if cont%2 == 0:
            print("bit de paridad es cero")
        else:
            print("bit de paridad es uno")
                    
        
    def bitParidad(self,binario):
        print(binario[0],end=" ")
        print(binario[1],end=" ")
        print(binario[2],end=" ")
        print(binario[3],end=" ")
        cont=0
        if binario[0]=='1':
            cont=cont+1
        if binario[1]=='1':
            cont=cont+1
        if binario[2]=='1':
            cont=cont+1
        if binario[3]=='1':
            cont=cont+1
        print("contador={}".format(cont))
        if cont%2 == 0:
            print("bit de paridad es cero")
        else:
            print("bit de paridad es uno")
                    
            
ejer = Ejercicio()
num = input("Ingrese numero binario de 4 digitos: ")
#ejer.bitParidad(num)        
ejer.bitPar(num)        
        