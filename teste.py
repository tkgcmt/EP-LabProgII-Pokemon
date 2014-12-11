from  bibxml import xml_class
from cliente import Cliente
from pokemon import Pokemon
import arena as are


def main():
    
    a = Cliente()
    b = xml_class
    s = a.comeca_batalha( '127.0.0.1', '5000')
    with open ("muk.xml",'w+') as f:
        f.write(s)
    print("\n\n@@@@@@@@@@@@@@@@@@@@@\n\n")
    s = a.posta_ataque( '127.0.0.1', '5000', 1)

if __name__ == '__main__':
    main()
