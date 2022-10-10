import requests

class api_tse_tabela():
    def getGeral(estado):
        dicionario = requests.get(
'https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/'+\
'{}/'.format(estado)+\
'{}'.format(estado)+\
'-c0001-e000544-r.json'\
).json()
        dicionario.pop('cand',None)
        return dicionario

    def getPresidentes(estado):
        dicionario = requests.get(
'https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/'+\
'{}/'.format(estado)+\
'{}'.format(estado)+\
'-c0001-e000544-r.json'\
).json()
        return dicionario['cand']
    
    def getGovernadores(estado):
        dicionario = requests.get(
'https://resultados.tse.jus.br/oficial/ele2022/546/dados-simplificados/'+\
'{}/'.format(estado)+\
'{}'.format(estado)+\
'-c0003-e000546-r.json'\
).json()
        return dicionario['cand']

    def getSenadores(estado):
        dicionario = requests.get(
'https://resultados.tse.jus.br/oficial/ele2022/546/dados-simplificados/'+\
'{}/'.format(estado)+\
'{}'.format(estado)+\
'-c0005-e000546-r.json'\
).json()
        return dicionario['cand']

    def getDeputadosFederais(estado):
        dicionario = requests.get(
'https://resultados.tse.jus.br/oficial/ele2022/546/dados-simplificados/'+\
'{}/'.format(estado)+\
'{}'.format(estado)+\
'-c0006-e000546-r.json'\
).json()
        return dicionario['cand']

    def getDeputadosEstaduais(estado):
        dicionario = requests.get(
'https://resultados.tse.jus.br/oficial/ele2022/546/dados-simplificados/'+\
'{}/'.format(estado)+\
'{}'.format(estado)+\
'-c0007-e000546-r.json'\
).json()
        return dicionario['cand']
    
    def getDistrital():
        dicionario = requests.get(
'https://resultados.tse.jus.br/oficial/ele2022/548/dados-simplificados/pe/pe30015-c0025-e000548-r.json'
).json()
        return dicionario['cand']

if __name__ == '__main__':
    print(api_tse_tabela.getDistrital())