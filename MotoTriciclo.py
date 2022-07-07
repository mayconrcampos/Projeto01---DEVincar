from Veiculo import Veiculo
from utils import Utils
from os import system
from Database import Database

class MotoTriciclo(Veiculo):
    def __init__(self) -> None:
        #super().__init__(self.chassi, self.data_fab, self.nome, self.placa, self.valor, self.cpf_compr, self.cor)

        self.combustivel = "Gasolina"
        self.potencia = None
        self.num_rodas = None
    
    def vender_veiculo(self):
        print("VENDA DE MOTO / TRICICLO".center(100, "-"))

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
            modelo = input("MODELO: ").upper()
            system("clear")

            if not modelo:
                print("VOCÊ DEVE INSERIR O MODELO")
                continue
            else:
                self.modelo = modelo
                print("MODELO INSERIDO COM SUCESSO")
                break
        
        while True:
            placa = input("DIGITE A PLACA: ANTIGA OU MERCOSUL: ").upper()
            system("clear")

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
                    gera_cpf = input("AO INVÉS DE DIGITAR, QUER GERAR UM CPF VÁLIDO?\n1. Gerar CPF\n2. Não! Quero Inserir meu CPF\n: ")
                    system("clear")

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
            Utils.print_BRANCO("1. BRANCO")
            Utils.print_PRETO("2. PRETO")
            Utils.print_ROXO("3. ROXO")
            Utils.print_AMARELO("4. AMARELO")
            print("5. INDECISO? Você pode Sortear a COR")

            opcao_cor = input("Opção: ")
            system("clear")

            if opcao_cor.isnumeric():
                match opcao_cor:
                    case "1":
                        Utils.print_BRANCO("1. BRANCO")
                        self.cor = "BRANCO"
                    case "2":
                        Utils.print_PRETO("2. PRETO")
                        self.cor = "PRETO"
                    case "3":
                        Utils.print_ROXO("3. ROXO")
                        self.cor = "ROXO"
                    case "4":
                        Utils.print_AMARELO("4. AMARELO")
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
            rodas = input("NÚMERO DE RODAS: ")
            system("clear")

            if Utils.valida_num_rodas(rodas):
                self.num_rodas = Utils.valida_num_rodas(rodas)
                print(f"NÚMERO DE RODAS: {self.num_rodas}")
                break
            else:
                print("OPÇÕES DISPONÍVEIS: 2 OU 3 RODAS")
                continue
        
        
        
        print("COMBUSTÍVEL PADRÃO DE MOTO/TRICICLO: GASOLINA".center(50, "-"))
        
        
        
        while True:
            print("POTÊNCIA".center(50, "-"))
            print("1. 150cc 14,2CV\n2. 250cc 22,4CV\n3. 650cc 88,4CV")

            potencia = input("Opção: ")
            system("clear")

            if potencia.isnumeric():
                if potencia == "1":
                    self.potencia = "150cc 14,2CV"
                    print(f"POTÊNCIA SELECIONADA: {self.potencia}")
                    break

                elif potencia == "2":
                    self.potencia = "250cc 22,4CV"
                    print(f"POTÊNCIA SELECIONADA: {self.potencia}")
                    break

                elif potencia == "3":
                    self.potencia = "650cc 88,4CV"
                    print(f"POTÊNCIA SELECIONADA: {self.potencia}")
                    break

                else:
                    print("Opção inválida")
            else:
                print("Opção numérica inválida")
        
        
        motoca = {
            "tipo": "Moto/Triciclo",
            "chassi": self.chassi,
            "data_fab": self.data_fab,
            "modelo": self.modelo,
            "placa": self.placa,
            "valor": self.valor,
            "cpf_compr": self.cpf_compr,
            "cor": self.cor,
            "num_rodas": self.num_rodas,
            "combustivel": self.combustivel,
            "potencia": self.potencia         
        }

        Database.adicionar_veiculo(veiculo=motoca)

    def listar_infos(self):
        Database.listar_VEICULOS("Moto/Triciclo")

    def alterar_infos(self):
        print("LISTANDO MOTOS / TRICICLOS VENDIDOS".center(50, "-"))
        
        
        while True:
            Database.listar_VEICULOS("Moto/Triciclo")
            placa = input("DIGITE A PLACA: ANTIGA OU MERCOSUL: ").upper()
            system("clear")

            if not Utils.valida_placa(placa):
                print("DIGITE UMA PLACA CORRETA")
                print("DEVE SER NO FORMATO ANTIGO MMM0000")
                print("OU NO FORMATO MERCOSUL: MMM0M00")
                continue
            else:
                print("PROCURANDO MOTO/TRICICLO NA BASE DE DADOS".center(50, "-"))

                if Database.existe_PLACA(placa=placa):
                    if Database.busca_por_PLACA(placa=placa, tipo="Moto/Triciclo"):
                        self.placa = placa
                        break
                    else:
                        print(f"PLACA {placa} PERTENCE A OUTRA CATEGORIA DE VEÍCULO.")
                        continue
                    
                else:
                    print("PLACA NÃO ENCONTRADA")
        

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
            valor = input("DIGITE O VALOR: R$: ")
            system("clear")

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
        
        
        if Database.busca_por_PLACA(placa=self.placa, tipo="Moto/Triciclo"):
            Database.alterar_VEICULO(placa=self.placa, cor=self.cor, valor=valor)
        else:
            print(f"MOTO NÃO PERMITE MODIFICAR PLACA DE OUTROS TIPOS DE VEICULO")


MOTO = MotoTriciclo()
#MOTO.vender_veiculo()
MOTO.listar_infos()
#MOTO.alterar_infos()