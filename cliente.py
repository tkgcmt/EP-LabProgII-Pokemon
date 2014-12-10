from requests import post
from bibxml import xml_class
import pokemon as pok
import arena as ar

class Cliente():

    # Ao começar a batalha, o cliente envia ao servidor
    # um arquivo xml 'meuxml' contendo as informações referentes
    # ao usuário e recebe as informações referentes aos dois
    # jogadores
    def comeca_batalha(self, nomehost, porta, meuxml):
        endereco = "http://" + nomehost + ":" + porta + "/battle"
        pkmn_cli = pok.Pokemon()
        obj = xml_class()
        xml_pkmn_cli = obj.cliente_gera_xml(pkmn_cli)
        response = post(endereco, data=xml_pkmn_cli)
        return response.text

    # O cliente envia ao servidor o ataque que o usuário utilizará
    # passando como parâmetro o id do ataque. Ele recebe do 
    # servidor as informações atualizadas, após os ataques
    # serem contabilizados
    def posta_ataque(self, nomehost, porta, id_ataque):
        endereco = "http://" + nomehost + ":" + porta + "/battle/attack/" + str(id_ataque)
        battle_state = post(endereco)
        conteudo_xml = battle_state.text
        print("conteudo_xml: ",  conteudo_xml)
        with open("output.xml", 'w') as arq:
          arq.write(conteudo_xml)
        with open("output.xml", 'r') as arq:
          self.imprime_informacoes(arq)
        return battle_state

    # Imprime de maneira agradável os dados para acompanhar
    # a batalha entre os dois jogadores
    def imprime_informacoes(self,xmlfile):
        xmlObj = bibxml.xml_class()
        arvore = xmlObj.cria_arvore(xmlfile)
        xmlObj.imprime_basico(arvore)

def main():

    eu = Cliente()
    eu.comeca_batalha("localhost","5000",)
    #eu.posta_ataque("127.0.0.1","5000",1)

if __name__ == '__main__':
    main()       
