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
# Arquivo: movimento.py
#-------------------------------------------------------------------------------

class Movimento:
   def __init__ ( self ):
      # attack name
      self.name = input ( 'Digite o nome do ataque: \n' )
      # type
      while ( True ):
         self.type = 17
         try:
            temp = int ( input ( 'Digite o tipo do ataque: \n' ) )
            self.__set_type(temp)
            if self.type < 17:
               break
         except ValueError:
            print ( 'ERRO: Tipo invalido. Tente novamente' )

      # accuracy
      while ( True ):
         self.accu = 0
         try:
            temp = int ( input ( 'Digite a acuracia do ataque: \n' ) )
            self.__set_accu(temp)
            if (self.accu):
               break
            else:
               print ( 'ERRO: Acuracia invalida. Tente novamente' )
         except ValueError:
            print ( 'ERRO: Acuracia invalida. Tente novamente' )

      # power
      while (True):
         self.power = 0
         try:
            temp = int ( input ( 'Digite o poder do ataque: \n' ) ) 
            self.__set_power(temp)
            if self.power:
               break
            else:
               print ( 'ERRO: Poder do ataque invalido. Tente novamente' )
         except ValueError:
            print ( 'ERRO: Poder do ataque invalido. Tente novamente' )
            pass

      # ppmax
      while (True):
         self.ppmax = 0
         try:
            temp = int ( input ( 'Digite quantos power points: \n' ) )
            self.__set_ppmax(temp)
            if self.ppmax:
               break
            else:
               print ( 'ERRO: Valor de Power points invalido. Tente novamente' )
         except ValueError:
            print ( 'ERRO: Valor de Power points invalido. Tente novamente' )
      # pp
      self.pp = self.ppmax

   ### Getters
   def get_name ( self ):
      return self.name

   def get_type ( self ):
      return self.type

   def get_accu ( self ):
      return self.accu

   def get_power ( self ):
      return self.power

   def get_ppmax ( self ):
      return self.ppmax

   def get_pp ( self ):
      return self.pp

   ### Setters - se o novo valor for invalido, mantem o valor anterior
   def __set_type( self, tipo):
      if tipo >= 0 and tipo <= 15:
         self.type = tipo
      else:
         print ( 'ERRO: Tipo invalido. Dom=[0,15]' )

   def __set_accu( self, acuracia):
      if acuracia >= 0 and acuracia <= 100:
         self.accu = acuracia
      else:
         print ( 'ERRO: invalido. Dom=[0,100]' )

   def __set_power ( self, poder ):
      if poder >= 0 and poder <= 100:
         self.power = poder
      else:
         print ( 'ERRO: invalido. Dom=[0,100]' )
         
   def __set_ppmax ( self, pontos ):
      if pontos >= 0 and pontos <= 61:
         self.ppmax = pontos
      else:
         print ( 'ERRO: invalido. Dom=[0,61]' )

   def set_pp ( self, pontos ):
      if pontos >= 0 and pontos <= self.ppmax:
         self.pp = pontos
      else:
         print ( 'ERRO: invalido. Dom=(0,%d)' %self.ppmax )

   ### Metodos
   def tem_movimentos ( self ):
      if self.pp > 0:
         return True
      else:
         return False

   def reduz_pp ( self ):
      if self.pp != 0:
         self.pp -= 1
      else:
         print('ERRO: (PP) - Algo esta errado, mas podemos continuar.\n')
