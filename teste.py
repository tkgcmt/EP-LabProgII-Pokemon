from  bibxml import xml_class
from cliente import Cliente
from pokemon import Pokemon
import arena as are
import sys


def main():
    
    a = Cliente()
    b = xml_class
    if sys.argv[1] == '-i':
        s = a.comeca_batalha( '127.0.0.1', '5000')
    if sys.argv[1] == '-a':
        s = a.posta_ataque( '127.0.0.1', '5000', sys.argv[2])

if __name__ == '__main__':
    main()
