from ctypes import util
from random import randint
from Veiculo import Veiculo
from utils import Utils
from Database import Database

class Camionete(Veiculo):
    def __init__(self) -> None:
        #super().__init__(self.chassi, self.data_fab, self.modelo, self.placa, self.valor, self.cpf_compr, self.cor)

        self.portas = None
        self.cacamba = None
        self.potencia = None
        self.combustivel = None
    
    def fabricar_veiculo(self):
        self.chassi = Utils.gera_chassi()
        self.data_fab = Utils.gera_data_HOJE()
        self.modelo = Utils.gerador_de_modelo()
        self.placa = None
        self.potencia = Utils.setPotencia_CAMIONETE()
        self.valor = Utils.gerador_de_valor_CAMIONETE(self.potencia)
        self.cpf_compr = None
        self.cor = "ROXO"
        self.portas = Utils.setPortas_CAMIONETE()
        self.cacamba = Utils.setCamionete_CACAMBA_LITROS()
        self.combustivel = Utils.setCombustivel_CAMIONETE()
        

        caminhonete = {
            "tipo": "Camionete",
            "chassi": self.chassi,
            "data_fab": self.data_fab,
            "modelo": self.modelo,
            "placa": self.placa,
            "valor": self.valor,
            "cpf_compr": self.cpf_compr,
            "cor": self.cor,
            "portas": self.portas,
            "cacamba": self.cacamba,
            "combustivel": self.combustivel,
            "potencia": self.potencia,
            "vendido": False         
        }

        Database.adicionar_veiculo(veiculo=caminhonete)


    def vender_veiculo(self):
        print("VENDA DE CAMIONETE".center(100, "-"))

        print("GERANDO NÚMERO DE CHASSI")
        chassi = Utils.gera_chassi()

        self.chassi = chassi
        print(f"CHASSI: {self.chassi}")


        while True:
            data_fab = input("DATA FABRICAÇÃO: 00-00-0000 : ")
            Utils.clear_tela()

            if not Utils.valida_data(data=data_fab):
                print("DATA DEVE SER VÁLIDA DE VERDADE")
                print("Deve ser no formato __-__-____")

                continue
            else:
                self.data_fab = Utils.valida_data(data=data_fab)
                print("DATA FABRICAÇÃO INFORMADA COM SUCESSO.")
                break
        
        while True:
            modelo = input("MODELO: ").upper()
            Utils.clear_tela()

            if not modelo:
                print("VOCÊ DEVE INSERIR O MODELO")
                continue
            else:
                self.modelo = modelo
                print("MODELO INSERIDO COM SUCESSO")
                break
        
        while True:
            placa = input("DIGITE A PLACA: ANTIGA OU MERCOSUL: ").upper()
            Utils.clear_tela()

            if not Utils.valida_placa(placa):
                print("DIGITE UMA PLACA CORRETA")
                print("DEVE SER NO FORMATO ANTIGO MMM0000")
                print("OU NO FORMATO MERCOSUL: MMM0M00")
                continue
            else:
                if Database.existe_PLACA(placa):
                    print("PLACA JÁ CADASTRADA NO SISTEMA! DIGITE OUTRA!")
                else:
                    self.placa = Utils.valida_placa(placa)
                    print("PLACA INSERIDA COM SUCESSO")
                    break
        
        while True:
            valor = input("DIGITE O VALOR: R$: ")
            Utils.clear_tela()

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
            Utils.clear_tela()

            if not Utils.valida_cpf(cpf_completo=cpf_compr):
                print("DIGITE UM CPF VÁLIDO")
                print("CPF POSSUI 11 DÍGITOS")
                print("NÃO DIGITE OS PONTOS E O TRAÇO\n")

                while True:
                    gera_cpf = input("AO INVÉS DE DIGITAR, QUER GERAR UM CPF VÁLIDO?\n1. Gerar CPF\n2. Inserir meu CPF\n: ")
                    Utils.clear_tela()

                    if gera_cpf.isnumeric():
                        match gera_cpf:
                            case "1":
                                self.cpf_compr = Utils.gera_cpf()
                                print(f"CPF {self.cpf_compr} GERADO E INSERIDO COM SUCESSO!")
                                break
                            case "2":
                                self.cpf_compr = False
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
   
            Utils.print_ROXO("1. SÓ TEM ROXO")

            print("2. QUER TENTAR ESCOLHER OUTRA COR? FIQUE A VONTADE.")

            opcao_cor = input("Opção: ")
            Utils.clear_tela()

            if opcao_cor.isnumeric():
                match opcao_cor:
                    case "1":
                        Utils.print_ROXO("1. ROXO - Ótima Escolha!")
                        self.cor = "ROXO"
                        break

                    case "2":
                        Utils.trava_lingua()
            
                    case _:
                        print("Opção inválida")
                
            else:
                print("Opção numérica inválida")
  
        

        while True:
            portas = input("NÚMERO DE PORTAS: ")
            Utils.clear_tela()

            if Utils.valida_portas(portas):
                self.portas = Utils.valida_portas(portas)
                print(f"PORTAS: {self.portas}")
                break
            else:
                print("OPÇÕES DISPONÍVEIS: 2 OU 4 PORTAS")
                continue
        
        
        while True:
            print("COMBUSTÍVEL".center(50, "-"))
            print("1. GASOLINA\n2. DIESEL")

            combustivel = input("Opção: ")
            Utils.clear_tela()

            if combustivel.isnumeric():
                if combustivel == "1":
                    self.combustivel = "GASOLINA"
                    print(f"COMBUSTÍVEL SELECIONADO: {self.combustivel}")
                    break

                elif combustivel == "2":
                    self.combustivel = "DIESEL"
                    print(f"COMBUSTÍVEL SELECIONADO: {self.combustivel}")
                    break
                else:
                    print("Opção inválida!")
            else:
                print("Opção numérica inválida")
        

        while True:
            print("POTÊNCIA".center(50, "-"))
            print("1. 2.5 130CV\n2. 3.0 190CV\n3. 4.0 250CV")

            potencia = input("Opção: ")
            Utils.clear_tela()

            if potencia.isnumeric():
                if potencia == "1":
                    self.potencia = "2.5 130CV"
                    print(f"POTÊNCIA SELECIONADA: {self.potencia}")
                    break

                elif potencia == "2":
                    self.potencia = "3.0 190CV"
                    print(f"POTÊNCIA SELECIONADA: {self.potencia}")
                    break

                elif potencia == "3":
                    self.potencia = "3.0 190CV"
                    print(f"POTÊNCIA SELECIONADA: {self.potencia}")
                    break

                else:
                    print("Opção inválida")
            else:
                print("Opção numérica inválida")
        

        while True:
            print("CAPACIDADE DA CAÇAMBA / LITROS")

            print("1. 500 Litros")
            print("2. 750 Litros")
            print("3. 1000 Litros")

            cacamba = input("Opção: ")

            if cacamba.isnumeric():
                if cacamba == "1":
                    print("1. 500 Litros")
                    self.cacamba = "500 Litros"
                    break

                elif cacamba == "2":
                    self.cacamba = "750 Litros"
                    break

                elif cacamba == "3":
                    self.cacamba = "1000 Litros"
                    break

                else:
                    print("Opção inválida")
            else:
                print("Opção numérica inválida")
        
        
        caminhonete = {
            "tipo": "Camionete",
            "chassi": self.chassi,
            "data_fab": self.data_fab,
            "modelo": self.modelo,
            "placa": self.placa,
            "valor": self.valor,
            "cpf_compr": self.cpf_compr,
            "cor": self.cor,
            "portas": self.portas,
            "combustivel": self.combustivel,
            "potencia": self.potencia,
            "cacamba": self.cacamba        
        }

        Database.adicionar_veiculo(veiculo=caminhonete)

    def listar_infos(self, status: str):
        Database.listar_VEICULOS("Camionete", status=status)

    def alterar_infos(self):
        print("LISTANDO CAMIONETES VENDIDOS".center(50, "-"))
        
        
        while True:
            Database.listar_VEICULOS("Camionete")
            placa = input("DIGITE A PLACA: ANTIGA OU MERCOSUL: ").upper()
            Utils.clear_tela()

            if not Utils.valida_placa(placa):
                print("DIGITE UMA PLACA CORRETA")
                print("DEVE SER NO FORMATO ANTIGO MMM0000")
                print("OU NO FORMATO MERCOSUL: MMM0M00")
                continue
            else:
                print("PROCURANDO CAMIONETES NA BASE DE DADOS".center(50, "-"))

                if Database.existe_PLACA(placa=placa):
                    if Database.busca_por_PLACA(placa=placa, tipo="Camionete"):
                        self.placa = placa
                        break
                    else:
                        print(f"PLACA {placa} PERTENCE A OUTRA CATEGORIA DE VEÍCULO.")
                        continue
                    
                else:
                    print("PLACA NÃO ENCONTRADA")
        

        while True:
            print("ESCOLHA A COR".center(50, "-"))
            Utils.print_ROXO("1. ROXO")
            print("2. Quer outra cor? QUER TENTAR TROCAR?")

            opcao_cor = input("Opção: ")
            Utils.clear_tela()

            if opcao_cor.isnumeric():
                match opcao_cor:
                    case "1":
                        Utils.print_ROXO("1. ROXO DE NOVO? ÓTIMA ESCOLHA!")
                        self.cor = "ROXO"
                        break

                    case "2":
                        Utils.trava_lingua()

                    case _:
                        print("Opção inválida")
                
            else:
                print("Opção numérica inválida")
   

        
        while True:
            valor = input("DIGITE O VALOR: R$: ")
            Utils.clear_tela()

            if not Utils.valida_valor(valor):
                print("DIGITE UM VALOR MONETÁRIO VÁLIDO")
                print("PODE SER NÚMERO INTEIRO (100)")
                print("PODE SER NÚMERO COM PONTO PRA CASA DECIMAL (100.00)")
                print("PODE SER NÚMERO COM VIRGULA PRA CASA DECIMAL (100,00)")
                continue
            else:
                valor = Utils.valida_valor(valor)
                print("VALOR INSERIDO COM SUCESSO")
                break
        
        
        if Database.busca_por_PLACA(placa=self.placa, tipo="Camionete"):
            Database.alterar_VEICULO(placa=self.placa, cor=self.cor, valor=valor)
        else:
            print(f"CAMIONETE NÃO PERMITE MODIFICAR PLACA DE OUTROS TIPOS DE VEICULO")
    

#caminhoneta = Camionete()
##caminhoneta.vender_veiculo()
##caminhoneta.listar_infos()
#caminhoneta.alterar_infos()