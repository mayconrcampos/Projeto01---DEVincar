from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self) -> None:
        self.chassi = str
        self.data_fab = str
        self.modelo = str
        self.placa = str
        self.valor = float
        self.cpf_compr = str
        self.cor = str
    
    @abstractmethod
    def vender_veiculo(self):
        pass
    
    @abstractmethod
    def listar_infos(self):
        pass 
    
    @abstractmethod
    def alterar_infos(self):
        pass