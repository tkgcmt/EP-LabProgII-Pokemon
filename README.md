|Contribuidores              | No. USP |
|----------------------------|---------|
|Christian M. T. Takagi      | 7136971 |
|Cinthia M Tanaka            | 5649479 |
|Daniel A. Nagata            | 7278048 |
|Fernando T. Tanaka          | 6920230 |

Disciplina: Laboratório de Programação II       
Prof. Alfredo Goldman
Exercicio Programa - Etapa 2
Arquivo: README.md


1. Introdução
================================================================================

Esse exercício programa tem como objetivo final criar um simulador de batalhas
Pokémon e realizar um torneio entre os alunos no final do curso.

Todas as fórmulas e informações adicionais foram extraídas da 
wiki bulbapedia.bulbagarden.net

Para mais informações sobre o funcionamento, leia o enunciado em pdf.

2. Estrutura de Dados
================================================================================

A classe Movimento representa uma ação (ataque ou outro movimento) que um 
Pokémon pode realizar. É responsável por verificar se é possível realizar a ação
e por deduzir o contador de uso pp.

A classe Pokemon representa um Pokémon com os atributos necessários. É também
responsável por mostrar a lista de ataques que possui e de verificar se foi
derrotado. Importa Movimento.

A classe Arena representa uma batalha entre dois Pokémons. É responsável pelo
controle do combate, cálculos e por informar o vencedor. Importa Pokemon.

A classe xml_class (do arquivo bibxml) contém funções que geram arquivos xml
e é responsável por extrair as informações do arquivo em xml.

A classe Cliente possui funções que fazem postagens em um Servidor

O arquivo app.py possui o loop do servidor, e é responsável por analisar os
métodos de POSTs e realizar as tarefas associadas aos mesmos.

As relações entra as classes são facilmente visualizadas no arquivo pokemon.dia

3. Execução
================================================================================

Para executar o programa, utilize a versao 3 do python.
Para iniciar o programa em modo servidor:
    $ python3 EP_Etapa2.py --server

Para executar o programa em modo cliente:
    $ python3 EP_Etapa2.py --client


Para usar um arquivo para inicializar o Pokemon do servidor:
    $ python3 EP_Etapa2.py --server --auto [input_file]

Para usar um arquivo para inicializar o Pokemon do servidor:
    $ python3 EP_Etapa2.py --server --auto [input_file]

Onde input_file é o nome do arquio a ser usado.


4. Testes
================================================================================

Utilizamos o pacote unittest, para os testes de unidade. Como já foi cobrado
seu uso durante o curso, não iremos aprofundar em questões de seu funcionamento.

Os teste são realizados através da criação de arquivos de entrada, substituindo
a entrada padrão. O próprio teste se encarrega de criar os arquivos necessários.

As entradas criadas possuem valores acima dos limites superiores e inferiores.

Os testes das classes pokemon e movimento são bastante objetivas, sendo simples
comparações de valores, em suma.

Os testes de arena.py não realiza testes para algumas funções, pois essas
são apenas interfaces que invocam a chamada outras funcões núcleo. Testamos 
essas funções núcleo, apenas.

Não fizemos testes de unidade para a Etapa2


5. Dificuldades
================================================================================

Três dos nossos integrantes tiveram problemas ao instalar o Flask, devido à incom-
patibilidade com a versão do Ubuntu.
Usando o virtualenv, não foi possível instalar o lxml.



6. A fazer
================================================================================

   * Refatorar o código e deixar o código com um única linguagem (nomes de
        métodos e atributos somente em en-us ou pt-br)
   
   * Etapa 3.

