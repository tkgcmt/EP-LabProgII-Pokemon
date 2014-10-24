#!/usr/bin/python3

import movimento as mov
import unittest as uni
import sys


# Rotina para testar objetos do tipo Movimento()
class TestadorArena(uni.TestCase):
   def setUp(self):
      arq = open('in_mov', 'w+')
      arq.write('blaster\n-1\n15\n1\n-10\n200\n90\n-50\n50\n256\n-40\n62\n40\n')
      arq.close()
      arq = open('in_mov', 'r')
      sys.stdin = arq
      self.blaster = mov.Movimento()


   # Testa se a leitura da entrada verifica os erros de valores extremos e testa os getters tambem.
   def testaEntrada(self):
      self.assertEqual('blaster' , self.blaster.get_name())
      self.assertEqual(1, self.blaster.get_type())
      self.assertEqual(90, self.blaster.get_accu())
      self.assertEqual(50, self.blaster.get_power())
      self.assertEqual(40, self.blaster.get_ppmax())
      self.assertEqual(40, self.blaster.get_pp())

   # Testa se os setters estao funcionando corretamente
   def testaSetters(self):
      # set_power
      temp = self.blaster.get_power()
      self.blaster.set_power(-1)
      self.assertEqual(temp, self.blaster.get_power())
      self.blaster.set_power(256)
      self.assertEqual(temp, self.blaster.get_power())
      self.blaster.set_power(70)
      self.assertEqual(70, self.blaster.get_power())

      # set_ppmax
      temp = self.blaster.get_ppmax()
      self.blaster.set_ppmax(-1)
      self.assertEqual(temp, self.blaster.get_ppmax())
      self.blaster.set_ppmax(62)
      self.assertEqual(temp, self.blaster.get_ppmax())
      self.blaster.set_ppmax(30)
      self.assertEqual(30, self.blaster.get_ppmax())

      # set_pp
      temp = self.blaster.get_pp()
      self.blaster.set_pp(-1)
      self.assertEqual(temp, self.blaster.get_pp())
      self.blaster.set_pp(70)
      self.assertEqual(temp, self.blaster.get_pp())
      self.blaster.set_pp(15)
      self.assertEqual(15, self.blaster.get_pp())
      
   # Testa se eh possivel utilizar este ataque
   def testa_tem_movimentos(self):
      self.assertEqual(True, self.blaster.tem_movimentos())
      self.blaster.set_pp(0)
      self.assertEqual(False, self.blaster.tem_movimentos())

   # Testa se a redução do pp está funcionando corretamente
   def testa_reduz_pp(self):
      temp = self.blaster.get_pp()
      self.blaster.reduz_pp()
      self.assertEqual(temp - 1, self.blaster.get_pp())
      
if __name__ == '__main__':
   uni.main()
