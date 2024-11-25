from models.animal_exotico import AnimalExotico


class BoaConstrictor(AnimalExotico):
    def __init__(self, nombre: str, edad: int, peso: float, pais_origen: str,
                 impuestos: float, ratones_comidos=0) -> None:
        super().__init__(nombre, edad, peso, pais_origen, impuestos)
        self.ratones_comidos = ratones_comidos

    @staticmethod
    def hacer_sonido() -> str:
        return "¡Tsss!"

    def comer_raton(self) -> None:
        try:
            if self.ratones_comidos >= 20:
                raise ValueError("Demasiados Ratones!")
            self.ratones_comidos += 1
        except Exception as e:
            return e

    # Getters y Setters
    @property
    def edad(self) -> int:
        """ Devuelve el valor del atributo privado 'edad' """
        return self.__edad

    @edad.setter
    def edad(self, nueva_edad: int) -> None:
        """
        Establece un nuevo valor para el atributo privado 'edad'

        Valida que el valor enviado corresponda al tipo de dato del atributo
        """
        if isinstance(nueva_edad, int):
            self.__edad = nueva_edad
        else:
            raise ValueError('Expected int')
