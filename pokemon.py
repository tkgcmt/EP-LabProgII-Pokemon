# |Contribuidores              | No. USP |
# |----------------------------|---------|
# |Christian M. T. Takagi      | 7136971 |
# |Cinthia M Tanaka            | 5649479 |
# |Daniel A. Nagata            | 7278048 |
# |Fernando T. Tanaka          | 6920230 |
#-------------------------------------------------------------------------------
# Disciplina: Laboratório de Programação II       
# Prof. Alfredo Goldman
# Exercicio Programa - Etapa 2
# Arquivo: pokemon.py
#-------------------------------------------------------------------------------

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
         self.lvl = 0
         try:
            temp = int ( input ( 'Digite o level do pokemon: \n' ) )
            self.set_lvl(temp)
            if self.lvl:
               break
         except ValueError:
            print ( 'ERROR: Level invalido' )
            pass
      # hpmax
      while ( True ):
         self.hpmax = 0
         try:
            temp = int ( input ( 'Digite a vida do pokemon: \n' ) )
            self.set_hpmax(temp)
            if self.hpmax: 
               self.hpmax = self.calcula_status(self.hpmax, self.lvl, 50, 10)
               self.hp = self.hpmax
               break
         except ValueError:
            print ( 'ERRO: Valor de vida invalido' )
            pass
      # atk 
      while ( True ):
         self.atk = 0
         try:
            temp = int ( input ( 'Digite o ataque do pokemon: \n' ) )
            self.set_atk(temp) 
            if self.atk :
               self.atk = self.calcula_status(self.atk, 50, 0, 5)
               break
         except ValueError:
            print ( 'ERRO: Valor de ataque invalido' )
            pass
      # def 
      while ( True ):
         self.defe = 0
         try:
            temp = int ( input ( 'Digite a defesa do pokemon: \n' ) )
            self.set_defe(temp) 
            if self.defe :
               self.defe = self.calcula_status(self.defe, 50, 0, 5)
               break
         except ValueError:
            print ( 'ERRO: Valor de defesa invalido' )
            pass
      # spd 
      while ( True ):
         self.spd = 0
         try:
            temp = int ( input ( 'Digite a velocidade do pokemon: \n' ) )
            self.set_spd(temp) 
            if self.spd :
               self.spd = self.calcula_status(self.spd, 50, 0, 5)
               break
         except ValueError:
            print ( 'ERRO: Valor de velocidade invalido' )
            pass
      # spc 
      while ( True ):
         self.spc = 0
         try:
            temp = int ( input ( 'Digite o especial do pokemon: \n' ) )
            self.set_spc(temp) 
            if self.spc :
               self.spc = self.calcula_status(self.spc, 50, 0, 5)
               break
         except ValueError:
            print ( 'ERRO: Valor de especial invalido' )
            pass
      # type1
      while ( True ):
         self.type1 = 17
         try:
            temp = int ( input ( 'Digite o tipo 1 do pokemon: \n' ) )
            self.set_type1(temp)
            if self.type1 < 17:
               break
         except ValueError:
            print ( 'ERRO: Tipo 1 invalido' )
            pass
      # type2
      while ( True ):
         self.type2 = 17
         try:
            temp = input ( 'Digite o tipo 2 do pokemon: \n' )
            self.set_type2(temp)
            if self.type2 < 17:
               break
         except ValueError:
            print ( 'ERRO: Tipo 2 invalido' )
            pass
      # numAtk
      while ( True ):
         try:
            self.numAtk = int ( input ( 'Digite o numero de ataques do pokemon: \n'))
            if self.numAtk >= 0 and self.numAtk <= 4:
               self.moveset = []
               self.moveset.append ( self.struggle )
               for i in range ( self.numAtk ):
                  print ( '--- Ataque', i + 1, '---' )
                  self.moveset.append ( mov.Movimento () )
               break
            else:
               print ( 'ERRO: Numero invalido de ataques' )
         except ValueError:
            print ( 'ERRO: Numero invalido de ataques' )
            pass
      print('\n')
      self.mostra_pkmn()
      self.mostra_lista_movimentos()
            

   ### Getters
   def get_name ( self ):
      return self.name

   def get_lvl ( self ):
      return self.lvl

   def get_hp ( self ):
      return self.hp

   def get_hpmax ( self ):
      return self.hpmax

   def get_atk ( self ):
      return self.atk

   def get_defe ( self ):
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
      self.name = nome;

   def set_lvl ( self, level ):
      if level >= 1 and level <= 100:
         self.lvl = level
      else:
         print( 'ERRO: Level invalido. Dom=[1,100]' )

   def set_hp ( self, vida ):
      if vida >= 0:
         if vida <= self.get_hpmax ():
            self.hp = vida
         else:
            self.hp = self.hpmax
      else:
         self.hp = 0

   def set_hpmax ( self, vida ):
      if vida >= 1 and vida <= 255:
         self.hpmax = vida
      else:
         print( 'ERRO: Vida invalido. Dom=[1,255]' )

   def set_atk ( self, ataque ):
      if ataque >= 1 and ataque <= 255:
         self.atk = ataque
      else:
         print( 'ERRO: Ataque invalido. Dom=[1,255]' )

   def set_defe ( self, defesa ):
      if defesa >= 1 and defesa <= 255:
         self.defe = defesa
      else:
         print( 'ERRO: Defesa invalido. Dom=[1,255]' )

   def set_spd ( self, velocidade ):
      if velocidade >= 1 and velocidade <= 255:
         self.spd = velocidade
      else:
         print( 'ERRO: Velocidade invalido. Dom=[1,255]' )

   def set_spc ( self, especial ):
      if especial >= 1 and especial <= 255:
         self.spc = especial
      else:
         print ( 'ERRO: Especial invalido. Dom=[1,255]' )
         return False

   def set_type1 ( self, tipo ):
      if tipo >= 0 and tipo <= 15:
         self.type1 = tipo
      else:
         print ( 'ERRO: Tipo 1 invalido. Dom=[0,15]' )
         return False

   def set_type2 ( self, tipo ):
      if tipo == '':
         self.type2 = 16
      else:
         tipo = int(tipo)
         if tipo >= 0 and tipo <= 16:
            self.type2 = tipo
         else:
            print ( 'ERRO: Tipo 2 invalido. Dom=[0,16]' )
            return False

   def set_numAtk ( self, num ):
      if num >= 0 and num <= 4:
         self.numAtk = num
         
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
         print(self.mostra_ataque( i + 1 ))
      print('\n')

   # mostra se o pokemon esta vivo ou nao
   def esta_vivo ( self ):
      if self.hp > 0:
         return True
      else:
         return False

   # calcula status de acordo com seu nivel e a constante base
   def calcula_status( self, base, level, var1, var2 ):
      return int((base+var1)*level/50 + var2)

   # imprime os status do pokemon
   def mostra_pkmn(self):
      print(self.get_name())
      print('Lvl: ', self.get_lvl())
      print('tipo 1:', self.get_type1(), '/', 'tipo 2:', self.get_type2())
      print('HP: ', self.get_hp())
      print('ATK: ', self.get_atk())
      print('DEF: ', self.get_defe())
      print('SPD: ', self.get_spd())
      print('SPC: ', self.get_spc())

   def cria_moveset ( self ):
      self.moveset = []
