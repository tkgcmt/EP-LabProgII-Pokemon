import movimento as mov

class Pokemon:

   ### Criacao do ataque struggle
   struggle = mov.Movimento.__new__ ( mov.Movimento )
   struggle.set_name ( 'Struggle' )
   struggle.set_type ( 0 )
   struggle.set_accu ( 100 )
   struggle.set_power ( 50 )
   struggle.set_ppmax ( 10 )
   struggle.set_pp ( 10 )

   def __init__ ( self ):
      self.name = input ( 'Digite o nome do pokemon: ' )

      while ( True ):
         self.lvl = int ( input ( 'Digite o level do pokemon: ' ) )
         if self.lvl >= 1 and self.lvl <= 100:
            break
         else:
            print ( 'ERROR: Level invalido' )

      while ( True ):
         self.hpmax = int ( input ( 'Digite a vida do pokmeon: ' ) )
         if self.hpmax >= 1:
            self.hp = self.hpmax
            break
         else:
            print ( 'ERRO: Valor de vida invalido' )

      while ( True ):
         self.atk = int ( input ( 'Digite o ataque do pokemon: ' ) )
         if self.atk >= 0 and self.atk <= 255:
            break
         else:
            print ( 'ERRO: Valor de ataque invalido' )

      while ( True ):
         self.defe = int ( input ( 'Digite a defesa do pokemon: ' ) )
         if self.defe >= 0 and self.defe <= 255:
            break
         else:
            print ( 'ERRO: Valor de defesa invalido' )

      while ( True ):
         self.spd = int ( input ( 'Digite a velocidade do pokemon: ' ) )
         if self.spd >= 0 and self.spd <= 255:
            break
         else:
            print ( 'ERRO: Valor de velocidade invalido' )

      while ( True ):
         self.spc = int ( input ( 'Digite o especial do pokemon: ' ) )
         if self.spc >= 0 and self.spc <= 255:
            break
         else:
            print ( 'ERRO: Valor de especial invalido' )

      while ( True ):
         self.type1 = int ( input ( 'Digite o tipo 1 do pokemon: ' ) )
         if self.type1 >= 0 and self.type1 <= 14:
            break
         else:
            print ( 'ERRO: Tipo 1 invalido' )

      while ( True ):
         self.type2 = input ( 'Digite o tipo 2 do pokemon: ' )
         if self.type2 == '':
            self.type2 = 15
         else:
            self.type2 = int ( self.type2 )
         if self.type2 >= 0 and self.type2 <= 15:
            break
         else:
            print ( 'ERRO: Tipo 2 invalido' )

      while ( True ):
         self.numAtk = int ( input ( 'Digite o numero de ataques do pokemon: '))
         if self.numAtk > 0 and self.numAtk <= 4:
            self.moveset = []
            for i in range ( self.numAtk ):
               print ( '--- Ataque', i, '---' )
               self.moveset.append ( mov.Movimento () )
            self.moveset.append ( self.struggle )
            break
         else:
            print ( 'ERRO: Numero invalido de ataques' )

   ### Getters
   def get_name ( self ):
      return self.name

   def get_level ( self ):
      return self.lvl

   def get_hp ( self ):
      return self.hp

   def get_hpmax ( self ):
      return self.hpmax

   def get_atk ( self ):
      return self.atk

   def get_def ( self ):
      return self.defe

   def get_spd ( self ):
      return self.spd

   def get_spc ( self ):
      return self.spc

   def get_type1 ( self ):
      return self.type1

   def get_type2 ( self ):
      return self.type2

   def get_numAtk ( self ):
      return self.numAtk

   def get_movimento ( self, num ):
      return self.moveset[num]

   ### Setters
   def set_name ( self, nome ):
      self.name = nome

   def set_level ( self, level ):
      self.lvl = level

   def set_hp ( self, vida ):
      self.hp = vida

   def set_hpmax ( self, vida ):
      self.hpmax = vida

   def set_atk ( self, ataque ):
      self.atk = ataque

   def set_def ( self, defesa ):
      self.defe = defesa

   def set_spd ( self, velocidade ):
      self.spd = velocidade

   def set_spc ( self, especial ):
      self.spc = especial

   def set_type1 ( self, tipo ):
      if tipo >= 0 and tipo <= 14:
         self.type1 = tipo
      else:
         print ( 'ERRO: Tipo invalido' )

   def set_type2 ( self, tipo ):
      if tipo >= 0 and tipo <= 15:
         self.type2 = tipo
      else:
         print ( 'ERRO: TIpo invalido' )

   ### Metodos
   def possui_ataques ( self ):
      for i in range ( self.numAtk ):
         atk = self.moveset[i]
         if atk.get_pp () > 0:
            return True
      return False

   def mostra_ataques ( self ):
      print ( self.name )
      for i in range ( self.numAtk ):
         ptr = self.get_movimento ( i )
         print ( '  ', i, '-', ptr.get_name (), ' (', ptr.get_pp (), '/',
                 ptr.get_ppmax (), ')' )

   def esta_vivo ( self ):
      if self.hp > 0:
         return True
      else:
         return False
