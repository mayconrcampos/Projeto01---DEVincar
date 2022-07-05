from Veiculo import Veiculo
from utils import Utils

class Carro(Veiculo):
    def __init__(self) -> None:
        #super().__init__(self.chassi, self.data_fab, self.modelo, self.placa, self.valor, self.cpf_compr, self.cor)
        
        self.portas = None
        self.combustivel = None
        self.potencia = None
    
    def vender_veiculo(self):
        print("VENDA DO VEÍCULO".center(100, "-"))

        print("GERANDO NÚMERO DE CHASSI")
        chassi = Utils.gera_chassi()

        self.chassi = chassi

        while True:
            data_fab = input("DATA FABRICAÇÃO: 00-00-0000 : ")

            if not Utils.valida_data(data=data_fab):
                print("DATA DEVE SER VÁLIDA DE VERDADE")
                print("Deve ser no formato __-__-____")

                continue
            else:
                self.data_fab = Utils.valida_data(data=data_fab)
                print("DATA FABRICAÇÃO INFORMADA COM SUCESSO.")
                break
        
        while True:
            modelo = input("MODELO: ")

            if not modelo:
                print("VOCÊ DEVE INSERIR O MODELO")
                continue
            else:
                self.modelo = modelo
                print("MODELO INSERIDO COM SUCESSO")
                break
        
        while True:
            placa = input("DIGITE A PLACA: ANTIGA OU MERCOSUL: ")

            if not Utils.valida_placa(placa):
                print("DIGITE UMA PLACA CORRETA")
                print("DEVE SER NO FORMATO ANTIGO MMM0000")
                print("OU NO FORMATO MERCOSUL: MMM0M00")
                continue
            else:
                self.placa = Utils.valida_placa(placa)
                print("PLACA INSERIDA COM SUCESSO")
                break
        
        while True:
            valor = input("DIGITE O VALOR: R$: ")

            if not Utils.valida_valor(valor):
                print("DIGITE UM VALOR MONETÁRIO VÁLIDO")
                print("PODE SER NÚMERO INTEIRO (100)")
                print("PODE SER NÚMERO COM PONTO PRA CASA DECIMAL (100.00)")
                print("PODE SER NÚMERO COM VIRGULA PRA CASA DECIMAL (100,00)")
                continue
            else:
                self.valor = Utils.valida_valor(valor)
                print("VALOR INSERIDO COM SUCESSO")
                break
        
        while True:
            cpf_compr = input("DIGITE O CPF DO COMPRADOR: ")

            
        

        print("Olar")

            
        


    def listar_infos(self):
        pass 

    def alterar_infos(self):
        pass


c = Carro()

c.vender_veiculo()