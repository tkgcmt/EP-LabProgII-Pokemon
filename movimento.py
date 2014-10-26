class Movimento:

   def __init__ ( self ):
      # attack name
      self.name = input ( 'Digite o nome do ataque: \n' )
      # type
      while ( True ):
         try:
            self.type = int ( input ( 'Digite o tipo do ataque: \n' ) )
            if self.type >= 0 and self.type < 15:
               break
            else:
               print ( 'ERRO: Tipo invalido. Tente novamente' )
         except ValueError:
            print ( 'ERRO: Tipo invalido. Tente novamente' )

      # accuracy
      while ( True ):
         try:
            self.accu = int ( input ( 'Digite a acuracia do ataque: \n' ) )
            if self.accu >= 0 and self.accu < 101:
               break
            else:
               print ( 'ERRO: Acuracia invalida. Tente novamente' )
         except ValueError:
            print ( 'ERRO: Acuracia invalida. Tente novamente' )

      #power
      while (True):
         try:
            self.power = int ( input ( 'Digite o poder do ataque: \n' ) ) 
            if self.power >=0 and self.power <=255:
               break;
            else:
               print ( 'ERRO: Poder do ataque invalido. Tente novamente' )
         except ValueError:
            print ( 'ERRO: Poder do ataque invalido. Tente novamente' )
            pass

      # ppmax
      while (True):
         try:
            self.ppmax = int ( input ( 'Digite quantos power points: \n' ) )
            if self.ppmax>=0 and self.ppmax<=61:
               break;
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
   def set_power ( self, poder ):
      if poder >=0 and poder <=255:
         self.power = poder

   def set_ppmax ( self, pontos ):
      if pontos >=0 and pontos <= 61:
         self.ppmax = pontos

   def set_pp ( self, pontos ):
      if pontos >= 0 and pontos <= self.ppmax:
         self.pp = pontos

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
