from operator import truediv
from tinydb import TinyDB, Query


carros = TinyDB("carros.json")


class Database:

    @staticmethod
    def adicionar_veiculo(veiculo: dict):
        carros.insert(veiculo)
    

    @staticmethod
    def listar_infos():
        todos = carros.all()

        if todos:
            for carro in carros:
                print(carro) 
        else:
            print("Lista Vazia")
    
    @staticmethod
    def listar_VEICULOS(tipo: str):
        busca = Query()
    
        lista = carros.search(busca.tipo == tipo)
        
        if lista:
            for carro in lista:
                print(carro)
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
    def alterar_VEICULO(placa: str, cor: str, valor: float):
        search = Query()

        carros.update({"cor": cor, "valor": valor}, search.placa == placa)




#Database.listar_infos()
#print(Database.existe_PLACA("BMM8S88"))
#print(Database.busca_por_PLACA("BMM8S88", "Carro"))