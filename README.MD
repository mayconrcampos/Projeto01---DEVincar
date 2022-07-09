<h1>Projeto 01 - MÓDULO 02 - Senai DEVinHouse[ConectaNuvem]</h1>

<h2>Nome do Projeto: DEVinCAR Project</h2>

<p>Neste primeiro projeto do segundo módulo devemos construir um sistema que simula uma MONTADORA e REVENDA de Carros. Neste sistema deverá conter 3 tipos de carros:</p>

<ul>
    <li>Carros</li>
    <li>Moto/Triciclo</li>
    <li>Camionete</li>
</ul>

<p>Cada um deles deverá possuir características em comum, porém cada um deles vão possuir as suas características particulares.</p>

<p><strong>Professor: </strong>Yan Esteves<p>
<p><strong>Curso: </strong>Senai DEVinHouse[ConectaNuvem] - MÓDULO 02</p>

<h3>Linguagens, conceitos e tecnologias utilizadas neste projeto:</h3>

<ul>
    <li>Python 3.10</li>
    <li>Programação Orientada a Objetos</li>
    <li>
        <li>Conceitos de Classes Abstratas</li>
        <li>Herança e Polimorfismo</li>
        <li>Métodos estáticos</li>
    </li>
    <li>Persistência de Dados com JSON</li>
    <li>
        <li>Biblioteca TinyDB - Manipulação de JSON</li>
    </li>
    <li>Bibliotecas Gerais</li>
    <li>
        <li>Biblioteca Faker_vehicle - Gerando nomes de automóveis de forma aleatória</li>
        <li>Biblioteca num2words - Escrevendo valores monetários por extenso</li>
        <li>Entre outras bibliotecas bultins do Python: os, random, datetime, etc...</li>
    </li>
    <li>Versionamento com GIT</li>
</ul>

<h3>Descrição de como ficou o projeto e seu fluxo de trabalho</h3>

<li>Ele é iniciado pelo main.py que gera um menu com 8 opções:</li>
<li>
    <li>1. Fabricar Veículo</li>
    <li>
        <li>SELECIONE A QUANTIDADE</li>
        <li>1.1 10 unidades</li>
        <li>
            <li>SELECIONE A CATEGORIA</li>
            <li>1.1.1 Carro</li>
            <li>1.1.2 Moto/Triciclo</li>
            <li>1.1.3 Camionete</li>
        </li>
        <li>1.2 20 unidades</li>
        <li>
            <li>SELECIONE A CATEGORIA</li>
            <li>1.2.1 Carro</li>
            <li>1.2.2 Moto/Triciclo</li>
            <li>1.2.3 Camionete</li>
        </li>
        <li>1.3 50 unidades</li>
        <li>
            <li>SELECIONE A CATEGORIA</li>
            <li>1.3.1 Carro</li>
            <li>1.3.2 Moto/Triciclo</li>
            <li>1.3.3 Camionete</li>
        </li>
        <li>1.4 Retornar ao menu principal</li>
    </li>
    <li>2. Listar Veículos em estoque</li>
    <li>
        <li>ESCOLHA A CATEGORIA PARA LISTAR O ESTOQUE</li>
        <li>2.1 Carro</li>
        <li>2.2 Moto/Triciclo</li>
        <li>2.3 Camionete</li>
        <li>2.4 Retornar ao menu principal</li>
    </li>
    <li>3. Vender veículo</li>
    <li>
        <li>ESCOLHA A CATEGORIA</li>
        <li>3.1 Carro</li>
        <li>3.2 Moto/Triciclo</li>
        <li>3.3 Camionete</li>
        <li>3.4 Retornar ao menu principal</li>
    </li>
    <li>4. Listar Veículos vendidos</li>
    <li>
        <li>ESCOLHA A CATEGORIA PARA LISTAR VEÍCULOS VENDIDOS</li>
        <li>4.1 Carro</li>
        <li>4.2 Moto/Triciclo</li>
        <li>4.3 Camionete</li>
        <li>4.4 Retornar ao menu principal</li>
    </li>
    <li>5. Visualizar veículo mais caro</li>
    <li>
        <li>5.1 Em Estoque</li>
        <li>5.2 Vendidos</li>
    </li>
    <li>6. Visualizar veículo mais barato</li>
    <li>
        <li>6.1 Em Estoque</li>
        <li>6.2 Vendidos</li>
    </li>
    <li>7. Alterar Veículo Comprado</li>
    <li>
        <li>SELECIONE A CATEGORIA</li>
        <li>7.1 Carro</li>
        <li>7.2 Moto/Triciclo</li>
        <li>7.3 Camionete</li>
        <li>7.4 Retornar ao menu principal</li>
    </li>
    <li>8. Sair do Sistema</li>
</li>

<h3>FLUXO DO PROGRAMA</h3>

<p>Para este programa, imaginei o seguinte: </p>

<p>Ao executar o programa, se o usuário selecionar as opções de listar veículos em estoque ou vendidos, ou visualizar veiculo mais caro ou mais barato, ou mesmo alterar veículo comprado, ele não irá conseguir, pois não existem veículos cadastrados.</p>
<p>Logo, ao iniciar, a primeira coisa a se fazer será ir na opção 1 e fabricar os veículos desejados na quantidade desejada.</p>
<p>Ao iniciar a aplicação, haverá a instanciação de 3 objetos das 3 classes: Carro, MotoTriciclo e Camionete. Estarão na memória aguardando o acionamento de seus métodos.</p>
<p>Ao fabricar veículos, o método fabricar_veículo da instância escolhida será chamado para povoar o arquivo JSON com veículos cujos dados serão gerados de forma aleatória. chassi, cor, valor, etc .... Serão gerados, 10, 20 ou 50 de uma vez e inseridos no array... Todos com a data de sua fabricação e 0km, sem dono. Agora estão em estoque.</p>
<p>Para listar estes itens, basta ir na opção 2 e listá-los para saber quantos itens possuimos em estoque, bem como todos seus dados e valor total que é a soma de todos os itens do estoque.</p>
<p>Para Vender um veículo, é necessário que ele esteja no estoque, e basta copiar o chassi do item desejado, colar no input e teclar enter. Se o usuário tiver digitado o chassi corretamente ele prosseguirá pedindo outros dados para concretização da venda.</p>
<p>Ao vender um veículo, todos os dados inseridos possuem validação, sendo necessário inserir CPF válido e placa que esteja no formato antigo (sem o traço MMM0000) ou mercosul (XXX0X00).</p>
<p>Após a venda, o veículo sairá da lista de estoque e passará a ser visível somente na lista de veiculos vendidos, que podem ser acessados na opção 4 do menu principal.</p>
<p>Podemos visualizar veículos mais caros do estoque e dos que foram vendidos.</p>
<p>Podemos visualizar veículos mais baratos do estoque e dos que foram vendidos.</p>
<p>A alteração de veículos só é possível para aqueles que já foram vendidos, sendo que em uma das opções (Camionete), inseri uma brincadeira com relação à cor ROXA referida nos requisitos do sistema, onde apesar de não termos escolha, decidi fazer o usuário de bobo e tentar escolher uma nova cor, mas ele terá uma surpresa ao tentar fazer isso.</p>


<hr>

<h1>Telas do Sistema</h1>


<h2>MENU PRINCIPAL</h2>

<img src="./prints/01.png" alt="MENU PRINCIPAL">

<h2>SELECIONANDO QUANTIDADE DE ITENS A SEREM FABRICADOS</h2>

<img src="./prints/02.png" alt="QTDE">

<h3>SELEÇÃO DE CATEGORIA</h3>

<img src="./prints/03.png" alt="esqueceuasenha">

<h3>LISTAGEM DE ITENS VENDIDOS</h3>

<img src="./prints/04.png" alt="entrarcomgoogle">



