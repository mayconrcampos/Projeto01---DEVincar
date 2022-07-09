from Veiculo import Veiculo
from utils import Utils
from Database import Database

class MotoTriciclo(Veiculo):
    def __init__(self) -> None:
        #super().__init__(self.chassi, self.data_fab, self.modelo, self.placa, self.valor, self.cpf_compr, self.cor)

        self.combustivel = None
        self.potencia = None
        self.num_rodas = None
    
    def fabricar_veiculo(self):
        self.chassi = Utils.gera_chassi()
        self.data_fab = Utils.gera_data_HOJE()
        self.modelo = Utils.gerador_de_modelo()
        self.placa = None
        self.potencia = Utils.setPotencia_MOTO()
        self.valor = Utils.gerador_de_valor_MOTO(self.potencia)
        self.cpf_compr = None
        self.cor = Utils.gera_COR()
        self.num_rodas = Utils.setNum_RODAS_MOTO_TRICICLO()
        self.combustivel = Utils.setCombustivel_MOTO()
        

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
            "potencia": self.potencia,
            "vendido": False         
        }

        Database.adicionar_veiculo(veiculo=motoca)

    
    def vender_veiculo(self):
        Utils.print_formatado("VENDA DE MOTO/TRICICLO")
        self.listar_infos("estoque")

        while True:
            chassi = input("DIGITE O CHASSI DO CARRO DESEJADO: (COPIE E COLE AQUI): ----> ").upper().strip()

            if chassi:
                busca = Database.busca_por_chassi(chassi, "Moto/Triciclo")

                if busca:
                    break
                else:
                    print("CHASSI NÃO ENCONTRADO")
            else:
                print("COPIE UM CHASSI DA LISTA DE CARROS E COLE NO INPUT")


        
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
            cpf_compr = input("DIGITE O CPF DO COMPRADOR: ")
            Utils.clear_tela()

            if not Utils.valida_cpf(cpf_completo=cpf_compr):
                print("DIGITE UM CPF VÁLIDO")
                print("CPF POSSUI 11 DÍGITOS")
                print("NÃO DIGITE OS PONTOS E O TRAÇO\n")

                while True:
                    gera_cpf = input("AO INVÉS DE DIGITAR, QUER GERAR UM CPF VÁLIDO?\n1. Gerar CPF\n2. Não! Quero Inserir meu CPF\n: ")
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


        Database.vender_VEICULO(chassi=chassi, placa=placa, cpf=self.cpf_compr)

    def listar_infos(self, status: str):
        Database.listar_VEICULOS("Moto/Triciclo", status=status)

    def alterar_infos(self):
        print("LISTANDO MOTOS / TRICICLOS VENDIDOS".center(50, "-"))
        
        
        while True:
            self.listar_infos("vendido")
            placa = input("DIGITE A PLACA: ANTIGA OU MERCOSUL:\n --> COPIE A PLACA DESEJADA DA LISTA E COLE AQUI --> ").upper()
            Utils.clear_tela()

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
            Utils.clear_tela()

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
                            Utils.clear_tela()

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
        
        
        Database.alterar_VEICULO(placa=self.placa, cor=self.cor, valor=self.valor)
        

