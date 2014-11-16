|Contribuidores              | No. USP |
|----------------------------|---------|
|Christian M. T. Takagi      | 7136971 |
|Cinthia M Tanaka            | 5649479 |
|Daniel A. Nagata            | 7278048 |
|Fernando T. Tanaka          | 6920230 |

Disciplina: Laboratório de Programação II       
Prof. Alfredo Goldman
Exercicio Programa - Etapa 1                    
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

As relações entra as classes são facilmente visualizadas no arquivo pokemon.dia

3. Execução
================================================================================

Para executar o programa, utilize a versao 3 do python, chamando o arquivo arena.py, como a seguir
    $ python3 arena.py

Se preferir, temos um arquivo para servir de entrada, chamado 'simulacao':
    $ python3 arena.py < simulacao

6. Testes
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

5. Dificuldades
================================================================================

Tivemos dificuldades em testar as impressões do programa. Como sugerido, 
separamos a geração do texto da impressão e testamos apenas a geração do texto,
confiando nas rotinas de impressão.

6. A fazer
================================================================================

   * Adicionar argumento na chamada do programa, para criação de 
   Pokémons via arquivo (apenas a criação).

   * Etapa 2.
