from requests import post
from bibxml import xml_class
import pokemon as pok
import arena as ar


obj = xml_class()

class Cliente():

    # Ao começar a batalha, o cliente envia ao servidor
    # um arquivo xml 'meuxml' contendo as informações referentes
    # ao usuário e recebe as informações referentes aos dois
    # jogadores
    def comeca_batalha(self, nomehost, porta):
        endereco = "http://" + nomehost + ":" + porta + "/battle"
        pkmn_cli = pok.Pokemon()
        xml_pkmn_cli = obj.cliente_gera_xml(pkmn_cli)
        battle_state = post(endereco, data=xml_pkmn_cli)
        return battle_state.text

    # O cliente envia ao servidor o ataque que o usuário utilizará
    # passando como parâmetro o id do ataque. Ele recebe do 
    # servidor as informações atualizadas, após os ataques
    # serem contabilizados
    def posta_ataque(self, nomehost, porta, id_ataque):
        endereco = "http://" + nomehost + ":" + porta + "/battle/attack/" + str(id_ataque)
        battle_state = post(endereco)
        return battle_state.text
        

    # Imprime de maneira agradável os dados para acompanhar
    # a batalha entre os dois jogadores
    def imprime_informacoes(self, xmlfile):
        arvore = obj.cria_arvore(xmlfile)
        obj.imprime_basico(arvore)

def main():

    eu = Cliente()
    eu.comeca_batalha("localhost","5000",)
    #eu.posta_ataque("127.0.0.1","5000",1)

if __name__ == '__main__':
    main()       
