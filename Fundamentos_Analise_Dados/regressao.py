import pandas as pd 
import statsmodels.formula.api as smf
import plotly.express as px 

dados=pd.read_csv('/home/eco/Downloads/FAD14-2/FAD14/dados/dados.csv')
modelo=smf.ols('y ~tempo',data=dados).fit()
modelo.params
ajuste=modelo.fittedvalues
dados['tendencia']=ajuste
dados["data"]=pd.PeriodIndex(data=dados["data"].str.replace(" ","-"),freq="Q").to_timestamp()
g1=px.line(
    data_frame=dados,
    y="y",
    x="data",
    title='PIB in BRAZIL',
    color=px.Constant('PIB'),
    color_discrete_sequence=['#282f6b'],
    labels=dict(data="",y="Indice",color=""))
g1.add_annotation(text="Price in Market",
    y=1.1,
    x=-0.11,
    yref='paper',
    xref='paper',
    showarrow=False)
g1.add_annotation(
    showarrow=False,
    text="Data: IBGE",
    x=1,
    xref='paper',
    yref='paper',
    y=-0.18)
g1.add_scatter(x=dados['data'],
    y=dados['tendencia'],
    name='Tendencia Linear',
    line=dict(color='#b22200')
    
)
g1.show()
    

