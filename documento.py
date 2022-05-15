from cnpj import Cnpj
from cpf import Cpf

class Documento:    #interface (factory)

    @staticmethod       #método estático
    def cria_documento(documento):
        if len(documento) == 11:
            return Cpf(documento)
        elif len(documento) == 14:
            return Cnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos inválida")