from models.boa_constrictor import BoaConstrictor
from models.huron import Huron


class Guarderia:
    def __init__(self, nombre: str, ubicacion: str):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.hurones = [
            Huron("Bobby", 2, 9.1, "Canada", 2),
            Huron("Sneaky", 5, 3.6, "Colombia", 15.2)
        ]
        self.boas = [
            BoaConstrictor("Sneaky", 5, 3.6, "Colombia", 15.2),
            BoaConstrictor("Bobby", 2, 9.1, "Canada", 2)
        ]

    def alimentar_boa(self, boa: int) -> None:
        try:
            result = self.boas[boa].comer_raton()
            if result is None:
                return "Éxito"
            else:
                raise ValueError(result)
        except ValueError as e:
            if str(e) == "Demasiados Ratones!":
                return "La boa está llena"
        except Exception:
            return "Esta Boa no existe!"

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        if isinstance(nuevo_nombre, str):
            self.__nombre = nuevo_nombre
        else:
            raise ValueError("El nombre debe ser una cadena de caracteres")

    @property
    def ubicacion(self) -> str:
        return self.__ubicacion

    @ubicacion.setter
    def ubicacion(self, nueva_ubicacion: str) -> None:
        if isinstance(nueva_ubicacion, str):
            self.__ubicacion = nueva_ubicacion
        else:
            raise ValueError("La ubicación debe ser una cadena de caracteres")

    @property
    def hurones(self) -> list[Huron]:
        return self.__hurones

    @hurones.setter
    def hurones(self, nuevos_hurones: list[Huron]) -> None:
        if all(isinstance(huron, Huron) for huron in nuevos_hurones):
            self.__hurones = nuevos_hurones
        else:
            raise ValueError("Todos los elementos deben ser "
                             "instancias de Huron")

    @property
    def boas(self) -> list[BoaConstrictor]:
        return self.__boas

    @boas.setter
    def boas(self, nuevas_boas: list[BoaConstrictor]) -> None:
        if all(isinstance(boa, BoaConstrictor) for boa in nuevas_boas):
            self.__boas = nuevas_boas
        else:
            raise ValueError("Todos los elementos deben ser "
                             "instancias de BoaConstrictor")
