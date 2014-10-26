#!/usr/bin/python3

import arena as are
import pokemon as pok
import unittest as uni
import sys
import os

# Rotina para testar objetos do tipo Arena()
class TestadorArena(uni.TestCase):
   def setUp(self):
      if os.path.isfile('in_arena') == False:
         with open('in_arena', 'w+') as arq:
            arq.write('Muk\n50\n105\n105\n75\n50\n65\n3\n\n2\n'
                      'Pound\n0\n100\n40\n35\n'
                      'Sludge\n3\n100\n65\n20\n'
                      'Mew\n50\n100\n100\n100\n100\n100\n13\n\n3\n'
                      'Pound\n0\n100\n40\n35\n'
                      'Mega Punch\n0\n85\n80\n10\n'
                      'Psychic\n12\n100\n90\n10\n')

      with open('in_arena', 'r') as sys.stdin:
         self.muk = pok.Pokemon()
         self.mew = pok.Pokemon()
      self.a = are.Arena()

   # Testa o metodo base_damage()
   def testa_base_damage_atk(self):
      atk = self.muk.get_movimento(1)
      self.assertAlmostEqual(32.03, self.a.base_damage(self.muk, atk, self.mew), 2)
   def testa_base_damage_spc(self):
      atk = self.mew.get_movimento(2)
      self.assertAlmostEqual(62.92, self.a.base_damage(self.mew, atk, self.muk), 2)


if __name__ == '__main__':
   uni.main(buffer=True)
