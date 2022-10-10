# Modulo API TSE
## Objetivo

Facilitar o uso da API do TSE(Tribunal Superior Eleitoral).

- Fácil utilização
- Funções divididas por meio de metétodos
- ✨Tudo isso feito para facilitar a  analise dos dados✨

## Começar a utilização
O modulo necessita da bibliotéca `requests`.
```sh
pip install requests
```
Importação do modulo .
```python
from api_tse import api_tse_tabela as api
```
- Agora podemos chamar nosso modulo escrevendo `api`.

Exemplo para conseguir receber dados sobre a votação no brasil
```python
print(api.getGeral('br'))
```
O resultado será um dicionário  com as informações .

## Métodos disponíveis

### getGeral( string )
```python
dicionárioInformaçõesGeraisEs = api.getGeral('es')
print(dicionárioInformaçõesGeraisEs)

dicionárioInformaçõesGeraisBr = api.getGeral('br')
print(dicionárioInformaçõesGeraisBr )
```
- Coloque a sigla do Estado desejado para obter a informação sobre aquele Estado.
- A sigla `'br'` para receber dados sobre a votação de presidente do Brasil.
- Retorna um dicionário com as informações.

###   api.getPresidentes( string )
```python
dicionárioInformaçõesPresidenteBr = api.getPresidentes('br')
print(dicionárioInformaçõesPresidenteBr)

dicionárioInformaçõesPresidenteMs = api.getPresidentes('ms')
print(dicionárioInformaçõesPresidenteMs)
```
- Recebe as informações dos candidatos.
- Coloque a sigla do Estado desejado para obter a informação sobre aquele Estado.
- A sigla `'br'` para receber dados sobre a votação de presidente do Brasil.
- Retorna uma lista de dicionário dos candidatos.

###   api.getSenadores( string )
```python
dicionárioInformaçõesSenadoresMs = api.getSenadores('ms')
print(dicionárioInformaçõesSenadoresMs)
```
- Recebe as informações dos candidatos.
- Coloque a sigla do Estado desejado para obter a informação sobre aquele Estado.
- Retorna uma lista de dicionário dos candidatos.

###   api.getDeputadosFederais( string )
```python
dicionárioInformaçõesDeputadosFederaisMs = api.getDeputadosFederais('ms')
print(dicionárioInformaçõesDeputadosFederaisMs)
```
- Recebe as informações dos candidatos.
- Coloque a sigla do Estado desejado para obter a informação sobre aquele Estado.
- Retorna uma lista de dicionário dos candidatos.

###   api.getDeputadosEstaduais( string )
```python
dicionárioInformaçõesDeputadosEstaduaisMs = api.getDeputadosEstaduais('ms')
print(dicionárioInformaçõesDeputadosEstaduaisMs)
```
- Recebe as informações dos candidatos.
- Coloque a sigla do Estado desejado para obter a informação sobre aquele Estado.
- Retorna uma lista de dicionário dos candidatos.

###   api.getDistrital()
```python
dicionárioInformaçõesVotoDistrital = api.getDistrital()
print(dicionárioInformaçõesVotoDistrital)
```
- Recebe as informações dos candidatos.
- Coloque a sigla do Estado desejado para obter a informação sobre aquele Estado.
- Retorna uma lista de dicionário dos candidatos.
`Apenas o Pernanbuco disponível`



## Exemplos 

### Pandas
O exemplo necessita da bibliotéca `pandas`.
```sh
pip install pandas
```
##### Arvquivo: `exemplo_pandas.py`
### importação
```python
import pandas as pd
from apy_tse import api_tse_tabela as api
```
### Criação do DataFrame por meio da bibliotéca `pandas`

```python
dataFrameInfoVotacao = pd.DataFrame([api.getGeral('es')])
```
- Como o getgeral retorna apenas 1 dicionário, por tanto é necessário passar ele como lista.

```python
dataFramePresidente = pd.DataFrame(api.getPresidentes('br'))
```
- Como o os outros métodos retorna uma lista de dicionário então só passamos o método.




