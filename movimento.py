class Movimento:

   def __init__ ( self ):
      self.name = input ( 'Digite o nome do ataque: ' )
   
      while ( True ):
         self.type = int ( input ( 'Digite o tipo do ataque: ' ) )
         if self.type >= 0 and self.type < 15:
            break
         else:
            print ( 'ERRO: Tipo invalido' )

      while ( True ):
         self.accu = int ( input ( 'Digite a acuracia do ataque: ' ) )
         if self.accu >= 0 and self.accu < 101:
            break
         else:
            print ( 'ERRO: Acuracia invalida' )

      self.power = int ( input ( 'Digite o poder do ataque: ' ) )
      self.ppmax = int ( input ( 'Digite quantos power points: ' ) )
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

   ### Setters
   def set_name ( self, nome ):
      self.name = nome

   def set_type ( self, tipo ):
      if tipo >= 0 and tipo < 15:
         self.type = tipo
      else:
         print ( 'ERRO: Tipo invalido' )

   def set_accu ( self, acur ):
      self.accu = acur

   def set_power ( self, poder ):
      self.power = poder

   def set_ppmax ( self, pontos ):
      self.ppmax = pontos

   def set_pp ( self, pontos ):
      self.pp = pontos

   ### Metodos
   def tem_movimentos ( self ):
      if self.pp > 0:
         return True
      else:
         return False

   def reduz_pp ( self ):
      self.pp = self.pp - 1
