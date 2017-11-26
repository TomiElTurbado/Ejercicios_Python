class Serie:
    def __init__(self, titulo, ntemp, genero, creador):
        self.entregado = False
        self.titulo = titulo
        self.ntemp = ntemp
        self.genero = genero
        self.creador = creador
    def getTitulo(self):
        return self.titulo
    def getNumeroTemporadas(self):
        return self.ntemp
    def getGenero(self):
        return self.genero
    def getCreador(self):
        return self.creador
    def setTitulo(self, titulo):
        self.titulo = titulo
    def setNumeroTemporadas(self, ntemp):
        self.ntemp = ntemp
    def setGenero(self, genero):
        self.genero = genero
    def setCreador(self, creador):
        self.creador = creador
    def entregar(self, estado):
        self.entregado = estado

class Videojuego:
    def __init__(self, titulo, hesti, genero, compania):
        self.entregado = False
        self.titulo = titulo
        self.hesti = hesti
        self.genero = genero
        self.compania = compania
    def getTitulo(self):
        return self.titulo
    def getHorasEstimadas(self):
        return self.hesti
    def getGenero(self):
        return self.genero
    def getCompania(self):
        return self.compania
    def setTitulo(self, titulo):
        self.titulo = titulo
    def setHorasEstimadas(self, hesti):
        self.hesti = hesti
    def setGenero(self, genero):
        self.genero = genero
    def setCompania(self, compania):
        self.compania = compania
    def entregar(self, estado):
        self.entregado = estado

series = (Serie("Titulo1", 20, "Accion", "Matt Groening"), Serie("Titulo2", 20, "Accion", "Matt Groening"), Serie("Titulo3", 20, "Accion", "Matt Groening"), Serie("Titulo4", 20, "Accion", "Matt Groening"), Serie("Titulo5", 20, "Accion", "Matt Groening"))
videojuegos = (Videojuego("Titulo1", 500, "Plataformas", "Sega"), Videojuego("Titulo2", 500, "Plataformas", "Sega"), Videojuego("Titulo3", 500, "Plataformas", "Sega"), Videojuego("Titulo4", 500, "Plataformas", "Sega"), Videojuego("Titulo5", 500, "Plataformas", "Sega"))

series.__getitem__(0).entregar(True)
series.__getitem__(2).entregar(True)
series.__getitem__(4).entregar(True)
videojuegos.__getitem__(1).entregar(True)
videojuegos.__getitem__(3).entregar(True)

seriesEntregadas = 0
juegosEntregados = 0

for i in series:
    if(i.entregado == True):
        seriesEntregadas += 1
        i.entregar(False)
for i in videojuegos:
    if(i.entregado == True):
        juegosEntregados += 1
        i.entregar(False)

print(seriesEntregadas)
print(juegosEntregados)

serieConMas = ""
serieConMasCant = 0
for i in series:
    if(i.getNumeroTemporadas() > serieConMasCant):
        serieConMasCant = i.getNumeroTemporadas()
        serieConMas = i.getTitulo()

juegosConMas = ""
juegosConMasCant = 0
for i in videojuegos:
    if(i.getHorasEstimadas() > juegosConMasCant):
        juegosConMasCant = i.getHorasEstimadas()
        juegosConMas = i.getTitulo()

print(serieConMas)
print(serieConMasCant)
print(juegosConMas)
print(juegosConMasCant)

