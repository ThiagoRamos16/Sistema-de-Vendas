# 📊 Sistema de Vendas | Python, Streamlit e Análise de Dados

[![Acessar aplicativo](https://img.shields.io/badge/Acessar_App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://sistema-de-vendas-3aver4pa4wqpe3z2jxrqyj.streamlit.app)

Aplicação web desenvolvida para **registrar vendas, organizar informações comerciais e acompanhar indicadores de faturamento** por meio de um dashboard interativo.

> **Sobre o projeto**
>
> Projeto de portfólio desenvolvido a partir do conteúdo educacional Sistema de Vendas com Python, da Jornada Python, promovida pela Hashtag Programação, com adaptações e melhorias próprias nas funcionalidades e na organização do código.
A aplicação utiliza dados fictícios para fins educacionais e demonstra conceitos de desenvolvimento em Python, manipulação de dados e visualização de indicadores comerciais.

## 🚀 Demonstração Online

A aplicação está disponível para acesso e testes pelo **Streamlit Community Cloud**.

🔗 **[Acessar Sistema de Vendas — Demonstração Online](https://sistema-de-vendas-3aver4pa4wqpe3z2jxrqyj.streamlit.app)**

Na aplicação, é possível cadastrar vendas com cálculo de valor e desconto, consultar e excluir registros, exportar os dados em CSV e acompanhar indicadores de faturamento em gráficos interativos.

*Os dados utilizados são fictícios e destinam-se a fins educacionais.*

## 🎯 Visão geral

O projeto simula a necessidade de centralizar registros de vendas que poderiam estar dispersos em planilhas e transformar essas informações em indicadores fáceis de consultar.

Com Python, Streamlit, Pandas e Plotly, a solução reúne **cadastro de vendas**, **consulta dos registros** e **visualização do faturamento** em uma interface web.

**Problema → implementação → entrega:** organização manual de vendas → cadastro estruturado e processamento com Pandas → histórico consultável e gráficos de desempenho comercial.

## 🛠️ Tecnologias utilizadas

| Tecnologia | Aplicação no projeto |
| --- | --- |
| **Python** | Lógica da aplicação e cálculos |
| **Streamlit** | Interface web, formulário, tabela e indicadores |
| **Pandas** | Leitura, atualização, agregação e gravação do CSV |
| **Plotly Express** | Gráficos interativos de vendas |
| **CSV** | Armazenamento local dos registros |
| **Power BI Desktop** | Dashboard de análise comercial e filtros interativos 
| **Power Query** | Importação, tipagem e verificação de qualidade do CSV |
| **DAX** | Medidas de faturamento, vendas, unidades vendidas e ticket médio |
| **GitHub** | Versionamento e disponibilização do código |

## ✅ Funcionalidades

- Cadastro de vendas com **data, vendedor, produto e quantidade**, com cálculo automático do valor a partir do preço unitário.
- Aplicação de desconto percentual opcional no cadastro, refletido no valor final da venda.
- Consulta dos registros em tabela interativa.
- Exclusão de vendas selecionadas, com confirmação e cópia de segurança local.
- Exportação do CSV para análises externas, como no Power BI.
- Indicadores de **faturamento total, número de vendas, unidades vendidas e ticket médio**.
- Gráfico de barras comparando faturamento por vendedor, segmentado por produto.
- Gráfico de pizza mostrando a participação dos produtos no faturamento.

## 🔄 Fluxo de dados

```text
Formulário Streamlit
       ↓
Registro da venda
       ↓
DataFrame Pandas
       ↓
Leitura e gravação em vendas.csv
       ↓
Indicadores e gráficos Plotly
       ↓
Exportação manual do CSV pelo Streamlit
       ↓
Power Query (importação, tipos e validação)
       ↓
Medidas DAX e dashboard Power BI
```

O sistema lê `vendas.csv` com `pd.read_csv()`. Ao cadastrar uma nova venda, adiciona uma linha ao DataFrame e atualiza o arquivo usando `to_csv(index=False)`. O mesmo conjunto de dados alimenta a tabela e o dashboard.

## 🗂️ Estrutura da base

| Coluna | Descrição |
| --- | --- |
| `data` | Data da venda |
| `vendedor` | Vendedor responsável |
| `produto` | Produto comercializado |
| `quantidade` | Número de unidades da venda |
| `valor` | Valor total registrado para a venda |

Os dados são fictícios. A coluna `valor` é utilizada para apurar o faturamento, sem multiplicá-la novamente por `quantidade`.

## 📈 Indicadores e visualizações

**Faturamento total**: soma dos valores de venda registrados na base.

**Quantidade de vendas**: número de registros no DataFrame.

**Unidades vendidas**: soma das quantidades comercializadas.

**Ticket médio**: faturamento total dividido pela quantidade de vendas.

**Vendas por vendedor**: visualização em barras para comparar a distribuição do faturamento por vendedor e produto.

**Participação por produto**: gráfico de pizza para visualizar a contribuição relativa de cada categoria para o faturamento.

Essas visualizações apoiam a exploração inicial dos dados, mas **não representam resultados de uma operação comercial real**.


## 📊 Dashboard complementar no Power BI
Como evolução do Sistema de Vendas, foi criado um dashboard comercial no Power BI Desktop com os dados exportados em CSV pelo Streamlit. A proposta é demonstrar um fluxo de análise: registro e exportação das vendas → preparação dos dados → cálculo de indicadores → visualização interativa.



## 🔎 Preparação e qualidade dos dados
No Power Query, foram conferidos os tipos das colunas (`data`, `vendedor`, `produto`, `quantidade`, `valor`), a presença de erros e valores vazios e a interpretação dos números decimais durante a importação. A base utilizada é fictícia, e a checagem de tipos e preenchimento não substitui a validação de regras de negócio.


## 📐 Indicadores com DAX
| Indicador | Cálculo utilizado |
| --- | --- |
| **Faturamento Total** | `SUM(vendas[valor])` |
| **Quantidade de Vendas** | `COUNTROWS(vendas)` |
| **Unidades Vendidas** | `SUM(vendas[quantidade])` |
| **Ticket Médio** | `DIVIDE([Faturamento Total], [Quantidade de Vendas], 0)` |

As medidas respondem aos filtros aplicados ao relatório. Os visuais também utilizam formatação monetária para apresentar os indicadores em reais.


## 📈 Análises e interatividade
- Faturamento por vendedor: comparação da receita entre os vendedores da base.
- Faturamento por produto: comparação da participação de Notebook, Celular e Fone na receita.
- Evolução mensal do faturamento: acompanhamento do desempenho em diferentes meses.
- Segmentações por vendedor e produto: exploração dinâmica dos indicadores e gráficos.


## 🖥️ Prévia do dashboard
<img width="1462" height="826" alt="image" src="https://github.com/user-attachments/assets/34c8ae6b-2178-4a7c-8b21-98994dc388f2" />

### 📥 Arquivo Power BI

O dashboard está disponível para download e pode ser aberto no Power BI Desktop.

[📊 Acessar Dashboard Comercial (.pbix)](power-bi/Dashboard_Comercial_Vendas.pbix)


## ▶️ Como executar localmente

**Pré-requisito:** Python instalado.


1. Clone o repositório:

```bash
git clone https://github.com/ThiagoRamos16/Sistema-de-Vendas.git
cd Sistema-de-Vendas
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Inicie a aplicação:

```bash
streamlit run main.py
```

O Streamlit abrirá um endereço local no navegador.

## 📁 Arquivos do projeto

```text
Sistema-de-Vendas/
├── main.py            # Interface, cadastro e dashboard
├── vendas.csv         # Dados fictícios de vendas
├── requirements.txt   # Dependências Python
├── README.md          # Documentação do projeto
└── power-bi/
    ├── Dashboard_Comercial_Vendas_Final.pbix  # Relatório Power BI
    └── dashboard_preview.png                 # Captura do dashboard
```

## 🧠 Aprendizados

Este projeto permitiu praticar:

- Manipulação de dados tabulares com DataFrames.
- Leitura e gravação de arquivos CSV.
- Criação de formulários e componentes web com Streamlit.
- Cálculo de indicadores comerciais.
- Visualização de dados com Plotly.
- Tratamento e validação dos dados no Power Query.
- Criação de medidas DAX e dashboards interativos no Power BI.
- Organização e documentação de um projeto no GitHub.
  

## 🚧 Próximas evoluções

- Construção de um dashboard complementar no Power BI a partir do CSV exportado.
- Armazenamento persistente em banco de dados.
- Possível registro do percentual de desconto na base para análises históricas (atualmente, a coluna `valor` armazena o total final da venda).

## ⚠️ Limitações

O armazenamento atual utiliza um **arquivo CSV local**, adequado ao objetivo didático. Em ambientes de hospedagem com sistema de arquivos temporário, alterações feitas durante o uso podem não permanecer após reinicializações. Para uso em produção, seria necessário adotar armazenamento persistente e controles adicionais de integridade e concorrência.

## 📚 Origem do projeto

Projeto baseado na aula **Sistema de Vendas com Python**, da **Jornada Python — Hashtag Programação**. A documentação descreve a implementação educacional e suas possíveis evoluções, sem atribuir resultados comerciais reais à aplicação.

## 👤 Autor

**Thiago Ramos** — [GitHub](https://github.com/ThiagoRamos16)
