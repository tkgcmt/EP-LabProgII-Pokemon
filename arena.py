import pokemon as pkm
import random

class Arena:

   tabela = [
   #  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14
   [ 1.0,1.0,1.0,1.0,1.0,0.5,1.0,0.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0 ],# 0 - Normal
   [ 2.0,1.0,0.5,0.5,1.0,2.0,0.5,0.0,1.0,1.0,1.0,1.0,0.5,2.0,1.0 ],# 1 - Fight
   [ 1.0,2.0,1.0,1.0,1.0,0.5,2.0,1.0,1.0,1.0,2.0,0.5,1.0,1.0,1.0 ],# 2 - Flying
   [ 1.0,1.0,1.0,0.5,0.5,0.5,2.0,0.5,1.0,1.0,2.0,1.0,1.0,1.0,1.0 ],# 3 - Poison
   [ 1.0,1.0,0.0,2.0,1.0,2.0,0.5,1.0,2.0,1.0,0.5,2.0,1.0,1.0,1.0 ],# 4 - Ground
   [ 1.0,0.5,2.0,1.0,0.5,1.0,2.0,1.0,2.0,1.0,1.0,1.0,1.0,2.0,1.0 ],# 5 - Rock
   [ 1.0,0.5,0.5,2.0,1.0,1.0,1.0,0.5,0.5,1.0,2.0,1.0,2.0,1.0,1.0 ],# 6 - Bug
   [ 0.0,1.0,1.0,1.0,1.0,1.0,1.0,2.0,1.0,1.0,1.0,1.0,0.0,1.0,1.0 ],# 7 - Ghost
   [ 1.0,1.0,1.0,1.0,1.0,0.5,2.0,1.0,0.5,0.5,2.0,1.0,1.0,2.0,0.5 ],# 8 - Fire
   [ 1.0,1.0,1.0,1.0,2.0,2.0,1.0,1.0,2.0,0.5,0.5,1.0,1.0,1.0,0.5 ],# 9 - Water
   [ 1.0,1.0,0.5,0.5,2.0,2.0,0.5,1.0,0.5,2.0,0.5,1.0,1.0,1.0,0.5 ],#10 - Grass
   [ 1.0,1.0,2.0,1.0,0.0,1.0,1.0,1.0,1.0,2.0,0.5,0.5,1.0,1.0,0.5 ],#11 - Electr
   [ 1.0,2.0,1.0,2.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.5,1.0,1.0 ],#12 - Psychc
   [ 1.0,1.0,2.0,1.0,2.0,1.0,1.0,1.0,1.0,0.5,2.0,1.0,1.0,0.5,2.0 ],#13 - Ice
   [ 1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,2.0 ] #14 - Dragon
            ]

   def base_damage ( self, pokeA, atk, pokeB ):
      termo1 = ( 2 * pokeA.get_level () + 10 ) / 250
      termo2 = pokeA.get_atk () / pokeB.get_def () * atk.get_power ()
      print ( '# DEBUG base_damage = ', ( termo1 * termo2 + 2 ) )
      return ( termo1 * termo2 + 2 )

   def stab ( self, poke, atk ):
      if poke.get_type1 () == atk.get_type ():
         print ( '# DEBUG stab = 1.5' )
         return 1.5
      if poke.get_type2 () == atk.get_type ():
         print ( '# DEBUG stab = 1.5' )
         return 1.5
      print ( '# DEBUG stab = 1.0' )
      return 1.0

   def type_effect ( self, atk, poke ):
      effect = self.tabela[atk.get_type ()][poke.get_type1 ()]
      if poke.get_type2 () != 15:
         print ( '# DEBUG  entra', poke.get_type2 () )
         print ( '# DEBUG tabela =',
                   self.tabela[ atk.get_type () ][ poke.get_type2 () ] )
         effect = effect * self.tabela[atk.get_type ()][poke.get_type2 ()]
      print ( '# DEBUG effect =', effect )
      return effect

   def critical ( self ):
      if random.random () >= 0.9:
         print ( '# DEBUG Critical = 2' )
         return 2
      else:
         print ( '# DEBUG Critical = 1' )
         return 1

   def rand ( self ):
      num = random.uniform ( 0.85, 1 )
      print ( '# DEBUG rand =', num )
      return num 

   def modifier_damage ( self, pokeA, mov, pokeB ):
      termo1 = self.stab( pokeA, mov ) * self.type_effect ( mov, pokeB )
      termo2 = self.critical () * self.rand ()
      print ( '# DEBUG modifier_damage =', ( termo1 * termo2 ) )
      return ( termo1 * termo2 )

   def damage ( self, pokeA, mov, pokeB ):
      dano = self.base_damage ( pokeA, mov, pokeB )
      dano = dano * self.modifier_damage ( pokeA, mov, pokeB )
      print ( '# DEBUG dano =', dano )
      return int ( dano )

   def __init__ ( self ):
      print ( '--- Player 1 ---' )
      self.poke1 = pkm.Pokemon ()
      print ( '--- Player 2 ---' )
      self.poke2 = pkm.Pokemon ()
      self.contador = 0
      self.batalha ()

   def batalha ( self ):
      print ( '--- Inicio da Batalha ---' )
      while self.rodada () == True:
         pass

      print ( '--- Fim da Batalha ---' )
      print ( 'Batalha terminou no turno:', self.contador )
      if self.poke1.esta_vivo:
         print ( 'Vitoria do Player 1' )
      else:
         print ( 'Vitoria do Player 2' )

   def rodada ( self ):
      if self.poke1.get_spd () > self.poke2.get_spd ():
         primeiro = self.poke1
         segundo  = self.poke2
      else:
         primeiro = self.poke2
         segundo  = self.poke1

      self.contador = self.contador + 1

      if primeiro.esta_vivo () and segundo.esta_vivo ():
         self.turno ( primeiro, segundo )
      else:
         return False

      if primeiro.esta_vivo () and segundo.esta_vivo ():
         self.turno ( segundo, primeiro )
      else:
         return False

      return True

   def mostra_info_baixo ( self, poke1, poke2 ):
      print ()
      print ( '### Turno', self.contador, '###' )
      print ()
      print ( '\  +---' )
      print ( ' \ | Nome:', poke1.get_name () )
      print ( ' / | HP:', poke1.get_hp (), '/', poke1.get_hpmax () )
      print ( '/  +---' )
      print ()
      print ( '     +--+'   )
      print ( '     |  |'   )
      print ( '   +-+  +-+' )
      print ( '    \    /'  )
      print ( '     \  /'   )
      print ( '      \/'    )
      print ()
      print ( '   +---' )
      print ( '   | Nome:', poke2.get_name () )
      print ( '   | HP:', poke2.get_hp (), '/', poke2.get_hpmax () )
      print ( '   +---' )

   def mostra_informacoes ( self, poke ):
      print ()
      print ( '+---' )
      print ( '| Noome:', poke.get_name () )
      print ( '| HP:', poke.get_hp (), '/', poke.get_hpmax () )
      print ( '+---' )
      print ()

   def turno ( self, ataque, defesa ):
      move_struggle = False
      self.mostra_info_turno ( ataque, defesa )

      if ataque.possui_ataques ():
         ataque.mostra_ataques ()

         while ( True ):
            opt = int ( input ( 'Qual ataque executar? ' ) )
            if opt >= 0 and opt < ataque.get_numAtk ():
               if ataque.moveset[opt].get_pp () < 1:
                  print ( 'No moves left' )
               else:
                  break
            else:
               print ( 'ERRO: Ataque invalido' )
      else:
         move_struggle = True
         print ( ataque.get_name (), 'nao possui mais ataques.' )
         opt = ataque.get_numAtk ()

      # calcula e aplica o dano ao defensor e mostra suas informacoes
      atk = ataque.moveset[opt]
      dano = self.damage ( ataque, atk, defesa )
      defesa.set_hp ( defesa.get_hp () - dano )
      self.mostra_informacoes ( defesa )

      if move_struggle and defesa.esta_vivo ():
         # pelo que entendi o atacante so sofre recoil se o
         # defensor estiver vivo
         print ( ataque.get_name (), 'is damaged by recoil' )
         dano = int ( dano * 0.5 )
         ataque.set_hp ( ataque.get_hp - dano )
         self.mostra_informacoes ( ataque )
