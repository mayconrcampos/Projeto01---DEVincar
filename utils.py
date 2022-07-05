from datetime import datetime
from random import randint

class Utils:

    @staticmethod
    def gera_chassi():
        chars = ['0', '1', '2', '3', '4', '5', '6', "7", '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Z']
        
        chassi = [chars[randint(1, len(chars) - 1)] for x in range(17)]

        chassi_str = ""
        for c in chassi:
            chassi_str += c
            if len(chassi_str) == 3:
                chassi_str += " "
            elif len(chassi_str) == 10:
                chassi_str += " "

            elif len(chassi_str) == 13:
                chassi_str += " "

        return chassi_str

    @staticmethod
    def valida_data(data: str):
        formato = "%d-%m-%Y"

        try:
            bool(datetime.strptime(data, formato))

            data_formatada = data.replace("-", "/")

            return data_formatada

        except ValueError:
            return False
    
    @staticmethod
    def valida_placa(placa: str):
        if len(placa) == 7:
            contLetra = 0
            contNum = 0
            for i, item in enumerate(placa):
                if item.isalpha() and (i == 0 or i == 1 or i == 2 or i ==4):
                    contLetra += 1
                elif item.isdigit() and (i == 3 or i == 4 or i == 5 or i == 6):
                    contNum += 1
 
 
            if (contLetra == 3 and contNum == 4) or (contLetra == 4 and contNum == 3):
                
                return placa.upper()
                
                 
            else:
                print('Placa inválida. Por favor, insira uma placa válida')
                return False
             
        else:
            print("Placa inválida. Por favor, insira uma placa válida:")
            return False
    
    @staticmethod
    def valida_valor(valor: str):
        try:
            for _ in valor:
                if _ in ",":
                    valor = valor.replace(",", ".")

            return float(valor)
            
        except ValueError:
            return False


    @staticmethod
    def valida_cpf(cpf_completo: str):
        if len(cpf_completo) == 11:
            '''Enche uma lista com todos os 11 dígitos.'''
            compara_cpf = []
            for num in cpf_completo:
                if num.isnumeric():
                    compara_cpf.append(int(num))

            '''Fatia a lista criada do índice 0 a 9'''
            cpflimpo = compara_cpf[0:9]

            '''Validando Décimo Dígito'''
            controle = 10
            soma = 0
            for numero in cpflimpo:
                multiplica = numero * controle
                soma += multiplica
                controle -= 1

            validando = 11 - (soma % 11)
            if validando > 9:
                validando = 0
                cpflimpo.append(validando)
            else:
                cpflimpo.append(validando)

            '''Validando Décimo Primeiro Dígito'''
            controle = 11
            soma = 0
            for numero in cpflimpo:
                multiplica = numero * controle
                soma += multiplica
                controle -= 1

            validando = 11 - (soma % 11)
            if validando > 9:
                validando = 0
                cpflimpo.append(validando)
            else:
                cpflimpo.append(validando)

            print('Resultado da Verificação de CPF!')
            print('-='*30)

            '''Abaixo tem uma estrutura que verifica se não se trata de uma sequencia de números iguais.'''
            repetido = []
            tudo_igual = 0
            conta = 0
            for i in compara_cpf:
                if i == compara_cpf[conta + 1]:
                    repetido.append(i)
            if len(repetido) == 11:
                tudo_igual = True

            '''
            Abaixo verifica se o compara_cpf e cpflimpo são iguais:
            Se forem iguais, e e repete for False, o CPF é válido.
            Se forem diferentes, o CPF é inválido.
            '''
            if compara_cpf == cpflimpo and not tudo_igual:
                print(f'O CPF: {cpflimpo} é válido!!')
            else:
                print(f'O CPF: {cpflimpo} não é válido!!')
        
        else:
            print("CPF inválido")


Utils.valida_cpf("03772137997")