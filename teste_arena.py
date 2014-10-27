#!/usr/bin/python3
'''
|Contribuidores              | No. USP |
|----------------------------|---------|
|Christian M. T. Takagi      | 7136971 |
|Cinthia M Tanaka            | 5649479 |
|Daniel A. Nagata            | 7278048 |
|Fernando T. Tanaka          | 6920230 |

Disciplina: Laboratório de Programação II       
Prof. Alfredo Goldman
Exercicio Programa - Etapa 1                    
Arquivo: teste_arena.py
'''

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
            arq.write('Charizard\n50\n78\n84\n78\n100\n85\n9\n2\n2\n'
                      'Flamethrower\n9\n100\n95\n15\n'
                      'Psychic\n13\n100\n90\n10\n'
                      'Mew\n50\n100\n100\n100\n100\n100\n13\n\n4\n'
                      'Thunderbolt\n12\n100\n95\n15\n'
                      'Rock Slide\n5\n90\n75\n10\n'
                      'Earthquake\n4\n100\n100\n10\n'
                      'Bubblebeam\n10\n100\n65\n20\n')

      with open('in_arena', 'r') as sys.stdin:
         self.cha = pok.Pokemon()
         self.mew = pok.Pokemon()
      self.a = are.Arena()

   def tearDown(self):
      sys.stdin = sys.__stdin__


   # Testa o metodo base_damage()
   def testa_base_damage_atk(self):
      mov = self.mew.get_movimento(1)
      self.assertAlmostEqual(44.303, self.a.base_damage(self.mew, mov, self.cha), 2)
   def testa_base_damage_spc(self):
      mov = self.cha.get_movimento(0)
      self.assertAlmostEqual(37.53, self.a.base_damage(self.cha, mov, self.mew), 2)


   # Testa o metodo stab()
   def testa_stab_false(self):
      self.assertEqual(1.0,self.a.stab(self.mew, self.mew.get_movimento(0)))
   def testa_stab_true(self):
      self.assertEqual(1.5,self.a.stab(self.cha, self.cha.get_movimento(0)))


   #Testa o metodo type_effect()
   def testa_type_effect_nulo(self):
      mov = self.mew.get_movimento(2)
      self.assertEqual(0.0, self.a.type_effect(mov, self.cha))
   def testa_type_effect_res(self):
      mov = self.cha.get_movimento(1)
      self.assertEqual(0.5, self.a.type_effect(mov, self.mew))
   def testa_type_effect_neutro(self):
      mov = self.cha.get_movimento(0)
      self.assertEqual(1.0, self.a.type_effect(mov, self.mew))
   def testa_type_effect_res_super(self):
      self.cha.type2 = 15
      mov = self.mew.get_movimento(3)
      self.assertEqual(1.0, self.a.type_effect(mov, self.cha))
   def testa_type_effect_super(self):
      mov = self.mew.get_movimento(0)
      self.assertEqual(2.0, self.a.type_effect(mov, self.cha))
   def testa_type_effect_super_super(self):
      mov = self.mew.get_movimento(1)
      self.assertEqual(4.0, self.a.type_effect(mov, self.cha))


   # Testa o metodo critical()
   def testa_critical(self):
      chance = self.cha.get_spd() / 512
      sucesso = 0
      for i in range(0, 100000):
         if (self.a.critical(self.cha) != 1):
            sucesso += 1
      razao = sucesso / 100000
      self.assertAlmostEqual(chance, razao, 2)


   # Testa o metodo accuracy(self)
   def testa_accuracy(self):
      mov = self.mew.get_movimento(1)
      chance = mov.get_accu() / 100
      sucesso = 0
      for i in range(0, 100000):
         if (self.a.accuracy(mov) == True):
            sucesso += 1
      razao = sucesso / 100000
      self.assertAlmostEqual(chance, razao, 2)

   # Testa o metodo cria_info_turno(self)
   def testa_cria_info_turno(self):
      contador = 0
      for i in range(0, 10):
         s = ( '\n' +
               'Turno #' + str(contador) + '\n'
               '\n' +
               '                              +---\n' +
               '                              | Nome:' + self.cha.get_name () + '\n' +
               '                              | HP:' + str((self.cha.get_hp ()-i) / self.cha.get_hpmax ()  * 100) + '\n' +
               '                              +---\n' +
               '\n' +
               ' +---\n' +
               ' | Nome:' + self.mew.get_name () +'\n' +
               ' | HP:' + str(( self.mew.get_hp ()-i) / self.mew.get_hpmax ()  * 100) + '%' + '\n' +
               ' +---\n' +
               '\n' )
         self.cha.set_hp(self.cha.get_hp() - i)
         self.mew.set_hp(self.mew.get_hp() - i)
         print(s)
         self.assertEqual(s, self.a.cria_info_turno(self.mew, self.cha))
   
   # Testa o metodo turno()
   def turno_continua(self):
      with open('in_seq', 'w+') as sys.stdin:
         sys.stdin.write('0\n0\n')
         assertEqual(True, self.a.turno(self.cha, self.mew))
   def turno_fim_1(self):
      self.mew.set_hp(1)
      with open('in_seq', 'w+') as sys.stdin:
         sys.stdin.write('0\n0\n')
         assertEqual(False, self.a.turno(self.cha, self.mew))
   def turno_fim_2(self):
      self.cha.set_hp(1)
      with open('in_seq', 'w+') as sys.stdin:
         sys.stdin.write('0\n0\n')
         assertEqual(False, self.a.turno(self.cha, self.mew))

   # Testa o metodo realiza_ataque():
   def testa_realiza_ataque_struggle(self):
      ac_hp = self.cha.get_hp()
      am_hp = self.mew.get_hp()
      self.a.realiza_ataque(self.cha, 2, self.mew)
      # Verifica se o ataque struggle foi realizado com recoil
      self.assertGreater(ac_hp, self.cha.get_hp())
      self.assertGreater(am_hp, self.mew.get_hp())
      

if __name__ == '__main__':
   uni.main(buffer=True)
