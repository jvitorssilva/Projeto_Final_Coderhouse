import pandas as pd
import requests
from plyer import notification
import datetime

#Criar a função de alerta de erro
def alerta():
    data_atual = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    notification.notify(
        title= f"Erro {response.status_code}",
        message="Ocorreu uma falha no carregamentos dos dados da API" + "\nData atual: " + data_atual,
        app_name="Alerta",
        timeout=10)
    
    #Consultar a API e gerar um dataframe com os feriados nacionais
ano = 2023
url_feriados =f"https://brasilapi.com.br/api/feriados/v1/{ano}"
response = requests.get(url_feriados)
if response.status_code == 200:
    data_json = response.json()
    feriados_nacionais = pd.DataFrame(data_json)
  
else:
    alerta()
#Alterar os nomes das colunas
feriados_nacionais = feriados_nacionais.rename(columns ={'date': 'Data', 'name': 'Feriado', 'type': 'Tipo'})
#Alterar o formato da data
feriados_nacionais['Data'] = pd.to_datetime(feriados_nacionais['Data']).dt.strftime('%d/%m/%Y')
#Deixar a coluna "Tipo" em português
feriados_nacionais['Tipo'] = feriados_nacionais['Tipo'].replace('national', 'Nacional')
#Consultar se existem valores nulos
feriados_nacionais.isna()
feriados_nacionais

# Consultar a API e gerar um dataframe com as corretoras ativas no Brasil
url_corretoras ="https://brasilapi.com.br/api/cvm/corretoras/v1"
response = requests.get(url_corretoras)
if response.status_code == 200:
    data_json2 = response.json()
    corretoras = pd.DataFrame(data_json2)
else:
    alerta()
#Limpar o dataframe deixando apenas as colunas com os dados de contato
corretoras_ativas = corretoras.loc[corretoras['status'] == 'EM FUNCIONAMENTO NORMAL']
dados = ['nome_social', 'email', 'municipio', 'telefone']
corretoras_ativas = corretoras_ativas[dados]
#Alterar nomes das colunas
corretoras_ativas = corretoras_ativas.rename(columns ={'nome_social': 'Nome', 'email': 'E-mail', 'municipio': 'Município', 'telefone': 'Telefone'})
#Formatar a coluna 'Telefone' no formato 'xxxx-xxxx' para melhor visualização
corretoras_ativas['Telefone'] = corretoras_ativas['Telefone'].astype(str).str[:4] + '-' + corretoras_ativas['Telefone'].astype(str).str[4:]
#Capitalizar a primeira letra de cada palavra na coluna 'Município'
corretoras_ativas['Município'] = corretoras_ativas['Município'].str.title()
#Consultar se existem valores nulos
corretoras_ativas.isna()
corretoras_ativas

#Consultar a API e gerar um dataframe com as taxas de juros vigentes no Brasil
url_taxas ="https://brasilapi.com.br/api/taxas/v1"
response = requests.get(url_taxas)
if response.status_code == 200:
    data_json3 = response.json()
    taxas = pd.DataFrame(data_json3)
else:
    alerta()

#Alterar nomes das colunas
taxas = taxas.rename(columns= {'nome': 'Nome', 'valor': 'Valor (%)'})
#Consultar se existem valores nulos
taxas.isna()
taxas

from sqlalchemy import create_engine

# Criar database
engine = create_engine('sqlite:///coderhouse.db')

# Importar dataframes para o database
feriados_nacionais.to_sql('feriados_nacionais', con=engine, if_exists='replace', index=False)
corretoras_ativas.to_sql('corretoras_ativas', con=engine, if_exists='replace', index=False)
taxas.to_sql('taxas', con=engine, if_exists='replace', index=False)