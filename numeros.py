class EjerNumeros:
  def __init__(self, dato=[]):
    #?crea un atributo de instancia de la clase "lista" con el valor del parametro dato
    self.lista = dato 
    x = dato
  
  def par(self,num):
    rec =  num % 2     #4 % 2 = 0 proceso matematico
    if num == 0:  # proceso logico
      print("es cero")
    elif rec == 0:
      print("es par")
    else:
      print("es impar")
  
  def parReturn(self,num):
    rec =  num % 2     
    if rec == 0:
      return True
    else:
      return False
  
  def sumaPar(self):
     acu=0
     cont = 0
     while cont < len(self.lista):
       n = self.lista[cont]
       if n%2 == 0:
         acu = acu + n
       cont = cont + 1    
     return acu   

  def sumaParFor(self):
     acu=0    
     # range. genera un rango de valores desde hasta                     
     for cont in range(0,len(self.lista)): #(0,1,2,3,4)
       n = self.lista[cont]
       if n%2 == 0:
         acu = acu + n
     return acu   
      
  def sumaParForLista(self):
     acu=0    
     # in for recorre una colenccio valor por valor                     
     for num in self.lista: #[2,3,5,8,10]
       if self.parReturn(num) == True:
         acu = acu + num
     return acu   
      
# instancia la clase EjerNumeros(crear un objeto(variable) como una copia de la clase "ejer1")
# y ejecuta el constructor(crea e inicializa los atributos(lista))
ejer1 = EjerNumeros([2,3,5,8,10])
#ejer1.par(8)
# x =ejer1.sumaPar()
# print(x)
# x =ejer1.sumaParFor()
# print(x)
x =ejer1.sumaParForLista()
print(x)
