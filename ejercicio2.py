class Electrodomestico:
    colores = {"blanco", "negro", "rojo", "azul", "gris"}
    consumoEnergeticoLista = {"A", "B", "C", "D", "E", "F"}
    def __init__(self, precioBase, color, consumoEnergetico, peso):
        '''for i in Electrodomestico.colores:
            if(i == color):
                self.color = color'''
        self.color = Electrodomestico.comprobarColor(self, color)
        self.precioBase = precioBase
        self.peso = peso
        self.consumoEnergetico = Electrodomestico.comprobarConsumoEnergetico(self, consumoEnergetico)
            #for i in consumoEnergetico:
            #    if(i == consumoEnergetico):
            #        self.consumoEnergetico = consumoEnergetico
            #    else:
    def comprobarConsumoEnergetico(self, letra):
        for i in Electrodomestico.consumoEnergeticoLista:
            if(i == letra):
                return letra
        return "F"
    def comprobarColor(self, color):
        for i in Electrodomestico.colores:
            if(i == color):
                return color
        return "blanco"
    def precioFinal(self):
        aumento = Electrodomestico.dictionary(self, self.consumoEnergetico)
        precioFinal = float(self.precioBase + aumento)
        if(self.peso <= 19):
            precioFinal = precioFinal + 10
        elif(self.peso <=49):
            precioFinal = precioFinal + 50
        elif (self.peso <= 79):
            precioFinal = precioFinal + 80
        else:
            precioFinal = precioFinal + 100
        return precioFinal
    '''def dictionary(self, letter):
        return {
            "A": 100,
            "B": 80,
            "C": 60,
            "D": 50,
            "E": 30,
            "F": 10
        }[letter]'''
    def dictionary(self, letter):
        if (letter == "A"):
            return 100
        elif (letter == "B"):
            return 80
        elif (letter == "C"):
            return 60
        elif (letter == "D"):
            return 50
        elif (letter == "E"):
            return 30
        elif (letter == "F"):
            return 10
        else:
            return 0

class Lavadora(Electrodomestico):
    def __init__(self, carga, precioBase, color, consumoEnergetico, peso):
        self.carga = carga
        self.color = Electrodomestico.comprobarColor(self, color)
        self.precioBase = precioBase
        self.consumoEnergetico = Electrodomestico.comprobarConsumoEnergetico(self, consumoEnergetico)
        self.peso = float(peso)
    def precioFinal(self):
        precioFinal = Electrodomestico.precioFinal(self)
        if(self.carga > 30):
            precioFinal = precioFinal + 50
        return precioFinal
    def getCarga(self):
        return self.carga

class Television(Electrodomestico):
    def __init__(self, resolucion, fourK, precioBase, color, consumoEnergetico, peso):
        self.resolucion = resolucion
        self.fourK = bool(fourK)
        self.color = Electrodomestico.comprobarColor(self, color)
        self.precioBase = precioBase
        self.consumoEnergetico = Electrodomestico.comprobarConsumoEnergetico(self, consumoEnergetico)
        self.peso = float(peso)
    def getResolucion(self):
        return self.resolucion
    def getFourK(self):
        return self.fourK
    def precioFinal(self):
        precioFinal = Electrodomestico.precioFinal(self)
        if(self.fourK == True):
            precioFinal = precioFinal + 50
        if(self.resolucion > 40):
            precioFinal = precioFinal + ((precioFinal / 100) * 30)
        return precioFinal

# electrodomesticos = {Electrodomestico(20, "blanco", 20, 50), Electrodomestico(20, "blanco", 20, 50), Electrodomestico(20, "blanco", 20, 50), Electrodomestico(20, "blanco", 20, 50), Electrodomestico(20, "blanco", 20, 50), Electrodomestico(20, "blanco", 20, 50), Electrodomestico(20, "blanco", 20, 50), Electrodomestico(20, "blanco", 20, 50), Electrodomestico(20, "blanco", 20, 50), Electrodomestico(20, "blanco", 20, 50)}

electrodomesticos = {Electrodomestico(20, "blanco", "A", 50), Television(48, True, 20, "blanco", "A", 50), Lavadora(80, 20, "blanco", "A", 50), Electrodomestico(20, "blanco", "B", 50), Electrodomestico(20, "blanco", "C", 50), Electrodomestico(20, "blanco", "D", 50), Electrodomestico(20, "blanco", "E", 50), Electrodomestico(20, "blanco", "F", 50), Electrodomestico(20, "blanco", "A", 50), Electrodomestico(20, "blanco", "B", 50)}

for i in electrodomesticos:
    print(i.precioFinal())

totalElectrodomestico = 0
totalTelevision = 0
totalLavadora = 0
total = 0

for i in electrodomesticos:
    if(type(i) is Electrodomestico):
        totalElectrodomestico += i.precioFinal()
    elif(type(i) is Television):
        totalTelevision += i.precioFinal()
    elif(type(i) is Lavadora):
        totalLavadora += i.precioFinal()
    total += i.precioFinal()

print("El precio de los electrodomesticos es: ")
print(totalElectrodomestico)
print("El precio de las televisiones es: ")
print(totalTelevision)
print("El precio de las lavadoras es: ")
print(totalLavadora)
print("El precio de todo es: ")
print(total)
