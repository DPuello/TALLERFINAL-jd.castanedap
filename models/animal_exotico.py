from abc import abstractmethod
from models.animal import Animal


class AnimalExotico(Animal):
    def __init__(self, nombre: str, edad: int, peso: float,
                 pais_origen: str, impuestos: float) -> None:
        super().__init__(nombre, edad, peso)
        self.pais_origen = pais_origen
        self.impuestos = impuestos

    @abstractmethod
    def hacer_sonido(self) -> str:
        pass

    def calcular_flete(self):
        flete = self.peso * self.impuestos
        return flete

    # Getters y Setters
    @property
    def pais_origen(self) -> str:
        return self._pais_origen

    @pais_origen.setter
    def pais_origen(self, nuevo_pais_origen: str) -> None:
        if isinstance(nuevo_pais_origen, str):
            self._pais_origen = nuevo_pais_origen
        else:
            raise ValueError("Ingresa el pais_origen como string")

    @property
    def impuestos(self) -> float:
        return self._impuestos

    @impuestos.setter
    def impuestos(self, nuevo_impuestos: float) -> None:
        if isinstance(nuevo_impuestos, float) or isinstance(
                nuevo_impuestos, int):
            self._impuestos = nuevo_impuestos
        else:
            raise ValueError("Ingresa el impuestos como un número")
