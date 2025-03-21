import requests
import pandas as pd #importa o pandas com pd
url= "https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trimestre=@trimestre)?@trimestre='20191'&$format=json"
req = requests.get(url)
print(req.status_code)


def requestApiBcb(data):
    """
    Função para extrair os dados dos meios de pagamentos trimestrais do banco central.

    Parâmentros:
    data - string aaaat (exemplo: 20191)

    """
    url = f"https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trimestre=@trimestre)?@trimestre='{data}'&$format=json"
    
    req = requests.get(url)
    dados = req.json()
    
    df= pd.json_normalize(dados['value'])
    return print (df)


requestApiBcb(20241)

