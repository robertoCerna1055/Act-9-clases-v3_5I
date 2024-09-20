print("Actividad 9 clase humano")
print("Roberto Cerna / Mat: 22308051281055")
print("")

# Zona de clases

class Humano1055:
    
    # Zona de atibutos dentro de la clase
    
    edad = 17
    nombre = "Roberto"
    genero = "Masculino"
    peso = 80.0
    estatura = 1.81
    colorPelo = "Negro"
    
    
    # Zona de funciones dentro de la clase
    
    def correr1055(self, n):
        print(f"{n} esta corriendo uffff.....")
        
    def caminar1055(self, n):
        print(f"{n} esta caminando uffff.....")
    
    def hablar1055(self, n):
        print(f"{n} esta hablando uffff.....")
        
    def saltar1055(self, n):
        print(f"{n} esta saltando uffff.....")
        
    def gritar1055(self, n):
        print(f"{n} esta gritando uffff.....")


    # Zona de creacion de objetos
    
roberto = Humano1055()
Cazzu = Humano1055()
      
    # Zona de usando objetos
    
print("---Resultado para Roberto---")
print(f"Edad: {roberto.edad}")
print(f"Nombre: {roberto.nombre}")
print(f"Genero: {roberto.genero}")
print(f"Peso: {roberto.peso}kg")
print(f"Estatura: {roberto.estatura}m")
print(f"Color de pelo: {roberto.colorPelo}")

roberto.correr1055("Roberto")
roberto.caminar1055("Roberto")
roberto.hablar1055("Roberto")
roberto.saltar1055("Roberto")
roberto.gritar1055("Roberto")
print("")

Cazzu.edad = 30
Cazzu.nombre = "Cazzu"
Cazzu.genero = "Femenino"
Cazzu.peso = 57
Cazzu.estatura = 1.67
Cazzu.colorPelo = "Rubia"

print("---Resultado para Cazzu---")
print(f"Edad: {Cazzu.edad}")
print(f"Nombre: {Cazzu.nombre}")
print(f"Genero: {Cazzu.genero}")
print(f"Peso: {Cazzu.peso}kg")
print(f"Estatura: {Cazzu.estatura}m")
print(f"Color de pelo: {Cazzu.colorPelo}")

Cazzu.correr1055("Cazzu")
Cazzu.caminar1055("Cazzu")
Cazzu.hablar1055("Cazzu")
Cazzu.saltar1055("Cazzu")
Cazzu.gritar1055("Cazzu")