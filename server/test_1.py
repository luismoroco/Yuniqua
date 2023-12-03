from enum import Enum


class EditorState(Enum):
    ACTIVE = 1
    ARCHIVED = 2


# Supongamos que tienes una cadena con la clave
clave_str = "ACTIVE"

# Intenta obtener el valor de la clave en la enumeración
try:
    valor = EditorState[clave_str].value
    print("Valor de", clave_str, ":", valor)
except KeyError:
    print("La clave", clave_str, "no se encuentra en la enumeración.")
