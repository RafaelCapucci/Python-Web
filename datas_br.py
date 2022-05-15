from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()
        print(self.momento_cadastro)

    def mes_cadastro(self):
        meses_do_ano = {
            "1" : "Janeiro","2" : "Fevereiro","3" : "Março","4" : "Abril","5" : "Maio","6" : "Junho",
            "7" : "Julho","8" : "Agosto","9" : "Setembro","10" : "Outubro","11" : "Novembro","12" : "Dezembro"
        }   #dicionário
        mes_cadastro = self.momento_cadastro.month  #retorna um "int"
        return meses_do_ano[str(mes_cadastro)]

    def dia_semana_cadastro(self):
        dias_da_semana = ["segunda","terça","quarta","quinta","sexta","sábado","domingo"]   #lista
        dia_semana = self.momento_cadastro.weekday()    #retorna um "int"
        return dias_da_semana[dia_semana]

    def formata_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        tempo_em_dias = (datetime.today() + timedelta(days=30)) - self.momento_cadastro
        return tempo_em_dias.days
