
from Camionete import Camionete
from Carro import Carro
from Database import Database
from MotoTriciclo import MotoTriciclo
from utils import Utils

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

        Utils.clear_tela()

        if opcao_categoria.isnumeric():
                                
            if opcao_categoria == "1":
                for _ in range(0, unidades):
                    carro.fabricar_veiculo()
                
                print(f"FORAM FABRICADOS {unidades} UNIDADES")
                break
                    
            elif opcao_categoria == "2":
                for _ in range(0, unidades):
                    moto.fabricar_veiculo()
                
                print(f"FORAM FABRICADOS {unidades} UNIDADES")
                break


            elif opcao_categoria == "3":
                for _ in range(0, unidades):
                    camionete.fabricar_veiculo()
                
                print(f"FORAM FABRICADOS {unidades} UNIDADES")
                break
        else:
            print("Opção numérica inválida")



    """
    MENU PRINCIPAL
    """

Utils.clear_tela()
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
    Utils.print_formatado("7. Alterar VEICULO COMPRADO")
    Utils.print_formatado("------------")
    Utils.print_formatado("8. Sair do Sistema")

    opcao = input("Opção: ")

    Utils.clear_tela()

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

                    Utils.clear_tela()

                    unidades = 0

                    if opcao_unidades.isnumeric():

                        if opcao_unidades == "1":
                            unidades = 10

                            menu_fabricacao(unidades=unidades)
                            break

                        elif opcao_unidades == "2":
                            unidades = 20

                            menu_fabricacao(unidades=unidades)
                            break

                        elif opcao_unidades == "3":
                            unidades = 50

                            menu_fabricacao(unidades=unidades)
                            break

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

                    Utils.clear_tela()

                    if opcao.isnumeric():
                        if opcao == "1":
                            carro.listar_infos("estoque")
                            break

                        elif opcao == "2":
                            moto.listar_infos("estoque")
                            break

                        elif opcao == "3":
                            camionete.listar_infos("estoque")
                            break

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

                    Utils.clear_tela()

                    if opcao.isnumeric():
                        if opcao == "1":
                            carro.vender_veiculo()
                            break

                        elif opcao == "2":
                            moto.vender_veiculo()
                            break

                        elif opcao == "3":
                            camionete.vender_veiculo()
                            break

                        elif opcao == "4":
                            print("VOCÊ RETORNOU AO MENU PRINCIPAL")
                            break

                        else:
                            print("Opção inválida")
                    else:
                        print("Opção numérica inválida")
            case "4":
                while True:
                    Utils.print_formatado("ESCOLHA A CATEGORIA PARA LISTAR VEÍCULOS VENDIDOS")
                    Utils.print_formatado("1. CARRO")
                    Utils.print_formatado("2. Moto/Triciclo")
                    Utils.print_formatado("3. Camionete")
                    Utils.print_formatado("4. RETORNAR AO MENU PRINCIPAL")

                    opcao = input("Opção: ")

                    Utils.clear_tela()

                    if opcao.isnumeric():
                        if opcao == "1":
                            carro.listar_infos("vendido")
                            break
                        \
                        elif opcao == "2":
                            moto.listar_infos("vendido")
                            break

                        elif opcao == "3":
                            camionete.listar_infos("vendido")
                            break

                        elif opcao == "4":
                            print("VOCÊ RETORNOU AO MENU PRINCIPAL")
                            break
                        else:
                            print("Opção inválida")
                    else:
                        print("Opção numérica inválida")
            case "5":
                while True:
                    print("VISUALIZANDO VEÍCULO MAIS CARO")
                    Utils.print_formatado("1. EM ESTOQUE")
                    Utils.print_formatado("2. VENDIDOS")
                    
                    opcao = input("Opção: ")

                    Utils.clear_tela()

                    if opcao.isnumeric():
                        if opcao == "1":
                            Database.listar_mais_CARO_OU_MAIS_BARATO(vendido=False, caro=True)
                            break

                        elif opcao == "2":
                            Database.listar_mais_CARO_OU_MAIS_BARATO(vendido=True, caro=True)
                            break
                        else:
                            print("Opção inválida!")
                    else:
                        print("Opção numérica inválida")
            case "6":
                while True:
                    print("VISUALIZANDO VEÍCULO MAIS BARATO")
                    Utils.print_formatado("1. EM ESTOQUE")
                    Utils.print_formatado("2. VENDIDOS")
                    
                    opcao = input("Opção: ")

                    Utils.clear_tela()

                    if opcao.isnumeric():
                        if opcao == "1":
                            Database.listar_mais_CARO_OU_MAIS_BARATO(vendido=False, caro=False)
                            break

                        elif opcao == "2":
                            Database.listar_mais_CARO_OU_MAIS_BARATO(vendido=True, caro=False)
                            break
                        else:
                            print("Opção inválida!")
                    else:
                        print("Opção numérica inválida")
            case "7":
                while True:
                    print("ALTERAR COR E VALOR DE VEICULO VENDIDO")
                    Utils.print_formatado("SELECIONE A CATEGORIA")
                    Utils.print_formatado("1. CARRO")
                    Utils.print_formatado("2. MOTO")
                    Utils.print_formatado("3. CAMIONETE")
                    Utils.print_formatado("4. RETORNAR AO MENU PRINCIPAL")
                    
                    opcao = input("Opção: ")

                    Utils.clear_tela()

                    if opcao.isnumeric():
                        if opcao == "1":
                            carro.alterar_infos()
                            break

                        elif opcao == "2":
                            moto.alterar_infos()
                            break

                        elif opcao == "3":
                            camionete.alterar_infos()
                            break

                        elif opcao == "4":
                            print("RETORNANDO AO MENU PRINCIPAL")
                            break

                        else:
                            print("Opção inválida!")
                    else:
                        print("Opção numérica inválida")
                

            case "8":
                print("Você saiu do Sistema!")
                break

            case _:
                print("Opção inválida!")
    else:
        print("Caracter inválido! Digite números inteiros para navegar no Menu.")