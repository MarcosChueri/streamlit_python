

# importar as bibliotecas
import streamlit as st
import pandas as pd
from  datetime import timedelta

# criar as funções de carregamento de dados
  # cotações do ITAU - ITUB4 - 2010 a 2024
  
#@st.cache_data
#def carrega_dados(empresa):
#  dados_acao=yf.Ticker(empresa)
#  cotacoes_acao=dados_acao.history(period='1d', start='2010-01-01', end='2024-01-01')
#  cotacoes_acao=cotacoes_acao[['Close']]
#  return cotacoes_acao

@st.cache_data
def carrega_dados(caminho, colunas):
  df=pd.read_csv(caminho, sep=',')
  df=df[colunas]
  df['date_time'] = pd.to_datetime(df['date_time'], format='%Y-%m-%d %H:%M:%S')
  df=df.dropna()
  df.set_index('date_time', inplace=True)
  return df

colunas=['temp', 'traffic_volume', 'date_time']
dados=carrega_dados("C:\\Users\\marco\\Desktop\\Fluxograma\\bootcamps\\kaggle\\datasets\\Metro_Interstate_Traffic_Volume.csv", colunas)

# prepara as visualizações
st.sidebar.header('filtros')

# filtro colunas
lista_colunas = st.sidebar.multiselect('escolha', dados.columns)
if lista_colunas:
  dados=dados[lista_colunas]

# filtro datas
data_inicial=dados.index.min().to_pydatetime()
data_final=dados.index.max().to_pydatetime()
intervalo_data=st.sidebar.slider('Selecione o periodo', 
                                 min_value=data_inicial,
                                 max_value=data_final,
                                 value=(data_inicial, data_final),
                                 step=timedelta(days=1))

dados = dados.loc[intervalo_data[0]:intervalo_data[1]]

st.write("""
# App Volume de Carros
O gráfico abaixo representa a variação de volume de tráfico ao passar do tempo.
 ao longo dos anos""") # markdown

st.line_chart(dados)



st.write("""
# Fim do App""") # markdown

print(dados)
#print(dados.info())
