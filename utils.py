from datetime import datetime
from random import randint
from faker import Faker
from faker_vehicle import VehicleProvider
from os import system, name
from num2words import num2words

fake = Faker(["pt-BR", "pt-BR", "pt-BR", "pt-BR"])
fake.add_provider(VehicleProvider)

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
    def gera_data_HOJE():
        ano = datetime.today().year 
        mes =  f"0{datetime.today().month}" if datetime.today().month < 10 else datetime.today().month
        dia =  f"0{datetime.today().day}" if datetime.today().day < 10 else datetime.today().day

        return f"{dia}/{mes}/{ano}"
    
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
                cpf = ""
                
                for num in cpflimpo:
                    cpf += f"{num}"
                    

                    if len(cpf) == 3 or len(cpf) == 7:
                        cpf += "."
                    elif len(cpf) == 11:
                        cpf += "-"
                        
                return cpf

                
            else:
                return False
        
        else:
            return False
    

    @staticmethod
    def gera_cpf():
        cpf_completo = []
        for i in range(0, 12):
            nums_aleatorios = randint(0, 9)
            cpf_completo.append(str(nums_aleatorios))

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
        
        """
        Transformando lista em string do CPF formatado com pontos e o traço
        """
        cpf_formatado_str = ""
        
        for n in cpflimpo:
            cpf_formatado_str += f"{n}"

            if len(cpf_formatado_str) == 3 or len(cpf_formatado_str) == 7:
                cpf_formatado_str += "."
            elif len(cpf_formatado_str) == 11:
                cpf_formatado_str += "-"
        

        return cpf_formatado_str

    @staticmethod
    def sortear_cor():
        cores = ["BRANCO", "PRETO", "ROXO", "AMARELO"]

        return cores[randint(0, 3)]
    
    @staticmethod
    def valida_portas(num: str):
        try:
            num = int(num)

            if num == 2 or num == 4:
                return num
            else:
                return False
                
        except ValueError:
            print("Número inválido")
    
    @staticmethod
    def valida_num_rodas(num: str):
        try:
            num = int(num)

            if num == 2 or num == 3:
                return num
            else:
                return False
                
        except ValueError:
            print("Número inválido")
    
       
    @staticmethod
    def trava_lingua():
        frases = ["O rato roeu a roupa do Rei de Roma e a rainha com raiva resolveu remendar.", "A Iara agarra e amarra a rara arara de Araraquara.", "Toco preto, porco fresco, corpo crespo.", "Lalá, Lelé e Lili e suas filhas, Lalalá, Lelelé e Lilili e suas netas Lalelá, Lelalé e Lelali e suas bisnetas Lilelá, Lalilé e Lelali e suas tataranetas Laleli, Lilalé e Lelilá cantavam em coro LÁLÁLÁLÉLÉLÉLILILI.", "Fala, arara loura. A arara loura falará.", "Paulo Pereira Pinto Peixoto, pobre pintor português, pinta perfeitamente portas, paredes e pias. Por Evaí Oliveira, por parco preço, patrão.", "Bagre branco, branco bagre.", "Chega de cheiro de cera suja.", "É crocogrilo? É cocodrilo? É cocrodilo? É cocodilho? É corcodilho? É crocrodilo? É crocrodilho? É corcrodilo? É cocordilo? É jacaré? Será que ninguém acerta O nome do crocodilo mané?", "A batina do padre Pedro é preta;", "Não confunda ornitorrinco com otorrinolaringologista, ornitorrinco com ornitologista, ornitologista com otorrinolaringologista, porque ornitorrinco, é ornitorrinco, ornitologista, é ornitologista, e otorrinolaringologista é otorrinolaringologista;", "Atrás da pia tem um prato, um pinto e um gato.", "Palma, palminha, Palminha de Guiné, para quando papai vier, mamãe dá a papinha, vovó bate cipó, na bundinha do nenê.", "O Papa papa o papo do pato.", '    A vaca malhada foi molhada por outra vaca molhada e malhada.\n', '    Enquanto Orsine bala dava, o sino badalava.\n', '    Maria-mole é molenga. Se não é molenga não é maria-mole. É coisa malemolente, nem mala, nem mola, nem Maria, nem mole.\n', '    O rato roeu a rolha da garrafa de rum do rei da Rússia\n', '    Três pratos de trigo para três tigres tristes.\n', '    Norma nina o nenê de Neuza.\n', '    O Juca ajuda: encaixa a caixa, agacha, engraxa.\n', '    Paraquedista brinquedista faz brinquedo paraquedista paraqueda brinquedista.\n', '    A rua de paralelepípedo é toda paralelepipedada.\n', '    Abadalado, Ababadado, Ababelado, Abobadado.\n', '    A aranha arranha a rã. A rã arranha a aranha. Nem a aranha arranha a rã. Nem a rã arranha a aranha.\n', '    O doce perguntou pro doce, qual é o doce mais doce que o doce de batata-doce. O doce respondeu pro doce, que o doce mais doce que o doce de batata-doce. É o doce de doce de batata-doce.\n', "    Pardal pardo, por que sempre palras? Palro sempre e palrarei, porque sou pardal pardo. O palrador d'el-rei.\n", '    Tal tatu tá tendo um treme traco troco treco por tramoia trava-línguas por Evaí Oliveira com a traquina da jiboia. E a jiboia que não boia sempre zoia tal tatu com seu balaio tal qual paca do soslaio;\n', '    O Tempo perguntou pro tempo quanto tempo o tempo tem, o tempo respondeu pro tempo que o tempo tem o tempo que o tempo tem;\n', '    Se o Papa papasse papa. Se o Papa papasse pão. O Papa tudo papava. Seria o Papa papão.\n', '    Se a liga me ligasse, eu ligava a liga, mas como a liga não me liga, eu não ligo a liga;\n', '    A pia pinga, o pinto pia, pinga a pia, pia o pinto, o pinto perto da pia, a pia perto do pinto.\n', '    Lanço o laço no salão. O lenço, lanço. A lança, não.\n', '    A babá boba bebeu o leite do bebê.\n', '    Um limão, mil limões, um milhão de limões.\n', '    Caixa de graxa grossa de graça.\n', '    Atrás da porta torta tem uma porca morta.\n', '    Se o papa papasse pão.\n', '    É preto o prato do pato preto.\n', '    Rosa vai dizer à Rita que o rato roeu a roupa da rainha.\n', '    A chave do chefe Chaves, está no chaveiro.\n', '    O Pedro pregou um prego na pedra.\n', '    O rato roeu o rabo da raposa.\n', '    Tigelinha de água fria, que caiu da prateleira, foi nos olhos de Maria, que chorou segunda-feira.\n', '    Chuva e sol, casamento de espanhol.\n', '    Pedro o pintor pinta o quadro do pintor paulo e paulo o pintor pinta o quadro do pato pedreiro.\n', '    O palhaço foi no palácio fazer palhaçada para o rei que do palácio expulsou o engraçado palhaço.\n', '    Bote a bota no bode e tira o pote do bode.\n', '    Gato escondido com rabo de fora está mais escondido que rabo escondido com gato de fora.\n', '    Enquanto Bia brinca, Bianca briga.\n', '    O dedo do Dudu é duro.\n', '    É muito socó para um socó só coçar.\n', '    O rei de Roma ruma a Madri.\n', '    Como a liga não me liga, eu também não ligo a liga.\n', '    Quando digo "digo", digo "digo. Não digo "Diogo". Quando digo "Diogo", digo "Diogo". Não digo "digo".\n', '    Não sei se é fato ou se é fita. Não sei se é fita ou fato. O fato é que você me fita e fita mesmo de fato.\n', '    Alô, o tatu tá ai? – Não, o tatu não tá. Mas a mulher do tatu tando, é o mesmo que o tatu tá.\n', '    A Iara agarra e amarra a rara arara de Araraquara.\n', '    O sabiá não sabia que o sábio sabia que o sabiá não sabia assobiar.\n', '    Embaixo da pia tem um pinto que pia, quanto mais a pia pinga mais o pinto pia.\n', '    O padre pouca capa tem, porque pouca capa compra.\n', '    Farofa feita com muita farinha fofa faz uma fofoca feia.\n', '    O que é que Cacá quer? Cacá quer caqui. Qual caqui que Cacá quer? Cacá quer qualquer caqui.\n', '    Luzia lustrava o lustre listrado, o lustre listrado luzia.\n', '    Uma trinca de trancas trancou Tancredo.\n', '    A Cuca cutuca a criança; A Cuca cutuca o Caqui; O Cucu cutuca a Cuca; A Cuca cutuca o Saci; A Cuca cutuca a arapuca da Tuca.\n', '    A fiadeira fia a farda do filho do feitor Felício.\n', '    Lá vem o velho Félix, com um fole velho nas costas, tanto fede o velho Félix, como o fole do velho Félix fede.\n', '    Lá de trás de minha casa tem um pé de umbu butando Umbu verde, umbu maduro, Umbu seco, umbu secando.\n', '    Biblioteca, bicicleta Sabrininha é sapeca bicicleta, biblioteca Sabrininha come bisteca bistequinha da Sabrina que anda de bicicleta e lê na biblioteca.\n', '    O seu Tatá tá? Não, o seu Tatá não tá, Mas a mulher do seu Tatá tá. E quando a mulher do seu Tatá tá, É a mesma coisa que o seu Tatá tá,tá?\n', '    Quem a paca cara compra, caro a paca pagará.\n', '    Larga a tia, largatixa! Lagartixa, larga a tia! Só no dia em que a sua tia chamar a largatixa de lagartixa.\n', '    Tacho sujo, chuchu chocho.\n', '    Tem uma tatu-peba, com sete tatupebinha. Quem destatupebá ela, bom destatupebador será.\n', '    Quando toca a retreta, na praça repleta, se cala o trombone, se toca a trombeta;\n', '    O caju do Juca, e a jaca do cajá. O jacá da Juju, e o caju do Cacá.\n', '    No morro chato, tem uma moça chata, com um tacho chato, no chato da cabeça. Moça chata, esse tacho chato é seu.\n', '    Em rápido rapto, um rápido rato raptou três ratos sem deixar rastros;\n', '    Se o Pedro é preto, o peito do Pedro é preto e o peito do pé do Pedro também é preto\n', '    Um ninho de carrapatos, cheio de carrapatinhos, qual o bom carrapateador, que o descarrapateará?\n', '    O bispo de Constantinopla, é um bom desconstantinopolitanizador. Quem o desconstantinopolitanizar, um bom desconstantinopolitanizador será.\n', '    Há quatro quadros três e três quadros quatro. Sendo que quatro destes quadros são quadrados, um dos quadros quatro e três dos quadros três. Os três quadros que não são quadrados, são dois dos quadros quatro e um dos quadros três.\n', '    O princípio principal do príncipe principiava principalmente no princípio principesco da princesa.\n', '    Se vaivém fosse e viesse, vaivém ia, mas como vaivém vai e não vem, vaivém não vai.\n', '    Tecelão tece o tecido em sete sedas de Sião. Tem sido a seda tecida na sorte do tecelão.\n', '    Para ouvir o tique-taque, tique-taque, tique-taque. Depois que um tique toca é que se toca um taque.\n', '    Em rápido rapto, um rápido rato raptou três ratos sem deixar rastros\n', '    Num ninho de mafagafos, cinco mafagafinhos há! Quem os desmafagafizá-los, um bom desmafagafizador será.\n']

        print(frases[randint(0, len(frases) - 1)])


    @staticmethod
    def print_BRANCO(cor: str = "BRANCO"):
        print(cor.rjust(20, ' ') + '\x1b[6;37;47m'+ "         " + '\x1b[0m'.rjust(20, " "))
    
    @staticmethod
    def print_PRETO(cor: str = "PRETO"):
        print(cor.rjust(20, ' ') + '\x1b[7;30;41m'+ "         " + '\x1b[0m'.rjust(20, " "))
    
    @staticmethod
    def print_ROXO(cor: str = "ROXO"):
        print(cor.rjust(20, ' ') + '\x1b[7;35;45m'+ "         " + '\x1b[0m'.rjust(20, " "))
    
    @staticmethod
    def print_AMARELO(cor: str = "AMARELO"):
        print(cor.rjust(20, ' ') + '\x1b[6;33;43m'+ "         " + '\x1b[0m'.rjust(20, " "))

    @staticmethod
    def print_formatado(texto: str):
        print(texto.center(150, "-"))
    


#   GERADORES ALEATÓRIOS PARA VEICULOS
#   MODELO, VALOR, COMBUSTIVEL, POTENCIA, COR

    
    @staticmethod
    def gerador_de_modelo():
        return fake.vehicle_make_model()
    
    @staticmethod
    def gerador_de_valor_CARRO(potencia: str):
        power = ["1.0 65CV", "1.6 100CV", "2.0 150CV", "3.0 240CV", "4.1 330CV"]
        if power[0] == potencia:
            return randint(29000, 89000)
        elif power[1] == potencia:
            return randint(89100, 129000)
        elif power[2] == potencia:
            return randint(129100, 179000)
        elif power[3] == potencia:
            return randint(179100, 399000)
        else:
            return randint(399100, 1099000)
        
    
    @staticmethod
    def gerador_de_valor_MOTO(potencia: str):
        power = ["150cc 14,2CV", "250cc 22,4CV", "650cc 88,4CV", "1000cc 141CV"]
        if power[0] == potencia:
            return randint(3000, 9999)
        elif power[1] == potencia:
            return randint(10000, 19999)
        elif power[2] == potencia:
            return randint(20000, 39000)
        else:
            return randint(40000, 79999)
        
    
    @staticmethod
    def gerador_de_valor_CAMIONETE(potencia: str):
        power = ["2.0 150CV", "2.5 130CV", "3.0 190CV"]
        if power[0] == potencia:
            return randint(39000, 109999)
        elif power[1] == potencia:
            return randint(110000, 219999)
        else:
            return randint(220000, 999000)

    @staticmethod
    def setCombustivel_CARRO():
        combustivel = ["Gasolina", "Flex"]

        return combustivel[randint(0, 1)] 

    @staticmethod
    def setCombustivel_MOTO():
        combustivel = "Gasolina"
        return combustivel

    @staticmethod
    def setCombustivel_CAMIONETE():
        combustivel = ["Gasolina", "Diesel"]

        return combustivel[randint(0, 1)]
    
    @staticmethod
    def setPotencia_CARRO():
        potencia = ["1.0 65CV", "1.6 100CV", "2.0 150CV", "3.0 240CV", "4.1 330CV"]

        return potencia[randint(0, 4)]
    
    @staticmethod
    def setPotencia_MOTO():
        potencia = ["150cc 14,2CV", "250cc 22,4CV", "650cc 88,4CV", "1000cc 141CV"]

        return potencia[randint(0, 3)]
    
    @staticmethod
    def setPotencia_CAMIONETE():
        potencia = ["2.5 130CV", "3.0 190CV", "2.0 150CV"]

        return potencia[randint(0, 2)]
    
    @staticmethod
    def setCamionete_CACAMBA_LITROS():
        litros = ["500 Litros", "750 Litros", "1000 Litros", "1500 Litros"]

        return litros[randint(0, 3)]
    
    
    @staticmethod
    def setNum_RODAS_MOTO_TRICICLO():
        return randint(2, 3)

    @staticmethod
    def gera_COR():
        return fake.safe_color_name()
    
    @staticmethod
    def clear_tela():
        return system("cls") if name == "nt" else system("clear")
    

    @staticmethod
    def valor_por_extenso(number_p: str):
        # sOLUÇÃO DO STACK OVERFLOW PARA ESCREVER VALORES POR EXTENSO
        
        number_p = number_p.replace(".", ",")

        if number_p.find(',')!=-1:
            number_p = number_p.split(',')
            number_p1 = int(number_p[0].replace('.',''))
            number_p2 = int(number_p[1])
        else:
            number_p1 = int(number_p.replace('.',''))
            number_p2 = 0    

        if number_p1 == 1:
            aux1 = ' real'
        else:
            aux1 = ' reais'

        if number_p2 == 1:
            aux2 = ' centavo'
        else:
            aux2 = ' centavos'

        text1 = ''
        if number_p1 > 0:
            text1 = num2words(number_p1,lang='pt_BR') + str(aux1)
        else:
            text1 = ''

        if number_p2 > 0:
            text2 = num2words(number_p2,lang='pt_BR') + str(aux2) 
        else: 
            text2 = ''

        if (number_p1 > 0 and number_p2 > 0):
            result = text1 + ' e ' + text2
        else:
            result = text1 + text2

        print(result)
