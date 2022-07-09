
from email import utils
from tinydb import TinyDB, Query

from utils import Utils


carros = TinyDB("carros.json")


class Database:

    @staticmethod
    def adicionar_veiculo(veiculo: dict):
        carros.insert(veiculo)
    

    @staticmethod
    def listar_mais_CARO_OU_MAIS_BARATO(vendido: bool, caro: bool):
        veiculos = carros.all()

        if veiculos:
            # SE FOR VENDIDO
            if vendido:
                # SE FOR CARO
                if caro:
                    VENDIDOS = []
                    for veiculo in carros:
                        if veiculo['vendido']:
                            VENDIDOS.append(veiculo) 
    
                    if len(VENDIDOS) > 0:
                        valores = [x['valor'] for x in VENDIDOS]
                        mais_caro = None
                        for _ in range(0, len(VENDIDOS)):
                            if VENDIDOS[_]['valor'] == max(valores):
                                mais_caro = VENDIDOS[_]
                            
                    Utils.print_formatado("VEICULO VENDIDO MAIS CARO")
                    print(f"TIPO: {mais_caro['tipo']} MODELO: {mais_caro['modelo']} \nPOTENCIA: {mais_caro['potencia']} COMBUSTIVEL: {mais_caro['combustivel']} VALOR: \nR${mais_caro['valor']:.2f}\n")
                    Utils.print_formatado("-")
                    print("VALOR: R$ ", end=" --> ")
                    Utils.valor_por_extenso(str(mais_caro['valor']))
                    print("\n\n\n")
                
                # SE FOR BARATO
                else:
                    VENDIDOS = []
                    for veiculo in carros:
                        if veiculo['vendido']:
                            VENDIDOS.append(veiculo) 
    
                    if len(VENDIDOS) > 0:
                        valores = [x['valor'] for x in VENDIDOS]
                        mais_barato = None
                        for _ in range(0, len(VENDIDOS)):
                            if VENDIDOS[_]['valor'] == min(valores):
                                mais_barato = VENDIDOS[_]
    
                    Utils.print_formatado("VEICULO VENDIDO MAIS BARATO")
                    print(f"TIPO: {mais_barato['tipo']} MODELO: {mais_barato['modelo']} \nPOTENCIA: {mais_barato['potencia']} COMBUSTIVEL: {mais_barato['combustivel']} VALOR: \nR${mais_barato['valor']:.2f}\n")
                    Utils.print_formatado("-")
                    print("VALOR: R$ ", end=" --> ")
                    Utils.valor_por_extenso(str(mais_barato['valor']))
                    print("\n\n\n")


            # SE FOR EM ESTOQUE
            else:
                if caro:
                    ESTOQUE = []
                    for veiculo in carros:
                        if not veiculo['vendido']:
                            ESTOQUE.append(veiculo) 
    
                    if len(ESTOQUE) > 0:
                        valores = [x['valor'] for x in ESTOQUE]
                        mais_caro = None
                        for _ in range(0, len(ESTOQUE)):
                            if ESTOQUE[_]['valor'] == max(valores):
                                mais_caro = ESTOQUE[_]
                                break
    
                    Utils.print_formatado("VEICULO EM ESTOQUE MAIS CARO")
                    print(f"TIPO: {mais_caro['tipo']} MODELO: {mais_caro['modelo']} \nPOTENCIA: {mais_caro['potencia']} COMBUSTIVEL: {mais_caro['combustivel']} VALOR: \nR${mais_caro['valor']:.2f}\n")
                    Utils.print_formatado("-")
                    print("VALOR: R$ ", end=" --> ")
                    Utils.valor_por_extenso(str(mais_caro['valor']))
                    print("\n\n\n")
                
                # SE FOR BARATO
                else:
                    ESTOQUE = []
                    for veiculo in carros:
                        if not veiculo['vendido']:
                            ESTOQUE.append(veiculo) 
    
                    if len(ESTOQUE) > 0:
                        valores = [x['valor'] for x in ESTOQUE]
                        mais_barato = None
                        for _ in range(0, len(ESTOQUE)):
                            if ESTOQUE[_]['valor'] == min(valores):
                                mais_barato = ESTOQUE[_]
    
                    Utils.print_formatado("VEICULO EM ESTOQUE MAIS BARATO")
                    print(f"TIPO: {mais_barato['tipo']} MODELO: {mais_barato['modelo']} \nPOTENCIA: {mais_barato['potencia']} COMBUSTIVEL: {mais_barato['combustivel']} VALOR: \nR${mais_barato['valor']:.2f}\n")
                    Utils.print_formatado("-")
                    print("VALOR: R$ ", end=" --> ")
                    Utils.valor_por_extenso(str(mais_barato['valor']))
                    print("\n\n\n")
 
        else:
            print("NÃO EXISTEM CARROS CADASTRADOS")
            
    
    @staticmethod
    def listar_VEICULOS(tipo: str, status: str = "vendido"):
        busca = Query()
    
        lista = carros.search(busca.tipo == tipo)
        
        if lista:
            # ITENS EM ESTOQUE
            if status == "estoque":
                Utils.print_formatado(f"LISTANDO TODOS OS VEICULOS EM ESTOQUE DA CATEGORIA: {tipo}")
                total_estoque = 0
                unidades = 0

                if tipo == "Carro":
                    for veiculo in lista:
                        if not veiculo['vendido']:
                            total_estoque += veiculo['valor']
                            unidades += 1
                            Utils.print_formatado("-")
                            print(f"TIPO  : {veiculo['tipo']:<7} CHASSI: {veiculo['chassi']:<25} DATA FAB: {veiculo['data_fab']:<15} MODELO: {veiculo['modelo']:<30}")
                            print(f"PLACA : {'0KM' if not veiculo['placa'] else veiculo['placa']:<7} VALOR (R$): {veiculo['valor']:<21.2f} CPF: {'N/D' if not veiculo['cpf_compr'] else veiculo['cpf_compr']:<20} COR: {veiculo['cor']}")
                            print(f"PORTAS: {'N/D' if not veiculo['portas'] else veiculo['portas']:<7} COMBUSTIVEL: {veiculo['combustivel']:<20} POTENCIA: {veiculo['potencia']:<15} STATUS: {'Vendido' if veiculo['vendido'] else 'ESTOQUE'}\n")
                
                elif tipo == "Moto/Triciclo":
                    for veiculo in lista:
                        if not veiculo['vendido']:
                            total_estoque += veiculo['valor']
                            unidades += 1
                            Utils.print_formatado("-")
                            print(f"TIPO  : {veiculo['tipo']:<7} CHASSI: {veiculo['chassi']:<25} DATA FAB: {veiculo['data_fab']:<15} MODELO: {veiculo['modelo']:<30}")
                            print(f"PLACA : {'0KM' if not veiculo['placa'] else veiculo['placa']:<7} VALOR (R$): {veiculo['valor']:<21.2f} CPF: {'N/D' if not veiculo['cpf_compr'] else veiculo['cpf_compr']:<20} COR: {veiculo['cor']}")
                            print(f"Nº RODAS: {veiculo['num_rodas']:<7} COMBUSTIVEL: {veiculo['combustivel']:<20} POTENCIA: {veiculo['potencia']:<15} STATUS: {'Vendido' if veiculo['vendido'] else 'ESTOQUE'}\n")

                else:
                    for veiculo in lista:
                        if not veiculo['vendido']:
                            total_estoque += veiculo['valor']
                            unidades += 1
                            Utils.print_formatado("-")
                            print(f"TIPO  : {veiculo['tipo']:<15} CHASSI: {veiculo['chassi']:<25} DATA FAB: {veiculo['data_fab']:<15} MODELO: {veiculo['modelo']:<30}")
                            print(f"PLACA : {'0KM' if not veiculo['placa'] else veiculo['placa']:<15} VALOR (R$): {veiculo['valor']:<21.2f} CPF: {'N/D' if not veiculo['cpf_compr'] else veiculo['cpf_compr']:<20} COR: {veiculo['cor']}")
                            print(f"PORTAS: {veiculo['portas']:<15} COMBUSTIVEL: {veiculo['combustivel']:<20} POTENCIA: {veiculo['potencia']:<15} STATUS: {'Vendido' if veiculo['vendido'] else 'ESTOQUE'}\nCACAMBA: {veiculo['cacamba']}")
                    
                
                if total_estoque > 0:
                    print(f"TOTAL EM ESTOQUE NA CATEGORIA {tipo}")
                    Utils.print_formatado("-")
                    print(f"UNIDADES            : {unidades:>85}")
                    print(f"TOTAL R$            : {total_estoque:>85.2f}\n")
                    print("TOTAL EM ESTOQUE: ", end=" -> ")
                    Utils.valor_por_extenso(str(total_estoque))
                    print("\n\n\n")
                else:
                    print(f"NÃO HÁ ITENS DA CATEGORIA {tipo} NO ESTOQUE. VOCÊ PRECISA FABRICAR")
            
            # ITENS VENDIDOS
            else:
                Utils.print_formatado(f"LISTANDO TODOS OS VEICULOS VENDIDOS DA CATEGORIA: {tipo}")
                total_vendidos = 0
                unidades = 0

                if tipo == "Carro":
                    for veiculo in lista:
                        if veiculo['vendido']:
                            total_vendidos += veiculo['valor']
                            unidades += 1
                            Utils.print_formatado("-")
                            print(f"TIPO  : {veiculo['tipo']:<7} CHASSI: {veiculo['chassi']:<25} DATA FAB: {veiculo['data_fab']:<15} MODELO: {veiculo['modelo']:<30}")
                            print(f"PLACA : {'0KM' if not veiculo['placa'] else veiculo['placa']:<7} VALOR (R$): {veiculo['valor']:<21.2f} CPF: {'N/D' if not veiculo['cpf_compr'] else veiculo['cpf_compr']:<20} COR: {veiculo['cor']}")
                            print(f"PORTAS: {'N/D' if not veiculo['portas'] else veiculo['portas']:<7} COMBUSTIVEL: {veiculo['combustivel']:<20} POTENCIA: {veiculo['potencia']:<15} STATUS: {'Vendido' if veiculo['vendido'] else 'ESTOQUE'}\n")
                            
                elif tipo == "Moto/Triciclo":
                    for veiculo in lista:
                        if veiculo['vendido']:
                            total_vendidos += veiculo['valor']
                            unidades += 1
                            Utils.print_formatado("-")
                            print(f"TIPO  : {veiculo['tipo']:<7} CHASSI: {veiculo['chassi']:<25} DATA FAB: {veiculo['data_fab']:<15} MODELO: {veiculo['modelo']:<30}")
                            print(f"PLACA : {'0KM' if not veiculo['placa'] else veiculo['placa']:<7} VALOR (R$): {veiculo['valor']:<21.2f} CPF: {'N/D' if not veiculo['cpf_compr'] else veiculo['cpf_compr']:<20} COR: {veiculo['cor']}")
                            print(f"Nº RODAS: {veiculo['num_rodas']:<7} COMBUSTIVEL: {veiculo['combustivel']:<20} POTENCIA: {veiculo['potencia']:<15} STATUS: {'Vendido' if veiculo['vendido'] else 'ESTOQUE'}\n")
                else:
                    pass
                
                if total_vendidos > 0:
                    print(f"TOTAL FATURADO NA CATEGORIA {tipo}")
                    Utils.print_formatado("-")
                    print(f"UNIDADES    : {unidades:>100}")
                    print(f"TOTAL R$    : {total_vendidos:>100.2f}\n")
                    print("TOTAL FATURADO: ", end=" -> ")
                    Utils.valor_por_extenso(str(total_vendidos))
                    print("\n\n\n")
                else:
                    print(f"NÃO EXISTEM ITENS DA CATEGORIA {tipo} VENDIDOS")
                    

        else:
            print(f"VEÍCULO TIPO: {tipo} NÃO ENCONTRADO")
    
    @staticmethod
    def existe_PLACA(placa: str):
        busca = Query()

        lista = carros.search(busca.placa == placa)

        if lista:
            return True
        else:
            return False
    
    @staticmethod
    def busca_por_PLACA(placa: str, tipo: str):
        busca = Query()
                
        lista = carros.search(busca.placa == placa)
    
        if lista:
            existe = False
            obj = ""
            for c in lista:
                if c["tipo"] == tipo:
                    existe = True
                    obj = c
            
            if existe:
                return obj
            else:
                return False

        else:
            print(f"PLACA INEXISTENTE OU CATEGORIA DIFERENTE")
            return False
    
    @staticmethod
    def busca_por_chassi(chassi: str, tipo: str):
        busca = Query()
                
        lista = carros.search(busca.chassi == chassi)
    
        if lista:
            existe = False
            obj = ""
            for c in lista:
                if c["tipo"] == tipo and not c['vendido']:
                    existe = True
                    obj = c
            
            if existe:
                return obj
            else:
                return False

        else:
            print(f"CHASSI INEXISTENTE OU CATEGORIA DIFERENTE")
            return False
       

    
    @staticmethod
    def alterar_VEICULO(placa: str, cor: str, valor: float):
        search = Query()

        carros.update({"cor": cor, "valor": valor}, search.placa == placa)
    

    @staticmethod
    def vender_VEICULO(chassi: str, placa: str, cpf: str, portas: int = 0):
        search = Query()

        if portas:
            carros.update({"placa": placa, "cpf_compr": cpf, "portas": portas, "vendido": True}, search.chassi == chassi)
        else:
            carros.update({"placa": placa, "cpf_compr": cpf, "vendido": True}, search.chassi == chassi)
        



#print(Database.busca_por_chassi("OM4 NPKXDN ZE XDMABT", "Carro"))
#Database.listar_infos()
#print(Database.existe_PLACA("BMM8S88"))
#print(Database.busca_por_PLACA("BMM8S88", "Carro"))