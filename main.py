from ctypes import util
from Camionete import Camionete
from Carro import Carro
from MotoTriciclo import MotoTriciclo
from utils import Utils
from Historico import Historico

carro = Carro()
moto = MotoTriciclo()
camionete = Camionete()


def menu_fabricacao(unidades: int):
    while True:
        Utils.print_formatado("SELECIONE A CATEGORIA")
        Utils.print_formatado("1. CARRO")
        Utils.print_formatado("2. MOTO/TRICICLO")
        Utils.print_formatado("3. CAMIONETE")

        opcao_categoria = input("Opção: ")

        if opcao_categoria.isnumeric():
                                
            if opcao_categoria == "1":
                for _ in range(0, unidades):
                    carro.fabricar_veiculo()
                
                print(f"FORAM FABRICADOS {unidades} UNIDADES")
                break
                    
            elif opcao_categoria == "2":
                for _ in range(0, unidades):
                    carro.fabricar_veiculo()
                
                print(f"FORAM FABRICADOS {unidades} UNIDADES")
                break


            elif opcao_categoria == "3":
                for _ in range(0, unidades):
                    carro.fabricar_veiculo()
                
                print(f"FORAM FABRICADOS {unidades} UNIDADES")
                break
        else:
            print("Opção numérica inválida")




                         

while True:
    Utils.print_formatado("SISTEMA GERENCIADOR DE FABRICAÇÃO E VENDA DE VEÍCULOS - DEVinCAR")
    Utils.print_formatado("1. Fabricar Veículo")
    Utils.print_formatado("2. Listar veículos em Estoque")
    Utils.print_formatado("------------")
    Utils.print_formatado("3. Vender veículo")
    Utils.print_formatado("4. Listar veículos Vendidos")
    Utils.print_formatado("------------")
    Utils.print_formatado("5. Visualizar Veículo mais caro")
    Utils.print_formatado("6. Visualizar Veículo mais barato")
    Utils.print_formatado("------------")
    Utils.print_formatado("7. Sair do Sistema")

    opcao = input("Opção: ")

    if opcao.isnumeric():
        match opcao:
            case "1":
                while True:
                    Utils.print_formatado("SELECIONE A QUANTIDADE")
                    Utils.print_formatado("1. 10 UNIDADES")
                    Utils.print_formatado("2. 20 UNIDADES")
                    Utils.print_formatado("3. 50 UNIDADES")
                    Utils.print_formatado("4. RETORNAR AO MENU PRINCIPAL")

                    opcao_unidades = input("Opção: ")

                    unidades = 0

                    if opcao_unidades.isnumeric():

                        if opcao_unidades == "1":
                            unidades = 10

                            menu_fabricacao(unidades=unidades)

                        elif opcao_unidades == "2":
                            unidades = 20

                            menu_fabricacao(unidades=unidades)

                        elif opcao_unidades == "3":
                            unidades = 50

                            menu_fabricacao(unidades=unidades)

                        elif opcao_unidades == "4":
                            print("Retornando ao Menu Principal")
                            break
                        else:
                            print("Opção inválida!")
                    else:
                        print("Opção numérica inválida")

                    
            case "2":
                while True:
                    Utils.print_formatado("ESCOLHA A CATEGORIA PARA LISTAR O ESTOQUE")
                    Utils.print_formatado("1. CARRO")
                    Utils.print_formatado("2. MOTO")
                    Utils.print_formatado("3. CAMIONETE")
                    Utils.print_formatado("4. Retornar ao Menu Principal")

                    opcao = input("Opção: ")

                    if opcao.isnumeric():
                        if opcao == "1":
                            carro.listar_infos()
                        elif opcao == "2":
                            moto.listar_infos()
                        elif opcao == "3":
                            camionete.listar_infos()
                        elif opcao == "4":
                            print("RETORNANDO AO MENU PRINCIPAL")
                            break
                        else:
                            print("Opção inválida")
                    else:
                        print("Opção numérica inválida")
                    
                    
            case "3":
                while True:
                    Utils.print_formatado("ESCOLHA A CATEGORIA")
                    Utils.print_formatado("1. CARRO")
                    Utils.print_formatado("2. Moto/Triciclo")
                    Utils.print_formatado("3. Camionete")
                    Utils.print_formatado("4. RETORNAR AO MENU PRINCIPAL")

                    opcao = input("Opção: ")

                    if opcao.isnumeric():
                        if opcao == "1":
                            carro.vender_veiculo()
                        elif opcao == "2":
                            pass
                        elif opcao == "3":
                            pass
                        elif opcao == "4":
                            print("VOCÊ RETORNOU AO MENU PRINCIPAL")
                            break
                        else:
                            print("Opção inválida")
                    else:
                        print("Opção numérica inválida")
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "7":
                print("Você saiu do Sistema!")
                break
    else:
        print("Caracter inválido! Digite números inteiros para navegar no Menu.")