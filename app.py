#!/usr/bin/python3
# |Contribuidores              | No. USP |
# |----------------------------|---------|
# |Christian M. T. Takagi      | 7136971 |
# |Cinthia M Tanaka            | 5649479 |
# |Daniel A. Nagata            | 7278048 |
# |Fernando T. Tanaka          | 6920230 |
# ------------------------------------------------------------------------------
# Disciplina: Laboratório de Programação II       
# Prof. Alfredo Goldman
# Exercicio Programa - Etapa 2
# Arquivo: app.py
# ------------------------------------------------------------------------------
from flask import Flask, Response, request
from flask.ext.restful import reqparse, abort, Api, Resource
from bibxml import xml_class
from arena import Arena
from pokemon import Pokemon
import sys, os

# Usamos uma divertida convencao de nomes aqui: RED = servidor, BLUE = cliente

app = Flask(__name__)
api = Api(app)
parser = xml_class()
are = Arena()
ERROR_400 = "ERROR 400 - BAD REQUEST\nCliente, seu XML nao passou a validacao\n"
ERROR_404 = ("ERROR 404 - NOT FOUND\nNao foi possivel encontrar o endereco" +
             "especificado\n")

RED = BLUE = None
pkmn = [None, None, None]
battle_state = ""
PRIMEIRO = True

# Recebe a string de um xml contendo o pokemon do cliente e devolve
# uma string xml contendo dois pokemons, do cliente e do servidor.
@app.route('/battle', methods = ['POST'])
def inicia_batalha():
    global RED, BLUE, battle_state
    # Converte em str o arquivo em bytes recebido pelo postador.
    xml_BLUE = str(request.data)[2:-1]
    # Verifica se o arquivo e valido
    if parser.valida( xml_BLUE):
        BLUE = parser.cria_pokemon( request.data )
        # Verifica o modo de entrada, se manual ou por arquivo.
        if sys.argv[2] == '--auto':
            if pokemon_por_arquivo(sys.argv[3]):
                pass
        else:
            RED = Pokemon()    
        xml_RED = parser.cliente_gera_xml( RED )
        battle_state = parser.servidor_gera_xml(RED, BLUE)

        define_ordem(RED, BLUE)
        return Response( battle_state, mimetype="text/xml" )

    else:
        abort( 400, message=ERROR_400  )



# Trata erro se o parametro id nao corresponder.
def aborta_ataque_nao_existente( id, moveset ):
    if id < 0 or id > len(moveset):
        abort( 404, message="Ataque {} nao existe".format(id) )


# Recebe id como indice do ataque a ser usado pelo cliente e devolve
# uma string xml atualizada com o resultado do confronto deste turno.
@app.route('/battle/attack/<int:id>', methods = ['POST'])
def recebe_ataque( id ):
    global RED, BLUE, battle_state, PRIMEIRO
    tree = parser.cria_arvore(battle_state)
    aborta_ataque_nao_existente( id, tree.pokemon[1].attacks )

    # Define a ordem do acao no turno
    RED_mov = escolhe_ataque(RED)
    if PRIMEIRO:
        pkmn[1] = RED
        pkmn1_mov = RED_mov
        pkmn[2] = BLUE
        pkmn2_mov = id
    else:
        pkmn[1] = BLUE
        pkmn1_mov = id
        pkmn[2] = RED
        pkmn2_mov = RED_mov

    # Primeiro ataque
    are.realiza_ataque(pkmn[1], pkmn1_mov, pkmn[2])
    quem_ganhou = ganhador(pkmn)
    if ( quem_ganhou < 3):
        print("Primeiro ganhou")
        return Response( 
                '{} foi o vencedor'.format(pkmn[quem_ganhou].get_name()),
                mimetype='text/xml' ), 205
    else:
        # Segundo ataque
        are.realiza_ataque(pkmn[2], pkmn2_mov, pkmn[1])
        quem_ganhou = ganhador(pkmn)
        if ( quem_ganhou < 3):
            print("Segundo ganhou")
            return Response( 
                '{} foi o vencedor'.format(pkmn[quem_ganhou].get_name()),
                mimetype='text' ), 205
    
    battle_state = parser.servidor_gera_xml(pkmn[1], pkmn[2])
    return Response( battle_state, mimetype='text/xml' )


# Devolve 0 se os dois pokemons foram derrotados.
# Devolve 1 se o primeiro pokemon a agir no turno foi derrotado.
# Devolve 2 se o segundo pokemon a agir no turno foi derrotado.
# Devolve 3 se os dois pokemons estao podem continuar a batalha.
def ganhador(pkmn):
    are.mostra_info_turno(pkmn[1], pkmn[2])
    if (not pkmn[1].esta_vivo() and not pkmn[2].esta_vivo()):
        print("Os dois pokemons foram derrotados. Nao ha vencedor.")
        return 0
    elif (pkmn[1].esta_vivo() and not pkmn[2].esta_vivo()):
        print("Servidor venceu")
        return 1
    elif (not pkmn[1].esta_vivo() and pkmn[2].esta_vivo()):
        print("Cliente venceu")
        return 2
    else:
        return 3

# Define qual pokemon ira atacar primeiro. Por padrao ou se suas velicidades
# forem iguais, o pokemon do servidor agira primeiro.
def define_ordem(pkmnS, pkmnC):
    global PRIMEIRO
    if pkmnS.get_spd() < pkmnC.get_spd():
        PRIMEIRO = False

# Escolhe qual ataque o servidor ira usar
def escolhe_ataque(pkmnS):
    return are.escolhe_ataques(pkmnS)

# Cria o pokemon do servidor usando entradas de um arquivo.
def pokemon_por_arquivo(input_file):
    global RED
    try:
        # Redireciona sys.stdin
        with open(input_file, 'r') as sys.stdin:
            RED = Pokemon()
        # Restaura sys.stdin
        sys.stdin = sys.__stdin__
        return True
    except: 
        print("Arquivo nao existente. Iniciando em modo de entrada manual.")
        return False

def main():
    app.run( debug=True )


if __name__ == '__main__':
    app.run( debug=True )
