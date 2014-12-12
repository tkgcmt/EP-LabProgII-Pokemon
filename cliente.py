from requests import post
from bibxml import xml_class
from pokemon import Pokemon
from arena import Arena
import sys

parser = xml_class()
are = Arena()

# Usamos uma divertida convencao de nomes aqui: RED = servidor, BLUE = cliente
BLUE = None


# Recebe um endereco de um servidor e envia (via HTTP POST) as informacoes de 
# um pokemon em formato xml a ele. 
def comeca_batalha(nomehost):
    global BLUE
    endereco = "http://" + nomehost + "/battle"
    # Verifica o modo de entrada, se manual ou por arquivo.
    if sys.argv[3] == '--auto':
        if pokemon_por_arquivo(sys.argv[4]):
            pass
    else:
        BLUE = Pokemon()
    xml_BLUE = parser.cliente_gera_xml(BLUE)
    response = post(endereco, data=xml_BLUE)
    battle_state = response.text
    if parser.valida(battle_state):
       imprime_informacoes(battle_state)
    else:
        if response.status_code != 200:
            print("Algo deu errado. HTTP CODE: ", response.status_code)
            sys.exit(1)
        print("A resposta do servidor nao e valida: \n", battle_state)
        sys.exit(1)
    return True


# Recebe um endereco de um servidor e um indice do ataque a ser usado. 
def posta_ataque(nomehost, id_ataque):
    global BLUE
    endereco = "http://" + nomehost + "/battle/attack/" + str(id_ataque)
    response = post(endereco)
    battle_state = response.text
    if parser.valida(battle_state):
       imprime_informacoes(battle_state)
    else:
        if response.status_code != 200:
            if response.status_code == 205:
                print("A batalha acabou. Resposta do servidor:\n", battle_state)
                sys.exit(0)
            else:
                print("Algo deu errado. HTTP CODE: ", response.status_code)
                sys.exit(1)

        print("A resposta do servidor nao e valida: \n", battle_state)
        sys.exit(1)
    parser.atualiza_poke_xml(battle_state, BLUE)
    return True




# Imprime de maneira agradável os dados para acompanhar
# a batalha entre os dois jogadores
def imprime_informacoes(xmlfile):
    arvore = parser.cria_arvore(xmlfile)
    parser.imprime_basico(arvore)


# Escolhe qual ataque o servidor ira usar
def escolhe_ataque(pkmnS):
    return are.escolhe_ataques(pkmnS)


# Cria o pokemon do cliente usando entradas de um arquivo.
def pokemon_por_arquivo(input_file):
    global BLUE
    try:
        # Redireciona sys.stdin
        with open(input_file, 'r') as sys.stdin:
            BLUE = Pokemon()
        # Restaura sys.stdin
        sys.stdin = sys.__stdin__
        return True
    except: 
        print("Arquivo nao existente. Iniciando em modo de entrada manual.")
        return False


def main():
    comeca_batalha(sys.argv[2])
    while(1):
        mov = escolhe_ataque(BLUE)
        posta_ataque(sys.argv[2], mov)
