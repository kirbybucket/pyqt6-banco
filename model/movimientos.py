class Transferencia():
    def __init__(self, tipo:str,documento:str,motivo:float,monto:int,dolares:bool,internacional:bool):
        self._tipo = tipo
        self._documento = documento
        self._motivo = motivo
        self._monto = monto
        self._dolares = dolares
        self._internacional = internacional

class DepositoInternacional():
    def __init__(self, tipo:str,documento:str,motivo:float,monto:int,nombre1:str,nombre2:str,apellido1:str,apellido2:str,sexo:str,fechaNacimiento:str,lugarNacimi:str,terminos:bool):
        self._tipo = tipo
        self._documento = documento
        self._motivo = motivo
        self._monto = monto
        self._dolares = True
        self._internacional = True
        self._nombre1 = nombre1
        self._nombre2 = nombre2
        self._apellido1 = apellido1
        self._apellido2 = apellido2
        self._sexo = sexo
        self._fechaNacimiento = fechaNacimiento
        self._lugarNacimiento = lugarNacimi
        self._terminos = terminos