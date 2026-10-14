# Titulo -  Sistema de vendas
# Seção Cadastrar Vendas
    # Campo Data
    # Campo vendedor - Ana, Bruno, Carla
    # Campo Produto - Notebook, Fone , Celular
    # Campo Quantidade
    # Campo Valor
    # Botão Cadastrar Venda
        # Quando eu clicar no botão -> Adicionar a venda na tabela
    
# Seção Vendas Cadastradas
    # Tabela com as vendas
    
# Seção Dashboard
    # Card/Métrica -> Faturamento Total
    # Gráfico de Barra/Coluna -> Venda por vendedor
    # Gráfico de Pizza -> Venda por produto


import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar a base de vendas
tabela_vendas = pd.read_csv("vendas.csv")

st.write("# Sistema de Vendas")

# Seção de cadastro de vendas
st.sidebar.write("## Cadastrar Vendas")

data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("Vendedor", ["Bruno", "Ana", "Carla"])
produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"])
quantidade = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("Valor")
botao_cadastrar = st.sidebar.button("Cadatrar Venda")

# Logica de cadastro
if botao_cadastrar:
    nova_venda = [str(data), vendedor, produto, quantidade, valor]
    ultima_linha = len(tabela_vendas) # 124 linhas
    tabela_vendas.loc[ultima_linha] = nova_venda
    tabela_vendas.to_csv("vendas.csv", index=False)
    st.success("Venda cadastrada!")

# Seção de visualizar as vendas
st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas)


# Seção de Dashboard
st.write("## Dashboard")

# Card/Métrica -> Faturamento Total
# Somando toda a coluna de valor da base de dados
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento Total", f"R$ {faturamento}")


# Gráfico de Barra/Coluna -> Venda por vendedor
    # Colocando as cores de acordo com a coluna PRODUTO
grafico1 = px.bar(tabela_vendas, x="vendedor" , y="valor", color="produto")
st.plotly_chart(grafico1)

# Gráfico de Pizza -> Venda por produto
grafico2 = px.pie(tabela_vendas, names="produto", values="valor")
st.plotly_chart(grafico2)
