import streamlit as st
import numpy as np
import pandas as pd
import geopandas as gpd


# @st.cache  # This function will be cached
def read_df_rain(path):
    # slow
    df = pd.read_csv(path)
    return df

df_nor = read_df_rain('/data/df_sdo.csv')

st.markdown("# Avaliação espaço-temporal de chuvas decendiais em início de safra em regiões do MT :rain_cloud:")
st.sidebar.markdown("# Introdução e Material e Métodos :rain_cloud:")

st.markdown("Esse estudo teve como objetivo a avaliação da variabilidade espacial e temporal de chuvas nos decêndios dos meses de Setembro e Outubro para identificar seus padrões e tendências nos meses de início de safra agrícola")

# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

# st.map(map_data)

tab1, tab2, tab3 = st.tabs(["🗺️ Local", "🗃 Dados", "💻 Metodologia "])

tab1.subheader('Locais de avaliação')
tab1.text('No presente estudo, as mesorregiões NO e NE do estado do Mato Grosso foram usadas para avaliação.')
tab1.image('/data/maps2.png')

tab2.subheader('Amostra dos dados em grade utilizados no estudo')
tab2.text("Obs: Foi utilizada base de dados históricos em grade com duração de 36 anos das mesorregiões Norte e Nordeste do estado do MT.")
tab2.text("Detalhes sobre os dados e metodologia empregada para construção da base de dados podem ser encontrados em Xavier et al. (2016).")
tab2.write(df_nor.head())
tab2.text("Xavier, A.C.; King, C.W.; Scanlon, B.R. 2016. Daily gridded meteorological variables in Brazil (1980–2013). International Journal of Climatology 36: 2644-2659.")

tab3.title('Metodologia de análise dos dados')

tab3.subheader('Distribuição espaço-temporal e variabilidade de chuvas decendiais médias')
tab3.text('Nessa etapa, os dados diários de chuva (1980 – 2015) foram agrupados de acordo com a variável espacial (pontos representativos da grade georreferenciada), mês e decêndio, e calculou-se a média do acumulado de chuvas decendiais')

tab3.subheader('Variabilidade temporal de chuvas decendiais')
tab3.text('Nessa etapa, realizou-se: (i) a construção de séries temporais de chuva acumulada nos decêndios, seguida de (ii) avaliação da variabilidade e tendência das séries e (iii) clusterização das séries temporais.')

tab3.text('A variabilidade e tendências foram avaliadas por meio do Coeficiente de variação (1); Índice de anomalia padronizado (2) e indicador de tendência (3)')
tab3.latex(r''' (1)
           CV = (\delta / \Chi md) * 100
           ''')
tab3.latex(r'''Em\,que: \delta: desvio\,padrão\,e\,\Chi md: média\,da\,série''')
tab3.latex(r''' (2)
           IAP = (x - \mu) / \delta
           ''')
tab3.latex(r'''Em\,que: x: total\,anual\,de\,determinado\,ano, \mu: média\,dos\,anos, \delta: desvio\,padrão\,dos\,anos''')
tab3.latex(r''' (3)
           S = (2 * (x2 - x1)) / n
           ''')
tab3.latex(r'''Em\,que: x1\,e\,x2\,são\,as\,médias\,da\,primeira\,e\,segunda\,metade\,das\,séries\,temporais\,(sub-séries),\,respectivamente,\,e\,n\,é\,o\,número\,de\,observações\,da\,série''')

tab3.subheader('Variabilidade espaço-temporal de chuvas decendiais')
tab3.text('Nessa etapa, buscou-se avaliar a variabilidade espaço-temporal da chuva decendial durante os meses de Setembro e Outubro usando aproximadamente 900 séries temporais.')
tab3.text('Essas séries referem-se aos cenários de mês-decêndio (2 x 3 = 6), 36 anos (1980 – 2015) e aproximadamente 900 pontos geolocalizados.')
tab3.text('As séries espaço-temporais foram avaliadas com relação às suas tendências, utilizando a mesma metodologia descrita na seção anterior')
tab3.text('Um total de 6 análises de clusterização (cenários mês-decêndio) foram feitas para que fosse possível avaliar as tendências decendiais de chuvas no espaço-tempo das regiões avaliadas.')
