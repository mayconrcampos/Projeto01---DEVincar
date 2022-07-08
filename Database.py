
from tinydb import TinyDB, Query

from utils import Utils


carros = TinyDB("carros.json")


class Database:

    @staticmethod
    def adicionar_veiculo(veiculo: dict):
        carros.insert(veiculo)
    

    @staticmethod
    def listar_infos():
        veiculos = carros.all()

        if veiculos:
            valores = []
            for veiculo in carros:
                print(veiculo)
                valores.append(veiculo['valor']) 
            
            return [sum(valores), max(valores), min(valores)]
        else:
            print("Lista Vazia")
    
    @staticmethod
    def listar_VEICULOS(tipo: str):
        busca = Query()
    
        lista = carros.search(busca.tipo == tipo)
        
        if lista:
            Utils.print_formatado(f"LISTANDO TODOS OS VEICULOS DA CATEGORIA: {tipo}")
            for veiculo in lista:
                Utils.print_formatado("-")
                print(f"TIPO  : {veiculo['tipo']:<7} CHASSI: {veiculo['chassi']:<25} DATA FAB: {veiculo['data_fab']:<15} MODELO: {veiculo['modelo']:<30}")
                print(f"PLACA : {'0KM' if not veiculo['placa'] else veiculo['placa']:<7} VALOR (R$): {veiculo['valor']:<21.2f} CPF: {'N/D' if not veiculo['cpf_compr'] else veiculo['cpf_compr']:<20} COR: {veiculo['cor']}")
                print(f"PORTAS: {'N/D' if not veiculo['portas'] else veiculo['portas']:<7} COMBUSTIVEL: {veiculo['combustivel']:<20} POTENCIA: {veiculo['potencia']:<15} STATUS: {'Vendido' if veiculo['vendido'] else 'ESTOQUE'}\n")
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
    def vender_VEICULO(chassi: str, placa: str, cpf: str, portas: int):
        search = Query()

        carros.update({"placa": placa, "cpf_compr": cpf, "portas": portas, "vendido": True}, search.chassi == chassi)



print(Database.busca_por_chassi("OM4 NPKXDN ZE XDMABT", "Carro"))
#Database.listar_infos()
#print(Database.existe_PLACA("BMM8S88"))
#print(Database.busca_por_PLACA("BMM8S88", "Carro"))