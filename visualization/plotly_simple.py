from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

print( __version__) # requires version >= 1.9.0


from plotly.graph_objs import Scatter, Figure, Layout, Data

trace0 = Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17],
    name="aaa"
)
trace1 = Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9],
    name="bbb"
)
data = Data([trace0, trace1])


init_notebook_mode(connected=True)


iplot(data)

# %%
# 多个子图subplot的例子见my_crypto_coin_data_test/binance_predict_v6.py
