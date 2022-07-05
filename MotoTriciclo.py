from Veiculo import Veiculo

class MotoTriciclo(Veiculo):
    def __init__(self) -> None:
        super().__init__(self.chassi, self.data_fab, self.nome, self.placa, self.valor, self.cpf_compr, self.cor)

        self.potencia = None
        self.num_rodas = None
    
    def vender_veiculo(self):
        pass

    def listar_infos(self):
        pass

    def alterar_infos(self):
        pass
