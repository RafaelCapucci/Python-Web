from validate_docbr import CNPJ

class Cnpj:
    def __init__(self, cnpj):
        if self.valida(cnpj):
            self.cnpj = cnpj
        else:
            raise ValueError("CNPJ inválido")

    def __str__(self):
        return self.formata()

    def valida(self, cnpj):
        validador = CNPJ()
        return validador.validate(cnpj)

    def formata(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

#pode usar nomes iguais ou diferentes nos métodos pois são classes irmãs (polimorfismo)