import streamlit as st

st.markdown("# Avaliação espaço-temporal de chuvas decendiais em início de safra em regiões do MT :rain_cloud:")
st.sidebar.markdown("# Resultados :rain_cloud:")

# x = st.slider('x')  #this is a widget
# st.write(x, 'squared is', x * x)

tab1, tab2, tab3 = st.tabs(["📈 Resultados", "📉 Resultados", "📊 Resultados"])

tab1.subheader('Distribuição espaço-temporal e variabilidade de chuvas decendiais médias')
tab1.text('Na figura abaixo, observa-se a distribuição e evolução médias de acumulado de chuvas ao longo dos cenários de meses e decêndios avaliados.')
tab1.image('./data/maps_rain_avg.png')

tab2.subheader('Variabilidade temporal de chuvas decendiais')

tab2.text('Séries temporais da média do acumulado decendial de chuvas nos meses de Setembro e Outubro nas mesorregiões NO e NE do estado do MT:')
tab2.image('./data/series_media.png')

tab2.text('Índice de anomalia padronizado dos acumulados decendiais de chuva nos meses de Setembro e Outubro nas mesorregiões NO e NE do estado do MT:')
tab2.image('./data/sia_bar_media.png')

tab2.text('Análise de tendência das séries temporais dos acumulados decendiais de chuva nos meses de Setembro e Outubro nas mesorregiões NO e NE do estado do MT:')
tab2.image('./data/ita_temp.png')

tab2.text('Clusterização das séries temporais da média do acumulado decendial de chuvas nos meses de Setembro e Outubro nas mesorregiões NO e NE do estado do MT:')
tab2.image('./data/swarm_series_media.png')

tab3.subheader('Variabilidade espaço-temporal de chuvas decendiais')

tab3.text('Análise de tendência das séries espaço-temporais dos acumulados decendiais de chuva nos meses de Setembro e Outubro nas mesorregiões NO e NE do estado do MT:')
tab3.image('./data/ita_spatial_temp.png')

tab3.text('Variabilidade e espacialização dos clusters das séries espaço-temporais mês de Setembro nas mesorregiões NO e NE do estado do MT:')
tab3.image('./data/st_cluster_9.png')

tab3.text('Variabilidade e espacialização dos clusters das séries espaço-temporais mês de Outubro nas mesorregiões NO e NE do estado do MT:')
tab3.image('./data/st_cluster_10.png')