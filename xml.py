from lxml import etree

import pokemon

class xml:

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

   def cliente_gera_xml ( self, poke ):
      xml = etree.Element ( 'battle_state' )
      doc = etree.ElementTree ( xml )
      self.pokemon_gera_xml ( xml, poke )
      return etree.tostring ( xml, encoding = 'unicode', pretty_print = True )

   def servidor_gera_xml ( self, pokeS, pokeC ):
      xml = etree.Element ( 'battle_state' )
      doc = etree.ElementTree ( xml )
      self.pokemon_gera_xml ( xml, pokeS )
      self.pokemon_gera_xml ( xml, pokeC )
      return etree.tostring ( xml, encoding = 'unicode', pretty_print = True )

   def validacao ( self, schema_file, xml_string ):
      schema = etree.XMLSchema ( etree.parse ( schema_file ) )
      xmlparser = etree.XMLParser ( schema = schema )
      try:
         etree.fromstring ( xml_string, xmlparser )
         return True
      except:
         return False
