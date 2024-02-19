import streamlit as st

import plotly.express as px

from dataset import df

from utils import format_number

from graficos import (
    grafico_map_estado, grafico_rec_mensal, grafico_rec_estado,
    grafico_rec_categoria, grafico_rec_vendedores
    )


# * ================================================ deve ficar no inicio do codigo
st.set_page_config(layout='wide')
# ^ ================================================ deve ficar no inicio do codigo

st.title("Dashboard de Vendas :shopping_trolley:")

aba1, aba2, aba3 = st.tabs(['Dataset', 'Receita', 'Vendedores'])

with aba1:
    st.dataframe(df)

with aba2:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        # st.metric('Receita Total', df['Preço'].sum())
        st.metric('Receita Total', format_number(df['Preço'].sum(), 'R$ '))
        st.plotly_chart(grafico_map_estado, use_container_width=True)
        st.plotly_chart(grafico_rec_estado, use_container_width=True)

    with coluna2:
        # st.metric("Quantidade de Vendas", df.shape[0])
        st.metric("Quantidade de Vendas", format_number(df.shape[0]))
        st.plotly_chart(grafico_rec_mensal, use_container_width=True)
        st.plotly_chart(grafico_rec_categoria, use_container_width=True)

with aba3:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.plotly_chart(grafico_rec_vendedores)