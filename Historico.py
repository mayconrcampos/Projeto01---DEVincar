from Carro import Carro
from MotoTriciclo import MotoTriciclo
from Camionete import Camionete
from Database import Database

class Historico:
    def __init__(self) -> None:
        pass
    
    def listar_todos_veiculos(self, tipo: str = ""):
        if tipo:
            Database.listar_VEICULOS(tipo)
        else:
            Database.listar_infos()

    def carros_disponiveis(self):
        pass

    def carros_vendidos(self):
        pass

    def carro_maior_preco(self):
        pass

    def carro_menor_preco(self):
        pass


#his = Historico()
#his.listar_todos_veiculos()