from persona import Persona
from deportista import Deportista
class Futbolista(Persona,Deportista):
    listaFutbolistas=[]
    def __init__(self,nombre,edad,altura,sexo,años,goles,tarjetas,pierna):
        Persona.__init__(self,nombre,edad,altura,sexo)
        Deportista.__init__(self,"Futbol",años)
        self._golesMarcados=goles
        self._tarjetasRojas=tarjetas
        self._piernaHabil=pierna
        self.listaFutbolistas.append(self)
        
    def getGolesMarcados(self):
        return self._golesMarcados
    def setGolesMarcados(self,goles):
        self._golesMarcados=goles
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    def setTarjetasRojas(self,tarjetas):
        self._tarjetasRojas=tarjetas
    def getPiernaHabil(self):
        return self._piernaHabil
    def setPiernaHabil(self,pierna):
        self._piernaHabil=pierna
    def __str__(self):
        cadena=f"Mi nombre es {Persona.getNombre(self)} soy profesional en el deporte {Deportista.getDeporte(self)} Tengo {Persona.getEdad(self)} años de edad y llevo {Deportista.getAñosPracticando(self)} años en el deporte"
        return cadena