from lxml import etree, objectify

import pokemon

class xml_class():

   def __init__ ( self ):
      self.schema_file = 'battle_state.xsd'

   def movimento_gera_xml ( self, xml, nid, mov ):
      mov_tag = etree.SubElement ( xml, 'attacks' )

      mov_id = etree.SubElement ( mov_tag, 'id' )
      mov_id.text = str ( nid )

      mov_name = etree.SubElement ( mov_tag, 'name' )
      mov_name.text = str ( mov.get_name () )

      mov_type = etree.SubElement ( mov_tag, 'type' )
      mov_type.text = str ( mov.get_type () )

      mov_power = etree.SubElement ( mov_tag, 'power' )
      mov_power.text = str ( mov.get_power () )

      mov_accu = etree.SubElement ( mov_tag, 'accuracy' )
      mov_accu.text = str ( mov.get_accu () )

      mov_pp = etree.SubElement ( mov_tag, 'power_points' )
      mov_pp.text = str ( mov.get_pp () )

   def pokemon_gera_xml ( self, xml, poke ):
      poke_tag = etree.SubElement ( xml, 'pokemon' )

      poke_name = etree.SubElement ( poke_tag, 'name' )
      poke_name.text = str ( poke.get_name () )

      poke_level = etree.SubElement ( poke_tag, 'level' )
      poke_level.text = str ( poke.get_lvl () )

      poke_attr = etree.SubElement ( poke_tag, 'attributes' )

      poke_health = etree.SubElement ( poke_attr, 'health' )
      poke_health.text = str ( poke.get_hp () )

      poke_attack = etree.SubElement ( poke_attr, 'attack' )
      poke_attack.text = str ( poke.get_atk () )

      poke_defense = etree.SubElement ( poke_attr, 'defense' )
      poke_defense.text = str ( poke.get_defe () )

      poke_speed = etree.SubElement ( poke_attr, 'speed' )
      poke_speed.text = str ( poke.get_spd () )

      poke_special = etree.SubElement ( poke_attr, 'special' )
      poke_special.text = str ( poke.get_spd () )

      poke_type1 = etree.SubElement ( poke_tag, 'type' )
      poke_type1.text = str ( poke.get_type1 () )

      if poke.get_type2 () != 16:
         poke_type2 = etree.SubElement ( poke_tag, 'type' )
         poke_type2.text = str ( poke.get_type2 () )

      for i in range ( poke.get_numAtk () ):
         atk = poke.get_movimento ( i + 1 )
         self.movimento_gera_xml ( poke_tag, i + 1, atk )

   # Gera xml para o cliente
   def cliente_gera_xml ( self, poke ):
      xml = etree.Element ( 'battle_state' )
      doc = etree.ElementTree ( xml )
      self.pokemon_gera_xml ( xml, poke )
      return etree.tostring ( xml, encoding = 'unicode', pretty_print = False )

   # Gera xml que sera enviado para o cliente, com os
   # dados do cliente e do servidor
   def servidor_gera_xml ( self, pokeS, pokeC ):
      xml = etree.Element ( 'battle_state' )
      #doc = etree.ElementTree ( xml )
      self.pokemon_gera_xml ( xml, pokeS )
      self.pokemon_gera_xml ( xml, pokeC )
      return etree.tostring ( xml, encoding = 'unicode', pretty_print = True )

   # Valida uma string xml a partir de um arquivo schema
   def valida ( self, xml_string ):
      
      # Salva a string em arquivo
      with open("output.xml",'w') as f:
         f.write(xml_string)
      
      schema = etree.XMLSchema(etree.parse(self.schema_file))
      xmlparser = etree.XMLParser(schema=schema)
      
      xml_file = "output.xml"

      try:
         with open(xml_file, 'r') as f:
            etree.fromstring(f.read(), xmlparser)
         return True

      except:
         return False

   # Cria arvore xml a partir de uma string  xml
   def cria_arvore ( self, myxml ):
      tree = objectify.fromstring(myxml)
      return tree 

   # Imprime informacoes essenciais a partir da arvore
   def imprime_basico ( self, tree ):
      for k in range(len(tree.pokemon)):
         print("\n")
         print(tree.pokemon[k]["name"].text, ": lvl ",tree.pokemon[k]["level"].text)
         print("hp: ", tree.pokemon[k].attributes["health"].text)
         for i in range(len(tree.pokemon[k].attacks)):
            print(tree.pokemon[k].attacks[i]["id"], " ",
            tree.pokemon[k].attacks[i]["name"])
            print("pp left: ", tree.pokemon[k].attacks[i]["power_points"])

   def atualiza_xml_para_pokemon ( self, elem, poke ):
      attributes = elem.find ( 'attributes' )
      hp         = int ( attributes.find ( 'health' ).text )
      poke.set_hp ( hp )

      attacks = elem.findall ( 'attacks' )
      for i in range ( len ( attacks ) ):
         atk_elem = attacks[i]
         nid = int ( atk_elem.find('id').text )
         pp  = int ( atk_elem.find('power_points').text )
         atk_mov = poke.get_movimento ( nid )
         atk_mov.set_pp ( pp )

   def atualiza_xml_para_batalha ( self, xml, pokeS, pokeC ):
      list_pokemon = xml.findall ( 'pokemon' )
      self.atualiza_pokemon ( list_pokemon[0], pokeS )
      self.atualiza_pokemon ( list_pokemon[1], pokeC )

   def cria_pokemon ( self, my_xml ):
      elem_xml = objectify.fromstring(my_xml)
      poke = pokemon.Pokemon.__new__ ( pokemon.Pokemon )
      # nome
      nome = elem_xml.pokemon['name']
      poke.set_name ( nome )
      # level
      level = elem_xml.pokemon['level']
      poke.set_lvl ( level ) 
      # atributos
      atributos = elem_xml.pokemon['attributes']
      # hp
      vida = int ( atributos[ 'health' ] )
      poke.set_hpmax ( vida )
      poke.set_hp ( vida )
      # ataque
      ataque = int ( atributos[ 'attack' ] )
      poke.set_atk ( ataque ) 
      # defesa
      defesa = int ( atributos[ 'defense' ] )
      poke.set_defe ( defesa ) 
      # velocidade
      velocidade = int ( atributos[ 'speed' ] )
      poke.set_spd ( velocidade ) 
      # especial
      especial = int ( atributos[ 'special' ] )
      poke.set_spc ( especial )

      # tipos
      lista_tipos = elem_xml.pokemon['type']
      for i in range ( len ( lista_tipos ) ):
         elem = lista_tipos[i]
         tipo = int ( elem )
         if i == 0:
            poke.set_type1 ( tipo )
            poke.set_type2 ( 16 )
         elif i == 1:
            poke.set_type2 ( tipo )
           

      # ataques
      lista_ataques = elem_xml.pokemon['attacks']
      poke.cria_moveset ()
      for i in range ( len ( lista_ataques ) + 1 ) :
         mov = pokemon.mov.Movimento.__new__ ( pokemon.mov.Movimento )
         if i == 0:
            nome = 'Struggle'
            tipo = 0
            accu = 100
            poder = 50
            ppmax = pp = 10
            nAtk = 0
         else:
            atk_elem = lista_ataques[i - 1]
            nome = atk_elem[ 'name' ]
            tipo = int ( atk_elem[ 'type' ] )
            accu = int ( atk_elem[ 'accuracy' ] )
            poder = int ( atk_elem[ 'power' ] )
            pp = ppmax = int ( atk_elem[ 'power_points' ] )
            nAtk = int ( poke.get_numAtk () + 1 )
         mov.set_name ( nome )
         mov.set_type ( tipo )
         mov.set_accu ( accu )
         mov.set_power ( poder )
         mov.set_ppmax ( ppmax )
         mov.set_pp ( pp )
         poke.set_numAtk ( nAtk )
         poke.moveset.append ( mov )
      poke.mostra_pkmn()
      poke.mostra_lista_movimentos()
      return poke
