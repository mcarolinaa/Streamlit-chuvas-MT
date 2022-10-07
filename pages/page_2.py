import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# Importa dados
@st.cache  # This function will be cached
def read_df_rain(path):
    # slow
    df = pd.read_csv(path)
    return df

df_tenday = read_df_rain('./data/tenday_gdf.csv')
df_stall = read_df_rain('./data/st_all.csv')
df_sall = read_df_rain('./data/s_all.csv')

#
st.markdown("# Avaliação espaço-temporal de chuvas decendiais em início de safra em regiões do MT :rain_cloud:")
st.sidebar.markdown("# Resultados :rain_cloud:")


# Tabs
tab1, tab2, tab3 = st.tabs(["📈 Resultados", "📉 Resultados", "📊 Resultados"])


# Tab 1
tab1.subheader('Distribuição espaço-temporal e variabilidade de chuvas decendiais médias')
tab1.markdown('Na figura abaixo, observa-se a distribuição e evolução médias de acumulado de chuvas ao longo dos cenários de meses e decêndios avaliados nas mesorregiões NO e NE do estado do MT ao longo do período (1980 - 2015).')

def plot_distribuicao(df):

    fig = make_subplots(
                        rows=2, cols=3, shared_xaxes=True, shared_yaxes=True,
                        subplot_titles=(
                                        "Setembro - decêndio 1", "Setembro - decêndio 2",
                                        "Setembro - decêndio 3", "Outubro - decêndio 1",
                                        "Outubro - decêndio 2",  "Outubro - decêndio 3"),
                        x_title='Longitude', y_title='Latitude',
                        )

    sbs = df.query('month == 9 and decend == 1')
    fig.add_trace(go.Scatter(x=sbs['lon'], y=sbs['lat'],
    marker=dict(color=sbs['sum'],colorbar=dict(title="Chuva (mm)"), colorscale="YlGnBu", cmin=0, cmax=100),mode="markers"),
    row=1, col=1)

    sbs = df.query('month == 9 and decend == 2')
    fig.add_trace(go.Scatter(x=sbs['lon'], y=sbs['lat'],
    marker=dict(color=sbs['sum'], colorscale="YlGnBu", cmin=0, cmax=100),mode="markers"),
    row=1, col=2)

    sbs = df.query('month == 9 and decend == 3')
    fig.add_trace(go.Scatter(x=sbs['lon'], y=sbs['lat'],
    marker=dict(color=sbs['sum'], colorscale="YlGnBu", cmin=0, cmax=100),mode="markers"),
    row=1, col=3)

    sbs = df.query('month == 10 and decend == 1')
    fig.add_trace(go.Scatter(x=sbs['lon'], y=sbs['lat'],
    marker=dict(color=sbs['sum'], colorscale="YlGnBu", cmin=0, cmax=100),mode="markers"),
    row=2, col=1)

    sbs = df.query('month == 10 and decend == 2')
    fig.add_trace(go.Scatter(x=sbs['lon'], y=sbs['lat'],
    marker=dict(color=sbs['sum'], colorscale="YlGnBu",cmin=0, cmax=100),mode="markers"),
    row=2, col=2)

    sbs = df.query('month == 10 and decend == 3')
    fig.add_trace(go.Scatter(x=sbs['lon'], y=sbs['lat'],
    marker=dict(color=sbs['sum'], colorscale="YlGnBu", cmin=0, cmax=100),mode="markers"),
    row=2, col=3)

    fig.update_layout(showlegend=False,
    title_text='Distribuição de chuvas nos meses-decêndios')
    return fig

plotdistrib = plot_distribuicao(df_tenday)
tab1.plotly_chart(plotdistrib, use_container_width=True, showlegend=False)


# Tab 2
tab2.subheader('Variabilidade temporal de chuvas decendiais')

#

tab2.markdown('A seguir, observam-se as séries temporais da média do acumulado decendial de chuvas nos meses de Setembro e Outubro nas mesorregiões NO e NE do estado do MT ao longo do período (1980 - 2015).')
# tab2.image('./data/series_media.png')

def plot_serie_temporal(df):

    fig = make_subplots(
                        rows=2, cols=3, shared_xaxes=True, shared_yaxes=True,
                        subplot_titles=(
                                        "Setembro - decêndio 1", "Setembro - decêndio 2",
                                        "Setembro - decêndio 3", "Outubro - decêndio 1",
                                        "Outubro - decêndio 2",  "Outubro - decêndio 3"),
                        x_title='Ano', y_title='Chuva (mm)',)

    s1t = df.query('month == 9 and decend == 1')
    fig.add_trace(go.Scatter(x=s1t['year'], y=s1t['sum']), row=1, col=1)

    s1t = df.query('month == 9 and decend == 2')
    fig.add_trace(go.Scatter(x=s1t['year'], y=s1t['sum']), row=1, col=2)

    s1t = df.query('month == 9 and decend == 3')
    fig.add_trace(go.Scatter(x=s1t['year'], y=s1t['sum']), row=1, col=3)

    s1t = df.query('month == 10 and decend == 1')
    fig.add_trace(go.Scatter(x=s1t['year'], y=s1t['sum']), row=2, col=1)

    s1t = df.query('month == 10 and decend == 2')
    fig.add_trace(go.Scatter(x=s1t['year'], y=s1t['sum']), row=2, col=2)

    s1t = df.query('month == 10 and decend == 3')
    fig.add_trace(go.Scatter(x=s1t['year'], y=s1t['sum']), row=2, col=3)

    fig.update_layout(showlegend=False,
    title_text='Séries temporais de chuva acumulada nos meses-decêndios')
    return fig

plottemporal = plot_serie_temporal(df_stall)
tab2.plotly_chart(plottemporal, use_container_width=True)

#

tab2.markdown('O Índice de Anomalia Padronizado (IAP) foi determinado para as séries temporais de cada cenário.')
tab2.markdown('Observa-se a seguir a variação do índice (indicando anos secos ou úmidos, relativo a cada período) nos meses de Setembro e Outubro nas mesorregiões NO e NE do estado do MT ao longo do período (1980 - 2015).')
# tab2.image('./data/sia_bar_media.png')

# calculo do IAP

def calcula_iap(df):
    mu = np.mean(df['sum'])
    gamma = np.std(df['sum'])
    df['sai'] = (df['sum'] - mu) / gamma
    return df

sb1 = df_stall.query('month == 9 and decend == 1')
sb2 = df_stall.query('month == 9 and decend == 2')
sb3 = df_stall.query('month == 9 and decend == 3')
sb4 = df_stall.query('month == 10 and decend == 1')
sb5 = df_stall.query('month == 10 and decend == 2')
sb6 = df_stall.query('month == 10 and decend == 3')

calcula_iap(sb1)
calcula_iap(sb2)
calcula_iap(sb3)
calcula_iap(sb4)
calcula_iap(sb5)
calcula_iap(sb6)

def plot_iap():

    fig = make_subplots(
                        rows=2, cols=3, shared_xaxes=True, shared_yaxes=True,
                        subplot_titles=(
                                        "Setembro - decêndio 1", "Setembro - decêndio 2",
                                        "Setembro - decêndio 3", "Outubro - decêndio 1",
                                        "Outubro - decêndio 2",  "Outubro - decêndio 3"),
                        x_title='Ano', y_title='IAP',)

    sb1["color"] = np.where(sb1["sai"] < 0, 'red', 'green')
    fig.add_trace(go.Bar(x=sb1['year'], y=sb1['sai'], marker_color=sb1['color']), row=1, col=1)

    sb2["color"] = np.where(sb2["sai"] < 0, 'red', 'green')
    fig.add_trace(go.Bar(x=sb2['year'], y=sb2['sai'], marker_color=sb2['color']), row=1, col=2)

    sb3["color"] = np.where(sb3["sai"] < 0, 'red', 'green')
    fig.add_trace(go.Bar(x=sb3['year'], y=sb3['sai'], marker_color=sb3['color']), row=1, col=3)

    sb4["color"] = np.where(sb4["sai"] < 0, 'red', 'green')
    fig.add_trace(go.Bar(x=sb4['year'], y=sb4['sai'], marker_color=sb4['color']), row=2, col=1)

    sb5["color"] = np.where(sb5["sai"] < 0, 'red', 'green')
    fig.add_trace(go.Bar(x=sb5['year'], y=sb5['sai'], marker_color=sb5['color']), row=2, col=2)

    sb6["color"] = np.where(sb6["sai"] < 0, 'red', 'green')
    fig.add_trace(go.Bar(x=sb6['year'], y=sb6['sai'], marker_color=sb6['color']), row=2, col=3)

    fig.update_layout(barmode='stack', showlegend=False,
    title_text='Índice de Anomalia Padronizado de chuvas nos meses-decêndios')
    return fig

plotiap = plot_iap()
tab2.plotly_chart(plotiap, use_container_width=True)


#

tab2.markdown('Já a análise gráfica de tendência permite a avaliação visual sobre tendências de aumento ou diminuição das chuvas durante o período.')
tab2.markdown('Observa-se a seguir essa análise das séries temporais dos acumulados decendiais de chuva nos meses de Setembro e Outubro nas mesorregiões NO e NE do estado do MT ao longo do período (1980 - 2015).')
# tab2.image('./data/ita_temp.png')

# Divide séries em 2 partes e ordena
def ordena_series(df):

    df_1 = df.query('year < 1998')
    df_1 = df_1.sort_values(by=['sum'])
    df_2 = df.query('year >= 1998')
    df_2 = df_2.sort_values(by=['sum'])

    return df_1, df_2

sb1_1, sb1_2 = ordena_series(sb1)
sb2_1, sb2_2 = ordena_series(sb2)
sb3_1, sb3_2 = ordena_series(sb3)
sb4_1, sb4_2 = ordena_series(sb4)
sb5_1, sb5_2 = ordena_series(sb5)
sb6_1, sb6_2 = ordena_series(sb6)

def plot_ita():

    fig = make_subplots(
                        rows=2, cols=3,
                        subplot_titles=(
                                        "Setembro - decêndio 1", "Setembro - decêndio 2",
                                        "Setembro - decêndio 3", "Outubro - decêndio 1",
                                        "Outubro - decêndio 2",  "Outubro - decêndio 3"),
                        x_title='Primeira metade da série', y_title='Segunda metade da série',)

    fig.add_trace(go.Scatter(x=sb1_1['sum'], y=sb1_2['sum'],
    marker=dict(color='blue'),mode="markers"), row=1, col=1)
    fig.update_xaxes(range=[0, 35], row=1, col=1)
    fig.update_yaxes(range=[0, 35], row=1, col=1)
    fig.add_shape(type="line", layer='below', x0=0, y0=0, x1=35, y1=35, line=dict(color="Crimson", width=3, dash="dot"),row=1, col=1)

    fig.add_trace(go.Scatter(x=sb2_1['sum'], y=sb2_2['sum'],
    marker=dict(color='blue'),mode="markers"), row=1, col=2)
    fig.update_xaxes(range=[0, 60], row=1, col=2)
    fig.update_yaxes(range=[0, 60], row=1, col=2)
    fig.add_shape(type="line", layer='below', x0=0, y0=0, x1=60, y1=60, line=dict(color="Crimson", width=3, dash="dot"),row=1, col=2)

    fig.add_trace(go.Scatter(x=sb3_1['sum'], y=sb3_2['sum'],
    marker=dict(color='blue'),mode="markers"), row=1, col=3)
    fig.update_xaxes(range=[0, 70], row=1, col=3)
    fig.update_yaxes(range=[0, 70], row=1, col=3)
    fig.add_shape(type="line", layer='below', x0=0, y0=0, x1=70, y1=70, line=dict(color="Crimson", width=3, dash="dot"),row=1, col=3)

    fig.add_trace(go.Scatter(x=sb4_1['sum'], y=sb4_2['sum'],
    marker=dict(color='blue'),mode="markers"), row=2, col=1)
    fig.update_xaxes(range=[0, 70], row=2, col=1)
    fig.update_yaxes(range=[0, 70], row=2, col=1)
    fig.add_shape(type="line", layer='below', x0=0, y0=0, x1=70, y1=70, line=dict(color="Crimson", width=3, dash="dot"),row=2, col=1)

    fig.add_trace(go.Scatter(x=sb5_1['sum'], y=sb5_2['sum'],
    marker=dict(color='blue'),mode="markers"), row=2, col=2)
    fig.update_xaxes(range=[0, 100], row=2, col=2)
    fig.update_yaxes(range=[0, 100], row=2, col=2)
    fig.add_shape(type="line", layer='below', x0=0, y0=0, x1=100, y1=100, line=dict(color="Crimson", width=3, dash="dot"),row=2, col=2)

    fig.add_trace(go.Scatter(x=sb6_1['sum'], y=sb6_2['sum'],
    marker=dict(color='blue'),mode="markers"), row=2, col=3)
    fig.update_xaxes(range=[0, 120], row=2, col=3)
    fig.update_yaxes(range=[0, 120], row=2, col=3)
    fig.add_shape(type="line", layer='below', x0=0, y0=0, x1=120, y1=120, line=dict(color="Crimson", width=3, dash="dot"),row=2, col=3)

    fig.update_layout(showlegend=False,
                      title_text='Tendência na chuva acumulada nos meses-decêndios (temporal)')
    return fig

plotita = plot_ita()
tab2.plotly_chart(plotita, use_container_width=True)


#

tab2.markdown('Por fim, foi aplicada técnica de clusterização nas séries temporais.')
tab2.markdown('Isso permitiu avaliar como cada ano se classificou no contexto de cada cenário (mês-decêndio).')
tab2.markdown('Observa-se a seguir o resultado da clusterização das séries temporais para o valor médio acumulado decendial de chuvas nos meses de Setembro e Outubro nas mesorregiões NO e NE do estado do MT  ao longo do período (1980 - 2015)')
# tab2.image('./data/swarm_series_media.png')

def plot_clusters(df):

    fig = px.strip(df, y='decend', x='sum', color='hcl_ord', facet_col='month', stripmode='group',
                   labels={'decend': 'Decêndio', 'sum': 'Chuva (mm)',
                   'hcl_ord': 'Cluster', 'month': 'Mês'})
    fig.update_traces(marker_size=8)
    fig.update_layout(title='Clusters das séries temporais nos meses-decêndios')

    return fig

plotclustemp = plot_clusters(df_stall)
tab2.plotly_chart(plotclustemp, use_container_width=True)

# Tab 3

#
tab3.subheader('Variabilidade espaço-temporal de chuvas decendiais')

#

tab3.markdown('A mesma análise de tendência aplicada às séries temporais, foi aplicada também as **séries espaço-temporais**.')
tab3.markdown('Tal técnica permitiu a avaliação visual de quantidade superior de observações, facilitando a identificação de tendências.')
tab3.markdown('Observa-se a seguir a análise de tendência das séries espaço-temporais dos acumulados decendiais de chuva nos meses de Setembro e Outubro nas mesorregiões NO e NE do estado do MT ao longo do período (1980 - 2015).')
tab3.image('./data/ita_spatial_temp.png')

# sa1 = df_sall.query('month == 9 and decend == 1')
# sa2 = df_sall.query('month == 9 and decend == 2')
# sa3 = df_sall.query('month == 9 and decend == 3')
# sa4 = df_sall.query('month == 10 and decend == 1')
# sa5 = df_sall.query('month == 10 and decend == 2')
# sa6 = df_sall.query('month == 10 and decend == 3')

# sa_91_1, sa_91_2 = ordena_series(sa1)
# sa_92_1, sa_92_2 = ordena_series(sa2)
# sa_93_1, sa_93_2 = ordena_series(sa3)
# sa_101_1, sa_101_2 = ordena_series(sa4)
# sa_102_1, sa_102_2 = ordena_series(sa5)
# sa_103_1, sa_103_2 = ordena_series(sa6)


# def plot_ita2():

#     fig = make_subplots(
#                         rows=2, cols=3,
#                         subplot_titles=(
#                                         "Setembro - decêndio 1", "Setembro - decêndio 2",
#                                         "Setembro - decêndio 3", "Outubro - decêndio 1",
#                                         "Outubro - decêndio 2",  "Outubro - decêndio 3"),
#                         x_title='Primeira metade da série', y_title='Segunda metade da série',)

#     fig.add_trace(go.Scatter(x=sa_91_1['sum'], y=sa_91_2['sum'],
#     marker=dict(color='blue'),mode="markers"), row=1, col=1)
#     fig.update_xaxes(range=[0, 80], row=1, col=1)
#     fig.update_yaxes(range=[0, 80], row=1, col=1)
#     fig.add_shape(type="line", layer='below', x0=0, y0=0, x1=80, y1=80, line=dict(color="Crimson", width=3, dash="dot"),row=1, col=1)

#     fig.add_trace(go.Scatter(x=sa_92_1['sum'], y=sa_92_2['sum'],
#     marker=dict(color='blue'),mode="markers"), row=1, col=2)
#     fig.update_xaxes(range=[0, 140], row=1, col=2)
#     fig.update_yaxes(range=[0, 140], row=1, col=2)
#     fig.add_shape(type="line", layer='below', x0=0, y0=0, x1=140, y1=140, line=dict(color="Crimson", width=3, dash="dot"),row=1, col=2)

#     fig.add_trace(go.Scatter(x=sa_93_1['sum'], y=sa_93_2['sum'],
#     marker=dict(color='blue'),mode="markers"), row=1, col=3)
#     fig.update_xaxes(range=[0, 150], row=1, col=3)
#     fig.update_yaxes(range=[0, 150], row=1, col=3)
#     fig.add_shape(type="line", layer='below', x0=0, y0=0, x1=150, y1=150, line=dict(color="Crimson", width=3, dash="dot"),row=1, col=3)

#     fig.add_trace(go.Scatter(x=sa_101_1['sum'], y=sa_101_2['sum'],
#     marker=dict(color='blue'),mode="markers"), row=2, col=1)
#     fig.update_xaxes(range=[0, 250], row=2, col=1)
#     fig.update_yaxes(range=[0, 250], row=2, col=1)
#     fig.add_shape(type="line", layer='below', x0=0, y0=0, x1=250, y1=250, line=dict(color="Crimson", width=3, dash="dot"),row=2, col=1)

#     fig.add_trace(go.Scatter(x=sa_102_1['sum'], y=sa_102_2['sum'],
#     marker=dict(color='blue'),mode="markers"), row=2, col=2)
#     fig.update_xaxes(range=[0, 250], row=2, col=2)
#     fig.update_yaxes(range=[0, 250], row=2, col=2)
#     fig.add_shape(type="line", layer='below', x0=0, y0=0, x1=250, y1=250, line=dict(color="Crimson", width=3, dash="dot"),row=2, col=2)

#     fig.add_trace(go.Scatter(x=sa_103_1['sum'], y=sa_103_2['sum'],
#     marker=dict(color='blue'),mode="markers"), row=2, col=3)
#     fig.update_xaxes(range=[0, 250], row=2, col=3)
#     fig.update_yaxes(range=[0, 250], row=2, col=3)
#     fig.add_shape(type="line", layer='below', x0=0, y0=0, x1=250, y1=250, line=dict(color="Crimson", width=3, dash="dot"),row=2, col=3)

#     fig.update_layout(showlegend=False,
#                       title_text='Tendência na chuva acumulada nos meses-decêndios (espaço-temporal)')
#     return fig

# plotitas = plot_ita2()
# tab3.plotly_chart(plotitas, use_container_width=True)




#

tab3.markdown('E por fim, novamente as técnicas de clusterização foram aplicadas às séries espaço-temporais.')
tab3.markdown('Tal análise permitiu a observação da distribuição espacial do clusters mais frequente ao longo dos anos, bem como o entendimento da variabilidade entre os grupos formados.')
tab3.markdown('Observa-se a seguir a variabilidade e distribuição dos clusters das séries espaço-temporais do mês de **Setembro** nas mesorregiões NO e NE do estado do MT ao longo do período (1980 - 2015).')
tab3.image('./data/st_cluster_9.png')

#

tab3.markdown('Observa-se a seguir a variabilidade e distribuição dos clusters das séries espaço-temporais do mês de **Outubro** nas mesorregiões NO e NE do estado do MT ao longo do período (1980 - 2015).')
tab3.image('./data/st_cluster_10.png')

#
tab3.caption('Nessa seção, devido à quantidade e tamanho dos datasets utilizados, foi realizado upload de gráficos já prontos.')
