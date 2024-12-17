import pandas as pd
import plotnine as p9
dados = pd.read_json('https://apisidra.ibge.gov.br/values/t/1737/n1/all/v/2265/p/all/d/v2265%202')

dados_ipca = dados.rename(columns={'V':'ipca','D3C':'data'}) \
                .query('ipca not in ["Valor", "..."]') \
                .assign(
                data=lambda x: pd.to_datetime(x.data, format="%Y%m"),
                ipca=lambda x: x.ipca.astype(float)
                )[['data', 'ipca']].query("data >= @pd.to_datetime('2004-01-01')")

print(dados_ipca.tail(2))
p9.ggplot(dados_ipca)+\
p9.aes(x='data', y='ipca')+\
p9.geom_line()    
dados_ipca.sort_values('ipca')
dados_ipca.query("ipca == ipca.max()")
dados_ipca.query("ipca == ipca.min()")
dados_ipca.ipca.describe()