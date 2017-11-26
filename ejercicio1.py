import random
class Persona:
    def __init__(self, nombre, edad, sexo, DNI, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.DNI = DNI
        self.peso = peso
        self.altura = altura
    def calcularIMC(self):
        imc = int(self.peso) / (int(self.altura) * int(self.altura))
        if self.sexo =='H':
            if imc < 20:
                return (-1, imc)
            elif imc >= 20 and imc <= 25:
                return (0, imc)
            elif imc > 25:
                return (1, imc)
        elif self.sexo == 'M':
            if imc < 19:
                return (-1, imc)
            elif imc >= 20 and imc <= 24:
                return (0, imc)
            elif imc > 24:
                return (1, imc)
    def esMayorDeEdad(self):
        if int(self.edad) >= 18:
            return True
        else:
            return False
    def introducirSexo(self, sexo):
        if sexo == 'H':
            self.sexo = 'H'
        else:
            self.sexo = 'M'
    def toString(self):
        return (self.nombre, self.edad, self.sexo, self.altura, self.peso, self.DNI)
    def generarDNI(self):
        # numPart = random.random(8)
        numPart = ""
        for i in range(0, 8):
            numPart = numPart + str(random.randint(0, 9))
        # letPart = str(randint(65, 90))
        # self.DNI = str(numPart) + letPart
        letter = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
        numLet = int(numPart) % 23
        letPart = letter.__getitem__(numLet)
        self.DNI = str(numPart) + str(letPart)
        return self.DNI

nombre = input("Introduzca el nombre:")
edad = input("Introduzca la edad:")
sexo = input("Introduzca el sexo:")
peso = input("Introduzca el peso:")
altura = input("Introduzca la altura:")

persona = Persona(nombre, edad, sexo, None, peso, altura)

print(persona.generarDNI())

isPesoIdeal = persona.calcularIMC().__getitem__(0)
if(isPesoIdeal < 0):
    print("Su peso está por debajo del ideal")
elif(isPesoIdeal == 0):
    print("Su peso es el ideal")
elif(isPesoIdeal > 0):
    print("Su peso está por encima del ideal")

if(persona.esMayorDeEdad()):
    print("Es mayor de edad")
else:
    print("Es menor de edad")

print(persona.nombre)
print(persona.edad)
print(persona.sexo)
print(persona.DNI)
print(persona.altura)
print(persona.peso)
