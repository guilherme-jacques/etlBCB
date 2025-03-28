import requests
import pandas as pd #importa o pandas com pd
url= "https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trimestre=@trimestre)?@trimestre='20191'&$format=json"
req = requests.get(url)
print(req.status_code)


def requestApiBcb(data: str)-> pd.DataFrame:
    """
    Função para extrair os dados dos meios de pagamentos trimestrais do banco central.

    Parâmentros:
    data - string AAAAT (exemplo: 20191)

    Saída:
    DataFrame - Estrutura de dados pandas.


    """
    url = f"https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trimestre=@trimestre)?@trimestre='{data}'&$format=json"
    
    req = requests.get(url)
    dados = req.json()
    
    df= pd.json_normalize(dados['value'])
    df['datatrimestre'] = pd.to_datetime(df['datatrimestre'])
    return (df)


dadosBcb = requestApiBcb('20191')
print (dadosBcb.info())


