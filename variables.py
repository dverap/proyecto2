# comentario
class Sintaxis:
   
    def __init__(self,titulo):
        self.mensaje = titulo
    
    def usoVariables(self):
        # varaibles primitivas
        edad, __peso = 50, 70.5
        nombre = "Daniel Vera"    
                  #012345678910
        tipo_sexo = 'M'
        civil = True
        #variables compuestas o colecciones
        usuario = ('dchiki', 1234, 'chiki@gmail.com',True)
        materias = ['Programacion Web', 'Php', 'POO']
        docente = {'nombre': 'Daniel', 'edad': 50, 'fac': 'faci'}
        print(self.mensaje)
        print(nombre,edad,tipo_sexo)
        print(usuario)
        print(materias)
        print(docente)
        
        
    # Dados dos (2) números calcule la suma, resta, multiplicación, división y módulo    
    def ejercicio4(self,num1,num2):
        sum = num1+num2
        res = num1 - num2
        mul = num1 * num2
        div = num1 // num2
        print("{}+{}={}".format(num1,num2,sum))
        print("{}-{}={}".format(num1,num2,res))
        print("{}*{}={}".format(num1,num2,mul))
        print("{}/{}={}".format(num1,num2,div))
        

# instancia de la clase Sintaxis
sintaxisVariable = Sintaxis("Uso de variables")
#sintaxisVariable.ejercicio2()
sintaxisVariable.ejercicio4(10,2)
