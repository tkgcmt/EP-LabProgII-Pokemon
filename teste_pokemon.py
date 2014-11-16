#!/usr/bin/python3
# |Contribuidores              | No. USP |
# |----------------------------|---------|
# |Christian M. T. Takagi      | 7136971 |
# |Cinthia M Tanaka            | 5649479 |
# |Daniel A. Nagata            | 7278048 |
# |Fernando T. Tanaka          | 6920230 |
# ------------------------------------------------------------------------------
# Disciplina: Laboratório de Programação II       
# Prof. Alfredo Goldman
# Exercicio Programa - Etapa 2                    
# Arquivo: teste_pokemon.py
# ------------------------------------------------------------------------------

import pokemon as pok
import unittest as uni
import sys
import os

# Rotina para testar objetos do tipo Pokemon()
class TestadorPokemon(uni.TestCase):
   def setUp(self):
      if os.path.isfile('in_missingno') == False:
         arq = open('in_missingno', 'w+')
         arq.write('MissingNo\n-1\n101\n51\n-1\n256\n1\n-1\n256\n2\n'
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

   def tearDown(self):
      sys.stdin = sys.__stdin__

   # Testa se a leitura da entrada trata os valores extremos e tambem 
   # testa os getters.
   def testa_get_name(self):
      self.assertEqual(self.missingno.name, self.missingno.get_name())
   def testa_get_lvl(self):
      self.assertEqual(self.missingno.lvl, self.missingno.get_lvl())
   def testa_get_hpmax(self):
      self.assertEqual(self.missingno.hpmax, self.missingno.get_hpmax())
   def testa_get_hp(self):
      self.assertEqual(self.missingno.hp, self.missingno.get_hp())
   def testa_get_atk(self):
      self.assertEqual(self.missingno.atk, self.missingno.get_atk())
   def testa_get_defe(self):
      self.assertEqual(self.missingno.defe, self.missingno.get_defe())
   def testa_get_spd(self):
      self.assertEqual(self.missingno.spd, self.missingno.get_spd())
   def testa_get_spc(self):
      self.assertEqual(self.missingno.spc, self.missingno.get_spc())
   def testa_get_type1(self):
      self.assertEqual(self.missingno.type1, self.missingno.get_type1())
   def testa_get_type2(self):
      self.assertEqual(self.missingno.type2, self.missingno.get_type2())
   def testa_get_numAtk(self):
      self.assertEqual(self.missingno.numAtk, self.missingno.get_numAtk())

   # Testa o metodo possui_ataques()
   def testa_possui_ataques_nulo(self):
      self.assertEqual(False, self.missingno.possui_ataques())
   def testa_possui_ataques_tem(self):
      self.assertEqual(True, self.mew.possui_ataques())
   def testa_possui_ataques_nao_tem(self):
      for i in range(self.mew.numAtk):
         obj = self.mew.get_movimento(i)
         while(obj.get_pp() > 0):
            obj.reduz_pp()
      self.assertEqual(False, self.mew.possui_ataques())

   # Testa o metodo mostra_ataques():
   def testa_mostra_ataque_normal(self):
      lista = ['  0 - Pound  PP:( 35 / 35 )',
               '  1 - Mega Punch  PP:( 10 / 10 )',
               '  2 - Psychic  PP:( 10 / 10 )']
      for i in range(self.mew.numAtk):
         linha = self.mew.mostra_ataque(i)
         self.assertEqual(lista[i], linha)
   
   # Testa se o metodo esta_vivo()
   def testa_esta_vivo_pos(self):
      self.assertEqual(True, self.missingno.esta_vivo())
      self.missingno.set_hp(0)
      self.assertEqual(False, self.missingno.esta_vivo())

if __name__ == '__main__':
   uni.main( buffer=True)
