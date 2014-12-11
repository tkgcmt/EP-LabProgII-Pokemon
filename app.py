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
import arena as are
from pokemon import Pokemon
import sys, os

# Usamos uma divertida convencao de nomes aqui: RED = servidor, BLUE = cliente

app = Flask(__name__)
api = Api(app)
parser = xml_class()
ERROR_400 = "ERROR 400 - BAD REQUEST\nCliente, seu XML nao passou a validacao\n"
ERROR_404 = ("ERROR 404 - NOT FOUND\nNao foi possivel encontrar o endereco" +
             "especificado\n")

#class Battle(Resource):
BLUE = RED = None
xml_BLUE = xml_RED = battle_state = ""

# Recebe a string de um xml contendo o pokemon do cliente e devolve
# uma string xml contendo dois pokemons, do cliente e do servidor.
@app.route('/battle', methods = ['POST'])
def inicia_batalha():
    global RED, BLUE, xml_RED, xml_BLUE, battle_state
    # Criar os pokemons para usar na simulacao
    xml_BLUE = str(request.data)[2:-1]
    print("&&&&&&&&&&&&&&&&&&&&&\n", xml_BLUE)
    # Trata do erro se a validacao nao foi bem sucedida.
    if parser.valida( xml_BLUE):
        BLUE = parser.cria_pokemon( request.data )
        if os.path.isfile('in_MEW') == False:
            with open('in_MEW', 'w+') as arq:
                 arq.write('Mew\n50\n100\n100\n100\n100\n100\n13\n\n4\n'
                         'Thunderbolt\n12\n100\n95\n15\n'
                         'Rock_Slide\n5\n90\n75\n10\n'
                         'Earthquake\n4\n100\n100\n10\n'
                         'Bubblebeam\n10\n100\n65\n20\n')
        with open('in_MEW', 'r') as sys.stdin:
            RED = Pokemon()

        xml_RED = parser.cliente_gera_xml( RED )
        battle_state = parser.servidor_gera_xml(RED, BLUE) 
        return Response( battle_state, mimetype="text/xml" )
    else:
        abort( 400, message=ERROR_400  )

# Trata erro se o parametro id nao corresponder.
def aborta_ataque_nao_existente( id, moveset ):
    if id < 0 or id > len(moveset):
        abort( 404, message="Ataque {} nao existe".format(id) )

# Recebe id como indice do ataque a ser usado pelo cliente e devolve
# uma string xml atualizada com o resultado do confronto deste turno.
# Ainda em teste
@app.route('/battle/attack/<int:id>', methods = ['POST'])
def recebe_ataque( id ):
    global RED, BLUE, xml_RED, xml_BLUE, battle_state
    tree = parser.cria_arvore(battle_state)
    print("\nCliente\n", tree.pokemon[1].attacks[id]['name'])
    aborta_ataque_nao_existente( id, tree.pokemon[1].attacks )
    # Testa atualização do ataque
    print( 'PP do ataque antes: ', tree.pokemon[0].attacks[id]["power_points"] )
    tree.pokemon[0].attacks[id]["power_points"] -= 1
    print( 'PP do ataque depois: ', tree.pokemon[0].attacks[id]["power_points"] )
    return Response( '<xml></xml>', mimetype='text/xml' )


if __name__ == '__main__':
    app.run( debug=True )
