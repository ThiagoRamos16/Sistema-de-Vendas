from datetime import datetime
from pathlib import Path
from shutil import copy2

import pandas as pd
import plotly.express as px
import streamlit as st

CAMINHO_CSV = Path(__file__).with_name("vendas.csv")
COLUNAS = ["data", "vendedor", "produto", "quantidade", "valor"]
PRECOS = {"Notebook": 3500.0, "Celular": 2000.0, "Fone": 150.0}
VENDEDORES = ["Ana", "Bruno", "Carla"]

st.set_page_config(page_title="Sistema de Vendas", layout="wide")


def moeda(valor: float) -> str:
    return f"R$ {valor:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")


def carregar_vendas() -> pd.DataFrame:
    if not CAMINHO_CSV.exists():
        return pd.DataFrame(columns=COLUNAS)
    dados = pd.read_csv(CAMINHO_CSV)
    faltantes = set(COLUNAS) - set(dados.columns)
    if faltantes:
        st.error(f"CSV incompatível. Colunas ausentes: {', '.join(sorted(faltantes))}")
        st.stop()
    dados = dados[COLUNAS].copy()
    dados["quantidade"] = pd.to_numeric(dados["quantidade"], errors="coerce")
    dados["valor"] = pd.to_numeric(dados["valor"], errors="coerce")
    return dados


def salvar_vendas(dados: pd.DataFrame, criar_backup: bool = False) -> None:
    if criar_backup and CAMINHO_CSV.exists():
        pasta_backup = CAMINHO_CSV.parent / "backups"
        pasta_backup.mkdir(exist_ok=True)
        copia = pasta_backup / f"vendas_{datetime.now():%Y%m%d_%H%M%S_%f}.csv"
        copy2(CAMINHO_CSV, copia)
    dados[COLUNAS].to_csv(CAMINHO_CSV, index=False)


vendas = carregar_vendas()
st.title("Sistema de Vendas")
st.caption("Aplicação demonstrativa com dados fictícios; valores originais preservados.")

st.sidebar.header("Cadastrar venda")
data = st.sidebar.date_input("Data da venda")
vendedor = st.sidebar.selectbox("Vendedor", VENDEDORES)
produto = st.sidebar.selectbox("Produto", list(PRECOS))
quantidade = st.sidebar.number_input("Quantidade", min_value=1, value=1, step=1)
desconto = st.sidebar.number_input("Desconto (%)", min_value=0.0, max_value=99.0, value=0.0, step=1.0)

preco_unitario = PRECOS[produto]
valor_bruto = preco_unitario * int(quantidade)
valor_desconto = valor_bruto * desconto / 100
valor_final = round(valor_bruto - valor_desconto, 2)
st.sidebar.write(f"Preço unitário: **{moeda(preco_unitario)}**")
st.sidebar.write(f"Subtotal: **{moeda(valor_bruto)}**")
st.sidebar.write(f"Desconto: **-{moeda(valor_desconto)}**")
st.sidebar.success(f"Total da venda: {moeda(valor_final)}")

if st.sidebar.button("Cadastrar venda", type="primary"):
    novo_registro = pd.DataFrame([{
        "data": data.isoformat(),
        "vendedor": vendedor,
        "produto": produto,
        "quantidade": int(quantidade),
        "valor": valor_final,
    }])
    vendas = pd.concat([vendas, novo_registro], ignore_index=True)
    salvar_vendas(vendas)
    st.success("Venda cadastrada com sucesso!")
    st.rerun()

st.subheader("Vendas cadastradas")
st.dataframe(vendas, use_container_width=True, hide_index=True)

with st.expander("Excluir registro de venda"):
    if vendas.empty:
        st.info("Não há registros para excluir.")
    else:
        
        posicoes = list(range(len(vendas)))
        def descrever(indice: int) -> str:
            linha = vendas.iloc[indice]
            return (
                f"Linha {indice + 1} — {linha['data']} | {linha['vendedor']} | "
                f"{linha['produto']} | {linha['quantidade']} unidade(s) | {moeda(float(linha['valor']))}"
            )

        with st.form("formulario_exclusao"):
            indice = st.selectbox("Escolha a venda", posicoes, format_func=descrever)
            st.write("Confira os dados antes de confirmar:")
            st.dataframe(vendas.iloc[[indice]], use_container_width=True, hide_index=True)
            confirmar = st.checkbox("Confirmo a exclusão deste registro")
            excluir = st.form_submit_button("Excluir venda")
        if excluir:
            if not confirmar:
                st.error("Marque a caixa de confirmação antes de excluir.")
            else:
                atual = carregar_vendas()
            
                if not atual.equals(vendas):
                    st.error("A base mudou desde que a página foi aberta. Recarregue e tente novamente.")
                else:
                    atual = atual.drop(index=indice).reset_index(drop=True)
                    salvar_vendas(atual, criar_backup=True)
                    st.success("Registro excluído. Backup criado na pasta backups.")
                    st.rerun()

st.subheader("Exportar dados")
st.download_button(
    "Baixar vendas.csv para Power BI",
    data=vendas[COLUNAS].to_csv(index=False).encode("utf-8-sig"),
    file_name="vendas.csv",
    mime="text/csv",
)

st.subheader("Dashboard de vendas")
qtd_vendas = len(vendas)
faturamento = float(vendas["valor"].sum())
unidades = int(vendas["quantidade"].sum()) if qtd_vendas else 0
ticket = faturamento / qtd_vendas if qtd_vendas else 0
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("Faturamento", moeda(faturamento))
kpi2.metric("Vendas", qtd_vendas)
kpi3.metric("Unidades vendidas", unidades)
kpi4.metric("Ticket médio", moeda(ticket))

if not vendas.empty:
    graficos = vendas.groupby(["vendedor", "produto"], as_index=False)["valor"].sum()
    por_produto = vendas.groupby("produto", as_index=False)["valor"].sum()
    esquerda, direita = st.columns(2)
    with esquerda:
        st.plotly_chart(px.bar(graficos, x="vendedor", y="valor", color="produto", title="Faturamento por vendedor"), use_container_width=True)
    with direita:
        st.plotly_chart(px.pie(por_produto, names="produto", values="valor", title="Participação no faturamento"), use_container_width=True)

st.caption(
    "💡 Dica: Baixe regularmente o CSV atualizado "
    "para manter uma cópia de segurança das suas vendas."
)
