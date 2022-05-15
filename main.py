from datas_br import DatasBr
from documento import Documento
from telefone import TelefoneBr
from acesso_cep import BuscaEndereco

cpf = "32909618854"     #passando como string
objeto_cpf = Documento.cria_documento(cpf)
print(objeto_cpf)


cnpj = "05555382000133" #passando como string
objeto_cnpj = Documento.cria_documento(cnpj)
print(objeto_cnpj)

telefone_celular = "meu telefone é +5513974040303 no Brasil ou 13981289880"
objeto_telefone = TelefoneBr(telefone_celular)
print(objeto_telefone)

telefone_fixo = "meu telefone é +551332348786 no Brasil ou 13981289880"
objeto_telefone = TelefoneBr(telefone_fixo)
print(objeto_telefone)

data_cadastro = DatasBr()
print(data_cadastro.mes_cadastro())
print(data_cadastro.dia_semana_cadastro())
print(data_cadastro.formata_data())
print(data_cadastro.tempo_cadastro())

cep = 11030101

objeto_cep = BuscaEndereco(cep)
print(objeto_cep)
bairro, cidade,estado = (objeto_cep.acessa_via_cep())   #criando multiplas variáveis com os dados retornados do método
print(bairro, cidade, estado)
