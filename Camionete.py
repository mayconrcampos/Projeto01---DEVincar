from Veiculo import Veiculo
from utils import Utils
from Database import Database

class Camionete(Veiculo):
    def __init__(self) -> None:
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
        self.portas = None
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
        Utils.print_formatado("VENDA DE CAMIONETE")
        
        existe = True
        if not self.listar_infos("estoque"):
            existe = False
        
        while existe:
            chassi = input("DIGITE O CHASSI DO CARRO DESEJADO: (COPIE E COLE AQUI): ----> ").upper().strip()

            if chassi:
                busca = Database.busca_por_chassi(chassi, "Camionete")

                if busca:
                    self.chassi = chassi
                    break
                else:
                    print("CHASSI NÃO ENCONTRADO")
            else:
                print("COPIE UM CHASSI DA LISTA DE CARROS E COLE NO INPUT")


       
        
        while existe:
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
        
        
        while existe:
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

       

        while existe:
            Utils.print_formatado("PENSE BEM ANTES DE ESCOLHER A COR DA CAMIONETE")
   
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
        
        while existe:
            portas = input("NÚMERO DE PORTAS: ")
            Utils.clear_tela()

            if Utils.valida_portas(portas):
                self.portas = Utils.valida_portas(portas)
                print(f"PORTAS: {self.portas}")
                break
            else:
                print("OPÇÕES DISPONÍVEIS: 2 OU 4 PORTAS")
                continue
  
        if existe:
            Database.vender_VEICULO(chassi=self.chassi, placa=self.placa, cpf=self.cpf_compr, portas=self.portas)
        else:
            print("NÃO EXISTEM CAMIONETES NO ESTOQUE")

    def listar_infos(self, status: str):
        if Database.listar_VEICULOS("Camionete", status=status):
            return True
        return False

    def alterar_infos(self):
        print("LISTANDO CAMIONETES VENDIDAS".center(50, "-"))

        existe = False
        if self.listar_infos("vendido"):
            existe = True
            Utils.clear_tela()
        
        while existe:
            self.listar_infos("vendido")
            placa = input("DIGITE A PLACA: ANTIGA OU MERCOSUL:\n --> COPIE A PLACA DESEJADA DA LISTA E COLE AQUI --> ").upper().strip()
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
        

        while existe:
            Utils.print_formatado("PARECE QUE VOCÊ SE ARREPENDEU DE TER ESCOLHIDO ROXO, NÃO É VERDADE?")
            print("ENTÃO ESCOLHA OUTRA COR".center(50, "-"))
            Utils.print_ROXO("1. ROXO")
            print("2. TÁ INDECISO? TENTE ESCOLHER OUTRA ENTÃO!")

            opcao_cor = input("Opção: ")
            Utils.clear_tela()

            if opcao_cor.isnumeric():
                match opcao_cor:
                    case "1":
                        Utils.print_ROXO("1. ROXO DE NOVO? VOCÊ TEM UM ÓTIMO GOSTO!")
                        self.cor = "ROXO"
                        break

                    case "2":
                        Utils.trava_lingua()

                    case _:
                        print("Opção inválida")
                
            else:
                print("Opção numérica inválida")

        
        if existe:
            Database.alterar_VEICULO(placa=self.placa, cor=self.cor)
        else:
            print(f"NÃO EXISTE NENHUMA CAMIONETE VENDIDA")
