'''
|Contribuidores              | No. USP |
|----------------------------|---------|
|Christian M. T. Takagi      | 7136971 |
|Cinthia M Tanaka            | 5649479 |
|Daniel A. Nagata            | 7278048 |
|Fernando T. Tanaka          | 6920230 |

Disciplina: Laboratório de Programação II       
Prof. Alfredo Goldman
Exercicio Programa - Etapa 1                    
Arquivo: pokemon.py
'''

import movimento as mov

class Pokemon:
   ### Criacao do ataque struggle
   struggle = mov.Movimento.__new__ ( mov.Movimento )
   struggle.name = 'Struggle'
   struggle.type = 0 
   struggle.accu = 100
   struggle.power = 50
   struggle.ppmax = 10
   struggle.pp = 10

   def __init__ ( self ):
      # name
      self.name = input ( 'Digite o nome do pokemon: \n' )
      # lvl
      while ( True ):
         try:
            self.lvl = int ( input ( 'Digite o level do pokemon: \n' ) )
            if self.lvl >= 1 and self.lvl <= 100:
               break
            else:
               print ( 'ERROR: Level invalido' )
         except ValueError:
            print ( 'ERROR: Level invalido' )
            pass
      # hpmax
      while ( True ):
         try:
            self.hpmax = int ( input ( 'Digite a vida do pokemon: \n' ) )
            if self.hpmax >= 1 and self.hpmax < 255:
               self.hp = self.hpmax
               break
            else:
               print ( 'ERRO: Valor de vida invalido' )
         except ValueError:
            print ( 'ERRO: Valor de vida invalido' )
            pass
      # atk
      while ( True ):
         try:
            self.atk = int ( input ( 'Digite o ataque do pokemon: \n' ) )
            if self.atk >= 0 and self.atk <= 255:
               break
            else:
               print ( 'ERRO: Valor de ataque invalido' )
         except ValueError:
            print ( 'ERRO: Valor de ataque invalido' )
            pass
      # def
      while ( True ):
         try:
            self.defe = int ( input ( 'Digite a defesa do pokemon: \n' ) )
            if self.defe >= 0 and self.defe <= 255:
               break
            else:
               print ( 'ERRO: Valor de defesa invalido' )
         except ValueError:
            print ( 'ERRO: Valor de defesa invalido' )
            pass
      # spd
      while ( True ):
         try:
            self.spd = int ( input ( 'Digite a velocidade do pokemon: \n' ) )
            if self.spd >= 0 and self.spd <= 255:
               break
            else:
               print ( 'ERRO: Valor de velocidade invalido' )
         except ValueError:
            print ( 'ERRO: Valor de velocidade invalido' )
            pass
      # spc
      while ( True ):
         try:
            self.spc = int ( input ( 'Digite o especial do pokemon: \n' ) )
            if self.spc >= 0 and self.spc <= 255:
               break
            else:
               print ( 'ERRO: Valor de especial invalido' )
         except ValueError:
            print ( 'ERRO: Valor de especial invalido' )
            pass
      # type1
      while ( True ):
         try:
            self.type1 = int ( input ( 'Digite o tipo 1 do pokemon: \n' ) )
            if self.type1 >= 0 and self.type1 <= 15:
               break
            else:
               print ( 'ERRO: Tipo 1 invalido' )
         except ValueError:
            print ( 'ERRO: Tipo 1 invalido' )
            pass
      # type2
      while ( True ):
         try:
            self.type2 = input ( 'Digite o tipo 2 do pokemon: \n' )
            if self.type2 == '':
               self.type2 = 16
            else:
               self.type2 = int ( self.type2 )
            if self.type2 >= 0 and self.type2 <= 16:
               break
            else:
               print ( 'ERRO: Tipo 2 invalido' )
         except ValueError:
            print ( 'ERRO: Tipo 2 invalido' )
            pass
      # numAtk
      while ( True ):
         try:
            self.numAtk = int ( input ( 'Digite o numero de ataques do pokemon: \n'))
            if self.numAtk >= 0 and self.numAtk <= 4:
               self.moveset = []
               for i in range ( self.numAtk ):
                  print ( '--- Ataque', i, '---' )
                  self.moveset.append ( mov.Movimento () )
               self.moveset.append ( self.struggle )
               break
            else:
               print ( 'ERRO: Numero invalido de ataques' )
         except ValueError:
            print ( 'ERRO: Numero invalido de ataques' )
            pass
            

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
   def set_hp ( self, vida ):
      if vida >= 0:
         if vida <= self.hpmax:
            self.hp = vida
         else:
            self.hp = self.hpmax
      else:
         self.hp = 0
         
   '''
   def set_name ( self, nome ):
      self.name = nome

   def set_level ( self, level ):
      self.lvl = level

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

   '''
   ### Metodos
   def possui_ataques ( self ):
      for i in range ( self.numAtk ):
         atk = self.moveset[i]
         if atk.tem_movimentos() == True:
            return True
      return False
   
   # mostra o ataque de indice i do objeto
   def mostra_ataque ( self, i ):
      ptr = self.get_movimento ( i )
      linha = ('  '+ str(i) + ' - ' + ptr.get_name() + '  PP:( '
      + str(ptr.get_pp ()) + ' / ' + str(ptr.get_ppmax ()) + ' )')
      return linha 

   # mostra a lista de ataques do objeto
   def mostra_lista_movimentos ( self ):
      print ( self.name )
      for i in range ( self.numAtk ):
         print(self.mostra_ataque( i ))
      print('\n')

   def esta_vivo ( self ):
      if self.hp > 0:
         return True
      else:
         return False
