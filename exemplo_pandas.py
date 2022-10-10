import pandas as pd
from apy_tse import api_tse_tabela as api

## Exemplo para utilizar pandas na criação de dataframe com informações sobre a votação

print('DATAFRAME INFORMAÇÕES RELAÇÃO A VOTAÇÃO')
dataFrameInfoVotacao = pd.DataFrame([api.getGeral('es')])
print(dataFrameInfoVotacao)

print('DATAFRAME VOTAÇÃO PRESIDENTES')
dataFramePresidente = pd.DataFrame(api.getPresidentes('br'))
print(dataFramePresidente)

print('DATAFRAME VOTAÇÃO SENADORES')
dataFrameSenadores = pd.DataFrame(api.getSenadores('es'))
print(dataFrameSenadores)

print('DATAFRAME VOTAÇÃO DEPUTADO FEDERAL')
dataFrameDeputadoFederal = pd.DataFrame(api.getDeputadosFederais('es'))
print(dataFrameDeputadoFederal)

print('DATAFRAME VOTAÇÃO DEPUTADO ESTADUAL')
dataFrameDeputadoEstadual = pd.DataFrame(api.getDeputadosEstaduais('es'))
print(dataFrameDeputadoEstadual)

print('DATAFRAME VOTAÇÃO DISTRITAL DE "PE" ')
dataFrameDistritalPe = pd.DataFrame(api.getDistrital())
print(dataFrameDistritalPe)
