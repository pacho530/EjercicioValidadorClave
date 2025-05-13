from abc import ABC, abstractmethod
from .errores import (
    NoCumpleLongitudMinimaError,
    NoTieneLetraMayusculaError,
    NoTieneLetraMinusculaError,
    NoTieneNumeroError,
    NoTieneCaracterEspecialError,
    NoTienePalabraSecretaError
)

# Clase abstracta base
class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada: int):
        self._longitud_esperada = longitud_esperada

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass

    def _validar_longitud(self, clave: str) -> bool:
        return len(clave) > self._longitud_esperada

    def _contiene_mayuscula(self, clave: str) -> bool:
        return any(c.isupper() for c in clave)

    def _contiene_minuscula(self, clave: str) -> bool:
        return any(c.islower() for c in clave)

    def _contiene_numero(self, clave: str) -> bool:
        return any(c.isdigit() for c in clave)

# Ganimedes
class ReglaValidacionGanimedes(ReglaValidacion):
    def contiene_caracter_especial(self, clave: str) -> bool:
        especiales = '@_#$%'
        return any(c in especiales for c in clave)

    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError("ReglaValidacionGanimedes: La clave debe tener una longitud de más de 8 caracteres")
        if not self._contiene_mayuscula(clave):
            raise NoTieneLetraMayusculaError("ReglaValidacionGanimedes: La clave debe contener al menos una letra mayúscula")
        if not self._contiene_minuscula(clave):
            raise NoTieneLetraMinusculaError("ReglaValidacionGanimedes: La clave debe contener al menos una letra minúscula")
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError("ReglaValidacionGanimedes: La clave debe contener al menos un número")
        if not self.contiene_caracter_especial(clave):
            raise NoTieneCaracterEspecialError("ReglaValidacionGanimedes: La clave debe contener al menos un carácter especial (@ _ # $ %)")
        return True

# Calisto
class ReglaValidacionCalisto(ReglaValidacion):
    def contiene_calisto(self, clave: str) -> bool:
        palabra = "calisto"
        for i in range(len(clave) - len(palabra) + 1):
            subcadena = clave[i:i+len(palabra)]
            if subcadena.lower() == palabra:
                mayus = sum(1 for c in subcadena if c.isupper())
                if 1 < mayus < len(palabra):
                    return True
        return False

    def es_valida(self, clave: str) -> bool:
        if not self.contiene_calisto(clave):
            raise NoTienePalabraSecretaError("ReglaValidacionCalisto: La palabra calisto debe estar escrita con al menos dos letras en mayúscula")
        return True

# Clase Validador
class Validador:
    def __init__(self, regla: ReglaValidacion):
        self.regla = regla

    def es_valida(self, clave: str) -> bool:
        return self.regla.es_valida(clave)
