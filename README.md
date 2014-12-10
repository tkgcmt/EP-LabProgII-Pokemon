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

Para executar o programa, utilize a versao 3 do python, chamando o arquivo app.py,
para iniciar o programa em modo servidor:
    $ python3 app.py

Para executar o programa em modo cliente, execute-o atráves do arquivo cliente.py:
    $ python3 cliente.py

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

Para testar a parte funcional do programa, inicialize o app.py e em seguida
rode o cliente.py, como mencionado no item anterior.

Deve ser possível postar um arquivo xml, a partir do cliente e recebê-lo no
servidor.

O arquivo teste.py testa algumas funcionalidades da interação cliente x servidor.
Rode-o, com 
    $ python3 teste.py < MUK

5. Dificuldades
================================================================================

Não conseguimos entregar um código funcional para a Etapa2 devido a extrema 
dificuldade de compreensão funcionamento do FLASK e como fazer as postagens 
corretamente. As instalações dos pacotes por si só já foram complicadas.

Três dos nossos integrantes tiveram problemas ao instalar o Flask, devido à incom-
patibilidade com a versão do Ubuntu.
Usando o virtualenv, não foi possível instalar o lxml.



6. A fazer
================================================================================

   * Completar a execução da web API (modo servidor)
   * Cuidar dos erros, quando valida() falha. i.e. error 404, etc.
   * Refatorar o código e deixar o código com um única linguagem (nomes de
        métodos e atributos somente em en-us ou pt-br)
   * Adicionar a opção de se criar um obj Pokemon() através de um arquivo.
        - def __init__(self, entrada = None)
            if entrada != None: redireciona_std_in #ver teste_*.py
    
    
   * Etapa 3.

