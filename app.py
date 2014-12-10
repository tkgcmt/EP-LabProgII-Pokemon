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
import sys

app = Flask(__name__)
api = Api(app)
parser = xml_class()

# Contem os metodos da batalha
class StartBattle( Resource ):
    def not_found( error=None ):
        message = {
                'status': 404,
                'message': 'Not Found: ' + request.url, }
        resp = jsonify(message)
        resp.status_code = 404
        return resp

    def post( self ):
        # Criar os pokemons para usar na simulacao
        self.xml_pkmn_cli = str( request.data )[2:-1]
        print( self.xml_pkmn_cli )
        if parser.valida( self.xml_pkmn_cli ):
            self.pkmn_cli = parser.cria_pokemon( request.data )
            self.pkmn_svr = Pokemon()
            self.xml_pkmn_svr = parser.cliente_gera_xml( self.pkmn_svr )
            battle_state = self.xml_pkmn_svr + self.xml_pkmn_cli
            return Response( battle_state, mimetype="text/xml" )
        else:
            return not_found()
            
class Move( Resource ):

    def aborta_ataque_nao_existente( self, id, moveset ):
        if id not in moveset:
            abort( 404, message="Ataque {} nao existe".format(id) )

    def post( self, id ):
        with open( 'entrada1.xml', 'r' ) as temp_xml:
            tree = bibxml.cria_arvore( temp_xml )
            self.aborta_ataque_nao_existente( id, tree.pokemon[0].attacks )
            print( 'PP do ataque antes: ', tree.pokemon[0].attacks[id]["power_points"] )
            tree.pokemon[0].attacks[id]["power_points"] -= 1
            print( 'PP do ataque depois: ', tree.pokemon[0].attacks[id]["power_points"] )
            body = temp_xml.read()
        # battle_state = open( 'battle_state.xml', 'w+' )
        # battle_state.write( body )
        return Response( battle_state, mimetype='text/xml' )

# Define as rotas do API
api.add_resource( StartBattle, '/battle' )
api.add_resource( Move, '/battle/attack/<int:id>' )


if __name__ == '__main__':
    app.run( debug=True )
