from abc import abstractmethod
from models.ianimal import IAnimal


class Animal(IAnimal):
    def __init__(self, nombre: str, edad: int, peso: float) -> None:
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.kilos_comidos = 0

    @abstractmethod
    def hacer_sonido(self) -> str:
        pass

    def comer(self, kilos: float) -> None:
        if isinstance(kilos, float) or isinstance(kilos, int):
            self.__kilos_comidos += kilos
        else:
            raise ValueError("Ingresa los kilos como un número")

    def obtener_kilos_comidos(self) -> float:
        return self.kilos_comidos

    @property
    def kilos_comidos(self):
        return self.__kilos_comidos

    @kilos_comidos.setter
    def kilos_comidos(self, nuevos_kilos):
        if isinstance(nuevos_kilos, float) or isinstance(nuevos_kilos, int):
            self.__kilos_comidos = nuevos_kilos
        else:
            raise ValueError("Ingresa los kilos como un número")

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if (isinstance(nuevo_nombre, str)):
            self._nombre = nuevo_nombre
        else:
            raise ValueError("Ingresa el nombre como un string")

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        if (isinstance(nueva_edad, int)):
            self._edad = nueva_edad
        else:
            raise ValueError("Ingresa la edad como un entero")

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, nuevo_peso):
        if (isinstance(nuevo_peso, float) or isinstance(nuevo_peso, int)):
            self._peso = nuevo_peso
        else:
            raise ValueError("Ingresa el peso como un número")
