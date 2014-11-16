#!/usr/bin/python3
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
# Arquivo: teste_movimento.py
#-------------------------------------------------------------------------------

import movimento as mov
import unittest as uni
import sys


# Rotina para testar objetos do tipo Movimento()
class TestadorMovimento(uni.TestCase):
   def setUp(self):
      # Redireciona arq para stdin
      with open('in_mov', 'w+') as arq:
         arq.write('blaster\n-1\n16\n1\n-10\n200\n90\n-50\n256\n50\n-40\n62\n40\n')
      with open('in_mov', 'r') as sys.stdin:
         self.blaster = mov.Movimento()

   def tearDown(self):
      sys.stdin = sys.__stdin__

   # Testa o tratamento da entrada corrigiu os valores extremos ao mesmo tempo
   # que testa os getters.
   def testa_get_name(self):
      self.assertEqual(self.blaster.name, self.blaster.get_name())
   def testa_get_type(self):
      self.assertEqual(self.blaster.type, self.blaster.get_type())
   def testa_get_accu(self):
      self.assertEqual(self.blaster.accu, self.blaster.get_accu())
   def testa_get_power(self):
      self.assertEqual(self.blaster.power, self.blaster.get_power())
   def testa_get_ppmax(self):
      self.assertEqual(self.blaster.ppmax, self.blaster.get_ppmax())
   def testa_get_pp(self):
      self.assertEqual(self.blaster.pp, self.blaster.get_pp())


   # Testa se os setters estao funcionando corretamente
   # set_pp
   def testa_set_pp_infe(self):
      temp = self.blaster.get_pp()
      self.blaster.set_pp(-1)
      self.assertEqual(temp, self.blaster.get_pp())
   def testa_set_pp_supe(self):
      temp = self.blaster.get_pp()
      self.blaster.set_pp(70)
      self.assertEqual(temp, self.blaster.get_pp())
   def testa_set_pp_valido(self):
      temp = self.blaster.get_pp()
      self.blaster.set_pp(15)
      self.assertEqual(15, self.blaster.get_pp())
     

   # Testa se eh possivel utilizar este ataque
   def testa_tem_movimentos_nao_nulo(self):
      self.assertEqual(True, self.blaster.tem_movimentos())
   def testa_tem_movimentos_nulo(self):
      self.blaster.pp = 0
      self.assertEqual(False, self.blaster.tem_movimentos())


   # Testa se a redução do pp está funcionando corretamente
   def testa_reduz_pp_nao_nulo(self):
      temp = self.blaster.get_pp()
      self.blaster.reduz_pp()
      self.assertEqual(temp - 1, self.blaster.get_pp())
   # Deve imprimir uma mensagem de erro, mas nao quebra o programa.
   def testa_reduz_pp_nulo(self):
      self.blaster.pp = 0
      self.blaster.reduz_pp()
      self.assertEqual(0, self.blaster.get_pp())
      
if __name__ == '__main__':
   uni.main(buffer=True)
