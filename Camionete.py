from Veiculo import Veiculo

class Camionete(Veiculo):
    def __init__(self) -> None:
        super().__init__(self.chassi, self.data_fab, self.nome, self.placa, self.valor, self.cpf_compr, self.cor)

        self.portas = None
        self.cacamba = None
        self.potencia = None
        self.combustivel = None

    def vender_veiculo(self):
        pass

    def listar_infos(self):
        pass

    def alterar_infos(self):
        pass
    