from validate_docbr import CPF

class Cpf:
    def __init__(self, cpf):
        if self.valida(cpf):
            self.cpf = cpf
        else:
            raise ValueError("CPF inválido")

    def __str__(self):
        return self.formata()

    def valida(self, cpf):
        validador = CPF()
        return validador.validate(cpf)

    def formata(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

#pode usar nomes iguais ou diferentes nos métodos pois são classes irmãs (polimorfismo)