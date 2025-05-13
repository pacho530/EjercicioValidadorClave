from modelo.validador import (
    Validador,
    ReglaValidacionGanimedes,
    ReglaValidacionCalisto
)
from modelo.errores import ValidadorError

def validar_clave(clave: str, reglas: list):
    for regla in reglas:
        validador = Validador(regla)
        try:
            if validador.es_valida(clave):
                print(f"✅ La clave es válida para {regla.__class__.__name__}")
        except ValidadorError as e:
            print(f"❌ Error: {e}")

# 🔍 Ejemplo de uso
if __name__ == "__main__":
    # Puedes cambiar las reglas aquí si quieres probar con una sola o diferentes combinaciones
    reglas = [
        ReglaValidacionGanimedes(8),
        ReglaValidacionCalisto(0)
    ]

    clave = input("🔐 Ingresa tu clave para validar: ")
    print("\nValidando clave...\n")
    validar_clave(clave, reglas)
