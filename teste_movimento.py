#!/usr/bin/python3

import movimento as mov
import unittest as uni
import sys
import os


# Rotina para testar objetos do tipo Movimento()
class TestadorMovimento(uni.TestCase):
   def setUp(self):
      if os.path.isfile('in_mov') == False:
         # Redireciona arq para stdin
         with open('in_mov', 'w+') as arq:
            arq.write('blaster\n-1\n15\n1\n-10\n200\n90\n-50\n256\n50\n-40\n62\n40\n')
      with open('in_mov', 'r') as sys.stdin:
         self.blaster = mov.Movimento()

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
   # set_power
   def testa_set_power_infe(self):
      temp = self.blaster.get_power()
      self.blaster.set_power(-1)
      self.assertEqual(temp, self.blaster.get_power())
   def testa_set_power_supe(self):
      temp = self.blaster.get_power()
      self.blaster.set_power(256)
      self.assertEqual(temp, self.blaster.get_power())
   def testa_set_power_valido(self):
      temp = self.blaster.get_power()
      self.blaster.set_power(70)
      self.assertEqual(70, self.blaster.get_power())

   # set_ppmax
   def testa_set_power_infe(self):
      temp = self.blaster.get_ppmax()
      self.blaster.set_ppmax(-1)
      self.assertEqual(temp, self.blaster.get_ppmax())
   def testa_set_power_supe(self):
      temp = self.blaster.get_ppmax()
      self.blaster.set_ppmax(62)
      self.assertEqual(temp, self.blaster.get_ppmax())
   def testa_set_power_valido(self):
      temp = self.blaster.get_ppmax()
      self.blaster.set_ppmax(30)
      self.assertEqual(30, self.blaster.get_ppmax())

   # set_pp
   def testa_set_power_infe(self):
      temp = self.blaster.get_pp()
      self.blaster.set_pp(-1)
      self.assertEqual(temp, self.blaster.get_pp())
   def testa_set_power_supe(self):
      temp = self.blaster.get_pp()
      self.blaster.set_pp(70)
      self.assertEqual(temp, self.blaster.get_pp())
   def testa_set_power_valido(self):
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
