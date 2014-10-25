import movimento
import pokemon
import random
import os

class Arena:

   tabela = [               #Bird
   #  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15
   [ 1.0,1.0,1.0,1.0,1.0,0.5,1.0,1.0,0.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0 ], # 0 - Normal
   [ 2.0,1.0,0.5,0.5,1.0,2.0,1.0,0.5,0.0,1.0,1.0,1.0,1.0,0.5,2.0,1.0 ], # 1 - Fight
   [ 1.0,2.0,1.0,1.0,1.0,0.5,1.0,2.0,1.0,1.0,1.0,2.0,0.5,1.0,1.0,1.0 ], # 2 - Fly
   [ 1.0,1.0,1.0,0.5,0.5,0.5,1.0,2.0,0.5,1.0,1.0,2.0,1.0,1.0,1.0,1.0 ], # 3 - Poison
   [ 1.0,1.0,0.0,2.0,1.0,2.0,1.0,0.5,1.0,2.0,1.0,0.5,2.0,1.0,1.0,1.0 ], # 4 - Ground
   [ 1.0,0.5,2.0,1.0,0.5,1.0,1.0,2.0,1.0,2.0,1.0,1.0,1.0,1.0,2.0,1.0 ], # 5 - Rock
   [ 1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0 ], # 6 - Bird
   [ 1.0,0.5,0.5,2.0,1.0,1.0,1.0,1.0,0.5,0.5,1.0,2.0,1.0,2.0,1.0,1.0 ], # 7 - Bug
   [ 0.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,2.0,1.0,1.0,1.0,1.0,0.0,1.0,1.0 ], # 8 - Ghost
   [ 1.0,1.0,1.0,1.0,1.0,0.5,1.0,2.0,1.0,0.5,0.5,2.0,1.0,1.0,2.0,0.5 ], # 9 - Fire
   [ 1.0,1.0,1.0,1.0,2.0,2.0,1.0,1.0,1.0,2.0,0.5,0.5,1.0,1.0,1.0,0.5 ], # 10 - Water
   [ 1.0,1.0,0.5,0.5,2.0,2.0,1.0,0.5,1.0,0.5,2.0,0.5,1.0,1.0,1.0,0.5 ], # 11- Grass
   [ 1.0,1.0,2.0,1.0,0.0,1.0,1.0,1.0,1.0,1.0,2.0,0.5,0.5,1.0,1.0,0.5 ], # 12- Eletr
   [ 1.0,2.0,1.0,2.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.5,1.0,1.0 ], # 13- Psychc
   [ 1.0,1.0,2.0,1.0,2.0,1.0,1.0,1.0,1.0,1.0,0.5,2.0,1.0,1.0,0.5,2.0 ], # 14- Ice
   [ 1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,2.0 ]  # 15- Dragon
             ]

   def base_damage ( self, pokeA, atk, pokeB ):
      termo1 = ( 2 * pokeA.get_level () + 10 ) / 250
      termo2 = pokeA.get_atk () / pokeB.get_def () * atk.get_power ()
      return ( termo1 * termo2 + 2 )

   def stab ( self, pokemon, movimento ):
      if pokemon.get_type1 () == movimento.get_type ():
         return 1.5
      elif pokemon.get_type2 () == movimento.get_type ():
         return 1.5
      else:
         return 1

   def type_effect ( self, atk, pokemon ):
      effect = self.tabela [atk.get_type ()][pokemon.get_type1 ()]
      if pokemon.get_type2 () != 16:
         effect = effect * self.tabela [atk.get_type ()][pokemon.get_type2 ()]
      if effect > 1:
         print ( 'Ataque super efetivo' )
      elif effect < 1:
         print ( 'Ataque nao muito efetivo' )
      return effect

   def critical ( self, pokemon ):
      chance = pokemon.get_spd () / 512
      rand   = random.random ()
      if rand <= chance:
         lvl = pokemon.get_level ()
         print ( 'Ataque critico' )
         return ( ( 2 * lvl ) / ( lvl + 5 ) )
      else:
         return 1

   def rand ( self ):
      return random.uniform ( 0.85, 1 )

   def modifier_damage ( self, pokeA, atk, pokeB ):
      termo1 = self.stab ( pokeA, atk ) * self.type_effect ( atk, pokeB )
      termo2 = self.critical ( pokeA ) * self.rand ()
      return ( termo1 * termo2 )

   def damage ( self, pokeA, atk, pokeB ):
      dano = self.base_damage ( pokeA, atk, pokeB )
      dano = dano * self.modifier_damage ( pokeA, atk, pokeB )
      return int ( dano )

   def accuracy ( self, mov ):
      accu = mov.get_accu ()
      if accu > 1:
         accu = accu * 0.01
      rand = random.random ()
      if rand <= accu:
         return True
      else:
         return False

   def mostra_info_turno ( self, poke1, poke2 ):
      print ()
      print ( ' Turno #', self.contador )
      print ( )
      print ( '                              +---' )
      print ( '                              | Nome:', poke2.get_name () )
      print ( '                              | HP:', ( poke2.get_hp () /
                                             poke2.get_hpmax () ) * 100, '%' )
      print ( '                              +---' )
      print ()
      print ( ' +---' )
      print ( ' | Nome:', poke1.get_name () )
      print ( ' | HP:', ( poke1.get_hp () / poke1.get_hpmax () ) * 100, '%' )
      print ( ' +---' )
      print ( )

   def mostra_info_pokemon ( self, poke ):
      print ( )
      print ( ' +---' )
      print ( ' | Nome:', poke.get_name () )
      print ( ' | HP:', poke.get_hp (), '/', poke.get_hpmax () )
      print ( ' +---' )
      print ( )


   def escolhe_ataques ( self, poke ):
      self.mostra_info_pokemon ( poke )
      poke.mostra_ataques ()

      if poke.possui_ataques ():
         while ( True ):
            opt = int ( input ( 'Qual ataque deseja executar?' ) )
            if opt >= 0 and opt < poke.get_numAtk ():
               atk = poke.moveset[opt]
               if atk.get_pp () < 1:
                  print ( 'Sem movimentos restantes' )
               else:
                  break
            else:
               print ( 'ERRO: Ataque invalido' )
      else:
         print ( poke.get_name (), 'nao possui mais ataques.' )
         opt = poke.get_numAtk ()

      return opt

   def realiza_ataque ( self, ataque, numero, defesa ):
      movimento = ataque.moveset[ numero ]

      print ( ataque.get_name (), 'usou', movimento.get_name () )

      if self.accuracy ( movimento ):
         dano = self.damage ( ataque, movimento, defesa )
         porcentagem = dano / defesa.get_hp () * 100
         print ( defesa.get_name (), 'perdeu', porcentagem, '% da sua vida' )
         defesa.set_hp ( defesa.get_hp () - dano )

         if numero == ataque.get_numAtk (): # Struggle
            print ( ataque.get_name (), 'sofre com o recoil' )
            dano = int ( dano / 2 )
            porcentagem = dano / ataque.get_hp () * 100
            print ( ataque.get_name (), 'perdeu', porcentagem, '% da sua vida' )
            ataque.set_hp ( ataque.get_hp () - dano )
      else:
         print ( ataque.get_name (), 'errou o ataque' )

      movimento.reduz_pp ()

   def turno ( self, poke1, poke2 ):
      self.contador = self.contador + 1
      print ( '# Player 1' )
      self.mostra_info_turno ( poke1, poke2 )
      ataque1 = self.escolhe_ataques ( poke1 )

      os.system ( 'clear' )

      print ( '# Player 2' )
      self.mostra_info_turno ( poke1, poke2 )
      ataque2 = self.escolhe_ataques ( poke2 )

      os.system ( 'clear' )
      self.mostra_info_turno ( poke1, poke2 )
      if poke1.get_spd () > poke2.get_spd ():
         primeiro = poke1
         first    = ataque1
         segundo  = poke2
         second   = ataque2
      else:
         primeiro = poke2
         first    = ataque2
         segundo  = poke1
         second   = ataque1

      if primeiro.esta_vivo () and segundo.esta_vivo ():
         self.realiza_ataque ( primeiro, first, segundo )
      else:
         return False

      if primeiro.esta_vivo () and segundo.esta_vivo ():
         self.realiza_ataque ( segundo, second, primeiro )
      else:
         return False

      if primeiro.esta_vivo () and segundo.esta_vivo ():
         return True
      else:
         return False

   def __init__ ( self ):
      print ( ' Player 1 ' )
      self.pkmn1 = pokemon.Pokemon ()
      os.system ( 'clear' )
      print ( ' Player 2 ' )
      self.pkmn2 = pokemon.Pokemon ()
      os.system ( 'clear' )
      self.contador = 0

      while ( self.turno ( self.pkmn1, self.pkmn2 ) ):
         input ( 'Pressione qualquer tecla para iniciar o proximo turno' )

      os.system ( 'clear' )
      print ( '   Fim da Batalha' )
      self.mostra_info_turno ( self.pkmn1, self.pkmn2 )
      if self.pkmn1.esta_vivo ()== False and self.pkmn2.esta_vivo () == False:
         print ( ' EMPATE' )
      elif self.pkmn1.esta_vivo ():
         print ( ' PLAYER 1 VENCEU' )
      else:
         print ( ' PLAYER 2 VENCEU' )
