from Veiculo import Veiculo
from utils import Utils
from os import system
from tinydb import TinyDB, Query

class Carro(Veiculo):
    def __init__(self) -> None:
        #super().__init__(self.chassi, self.data_fab, self.modelo, self.placa, self.valor, self.cpf_compr, self.cor)
        
        self.portas = None
        self.combustivel = None
        self.potencia = None

        self.carros = TinyDB("carros.json")
    
    def vender_veiculo(self):
        print("VENDA DO VEÍCULO".center(100, "-"))

        print("GERANDO NÚMERO DE CHASSI")
        chassi = Utils.gera_chassi()

        self.chassi = chassi
        print(f"CHASSI: {self.chassi}")


        while True:
            data_fab = input("DATA FABRICAÇÃO: 00-00-0000 : ")
            system("clear")

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
            system("clear")

            if not modelo:
                print("VOCÊ DEVE INSERIR O MODELO")
                continue
            else:
                self.modelo = modelo
                print("MODELO INSERIDO COM SUCESSO")
                break
        
        while True:
            placa = input("DIGITE A PLACA: ANTIGA OU MERCOSUL: ")
            system("clear")

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
            system("clear")

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
            system("clear")

            if not Utils.valida_cpf(cpf_completo=cpf_compr):
                print("DIGITE UM CPF VÁLIDO")
                print("CPF POSSUI 11 DÍGITOS")
                print("NÃO DIGITE OS PONTOS E O TRAÇO\n")

                while True:
                    gera_cpf = input("AO INVÉS DE DIGITAR, QUER GERAR UM CPF VÁLIDO?\n1. Gerar CPF\n2. Inserir meu CPF\n: ")
                    system("clear")

                    if gera_cpf.isnumeric():
                        match gera_cpf:
                            case "1":
                                self.cpf_compr = Utils.gera_cpf()
                                print(f"CPF {self.cpf_compr} GERADO E INSERIDO COM SUCESSO!")
                                break
                            case "2":
                                break
                            case _:
                                print("OPÇÃO INVÁLIDA")
                                continue
                    else:
                        print("Caracter Inválido! Precisa digitar números inteiros pra escolher.")

                if not self.cpf_compr:        
                    continue
                else:
                    break

            else:
                self.cpf_compr = Utils.valida_cpf(cpf_completo=cpf_compr)
                print(f"CPF INSERIDO COM SUCESSO: {self.cpf_compr}")
                break

       

        while True:
            print("ESCOLHA A COR".center(50, "-"))
            print("1. BRANCO")
            print("2. PRETO")
            print("3. ROXO")
            print("4. AMARELO")
            print("5. INDECISO? Você pode Sortear a COR")

            opcao_cor = input("Opção: ")
            system("clear")

            if opcao_cor.isnumeric():
                match opcao_cor:
                    case "1":
                        print("1. BRANCO")
                        self.cor = "BRANCO"
                    case "2":
                        print("2. PRETO")
                        self.cor = "PRETO"
                    case "3":
                        print("3. ROXO")
                        self.cor = "ROXO"
                    case "4":
                        print("4. AMARELO")
                        self.cor = "AMARELO"
                    case "5":
                        print("5. SORTEAR COR")

                        while True:
                            sortear = input("Tecle ENTER pra sortear: ")
                            system("clear")

                            if not sortear:
                                self.cor = Utils.sortear_cor()
                                print(f"COR SORTEADA: {self.cor}")
                                break
                            else:
                                self.cor = Utils.sortear_cor()
                                print(f"COR SORTEADA: {self.cor}")
                                break

                    case _:
                        print("Opção inválida")
                
            else:
                print("Opção numérica inválida")
            
            if self.cor:
                break
        

        while True:
            portas = input("NÚMERO DE PORTAS: ")
            system("clear")

            if Utils.valida_portas(portas):
                self.portas = Utils.valida_portas(portas)
                print(f"PORTAS: {self.portas}")
                break
            else:
                print("OPÇÕES DISPONÍVEIS: 2 OU 4 PORTAS")
                continue
        
        
        while True:
            print("COMBUSTÍVEL".center(50, "-"))
            print("1. GASOLINA\n2.FLEX")

            combustivel = input("Opção: ")
            system("clear")

            if combustivel.isnumeric():
                if combustivel == "1":
                    self.combustivel = "GASOLINA"
                    print(f"COMBUSTÍVEL SELECIONADO: {self.combustivel}")
                    break

                elif combustivel == "2":
                    self.combustivel = "FLEX"
                    print(f"COMBUSTÍVEL SELECIONADO: {self.combustivel}")
                    break
                else:
                    print("Opção inválida!")
            else:
                print("Opção numérica inválida")
        

        while True:
            print("POTÊNCIA".center(50, "-"))
            print("1. 1.0 65CV\n2. 1.6 100CV\n3. 2.0 150CV")

            potencia = input("Opção: ")
            system("clear")

            if potencia.isnumeric():
                if potencia == "1":
                    self.potencia = "1.0 65CV"
                    print(f"POTÊNCIA SELECIONADA: {self.potencia}")
                    break

                elif potencia == "2":
                    self.potencia = "1.6 100CV"
                    print(f"POTÊNCIA SELECIONADA: {self.potencia}")
                    break

                elif potencia == "3":
                    self.potencia = "2.0 150CV"
                    print(f"POTÊNCIA SELECIONADA: {self.potencia}")
                    break

                else:
                    print("Opção inválida")
            else:
                print("Opção numérica inválida")
        
        
        carrodicio = {
            "chassi": self.chassi,
            "data_fab": self.data_fab,
            "modelo": self.modelo,
            "placa": self.placa,
            "valor": self.valor,
            "cpf_compr": self.cpf_compr,
            "cor": self.cor,
            "portas": self.portas,
            "combustivel": self.combustivel,
            "potencia": self.potencia         
        }

        self.__adicionar_carro(carrodicio)
              
        
    def listar_infos(self):
        self.carros.all()

        for carro in self.carros:
            print(carro) 

    def alterar_infos(self):
        pass
    
    def listar_carro(self, chassi: str):
        search = Query()
        
        lista = self.carros.search(search.chassi == chassi)


        if lista:
            for carro in lista:
                print(carro)
        else:
            print(f"CARRO COM CHASSI {chassi} NÃO ENCONTRADO")

    def __adicionar_carro(self, carro: dict):
        self.carros.insert(carro)


c = Carro()

c.vender_veiculo()
#DB.adicionar_carro(c)
c.listar_infos()
#c.listar_carro("13V XXOUIS QV 5K7IJF")
