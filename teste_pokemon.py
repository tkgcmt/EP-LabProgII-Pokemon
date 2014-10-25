#!/usr/bin/python3

import pokemon as pok
import unittest as uni
import sys
import os

# Rotina para testar objetos do tipo Pokemon()
class TestadorPokemon(uni.TestCase):
   vez = True
   def setUp(self):
      if self.vez == True:
         if os.path.isfile('in_missingno') == False:
            arq = open('in_missingno', 'w+')
            arq.write('MissingNo\n-1\n101\n50\n-1\n256\n1\n-1\n256\n2\n'
                   '-1\n256\n3\n-1\n256\n4\n-1\n256\n5\n'
                   '-1\n17\n6\n-1\n17\n7\n0')
         with open('in_missingno', 'r') as arq:
            sys.stdin = arq
            self.missingno = pok.Pokemon()

         if os.path.isfile('in_mew') == False:
            arq = open('in_mew', 'w+')
            arq.write('Mew\n50\n175\n120\n120\n120\n120\n12\n15\n3\n'
                      'Pound\n0\n100\n40\n35\n'
                      'Mega Punch\n0\n85\n80\n10\n'
                      'Psychic\n12\n90\n100\n10\n')
         with open('in_mew', 'r') as arq:
            sys.stdin = arq
            self.mew = pok.Pokemon()

         self.vez = False

   # Testa se a leitura da entrada trata os valores extremos e tambem 
   # testa os getters.
   def testaEntrada(self):
      self.assertEqual('MissingNo', self.missingno.get_name())
      self.assertEqual(50, self.missingno.get_level())
      self.assertEqual(1, self.missingno.get_hpmax())
      self.assertEqual(1, self.missingno.get_hp())
      self.assertEqual(2, self.missingno.get_atk())
      self.assertEqual(3, self.missingno.get_def())
      self.assertEqual(4, self.missingno.get_spd())
      self.assertEqual(5, self.missingno.get_spc())
      self.assertEqual(6, self.missingno.get_type1())
      self.assertEqual(7, self.missingno.get_type2())
      self.assertEqual(0, self.missingno.get_numAtk())

   # Testa o metodo possui_ataques()
   def testa_possui_ataques(self):
      self.assertEqual(False, self.missingno.possui_ataques())
      self.assertEqual(True, self.mew.possui_ataques())
      for i in range(self.mew.numAtk):
         obj = self.mew.get_movimento(i)
         while(obj.get_pp() > 0):
            obj.reduz_pp()
      self.assertEqual(False, self.mew.possui_ataques())

   # Testa o metodo mostra_ataques():
   def testa_mostra_ataques(self):
      self.skipTest('Redirecionamento do stdout da erro')
      sys.stdout = open('out_temp', 'w+')
      # O redirecionamento do stdout da erro de atributo durante a escrita.
      self.mew.mostra_ataques()
      self.stdout = sys.__stdout__
      with open('moveSet', 'r') as leitura:
         lista = leitura.read()
      with open('out_temp', 'r') as leitura:
         temp = leitura.read()
      self.assertEqual(lista, temp)
   
   # Testa se o metodo esta_vivo() e o set_hp()
   def testa_esta_vivo(self):
      self.assertEqual(True, self.missingno.esta_vivo())
      self.missingno.set_hp(0)
      self.assertEqual(0, self.missingno.get_hp())
      self.assertEqual(False, self.missingno.esta_vivo())


if __name__ == '__main__':
   uni.main(verbosity=1, buffer=True)
