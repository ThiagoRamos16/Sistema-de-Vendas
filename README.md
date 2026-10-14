# 📊 Sistema de Vendas | Python, Streamlit e Análise de Dados

Aplicação web desenvolvida para **registrar vendas, organizar informações comerciais e acompanhar indicadores de faturamento** por meio de um dashboard interativo.

> **Sobre o projeto**
>
> Projeto de portfólio desenvolvido a partir do conteúdo educacional *Sistema de Vendas com Python*, da Jornada Python, promovida pela Hashtag Programação, com adaptações e melhorias próprias nas funcionalidades e na organização do código.
>
> A aplicação utiliza dados fictícios para fins educacionais e demonstra conceitos de desenvolvimento em Python, manipulação de dados e visualização de indicadores comerciais.

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
| **GitHub** | Versionamento e disponibilização do código |

## ✅ Funcionalidades da versão original

- Cadastro de vendas com **data, vendedor, produto, quantidade e valor**.
- Consulta dos registros em tabela interativa.
- Cálculo do **faturamento total** por soma da coluna `valor`.
- Gráfico de barras comparando vendas por vendedor, segmentadas por produto.
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

**Vendas por vendedor**: visualização em barras para comparar a distribuição do faturamento por vendedor e produto.

**Participação por produto**: gráfico de pizza para visualizar a contribuição relativa de cada categoria para o faturamento.

Essas visualizações apoiam a exploração inicial dos dados, mas **não representam resultados de uma operação comercial real**.

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
└── README.md          # Documentação do projeto
```

## 🧠 Aprendizados

Este projeto permitiu praticar:

- Manipulação de dados tabulares com DataFrames.
- Leitura e gravação de arquivos CSV.
- Criação de formulários e componentes web com Streamlit.
- Cálculo de indicadores comerciais.
- Visualização de dados com Plotly.
- Organização e documentação de um projeto no GitHub.

## 🚧 Melhorias em desenvolvimento

As funcionalidades abaixo fazem parte do plano de evolução do projeto e **devem ser marcadas como concluídas apenas após confirmação no código publicado**:

- Cadastro com preço unitário predefinido e desconto opcional.
- Exclusão de registros com confirmação e backup.
- Novos KPIs: quantidade de vendas, unidades e ticket médio.
- Exportação do CSV atualizado para análise no Power BI.
- Construção de um dashboard complementar no Power BI.
- Evolução para armazenamento persistente em banco de dados.

## ⚠️ Limitações

O armazenamento atual utiliza um **arquivo CSV local**, adequado ao objetivo didático. Em ambientes de hospedagem com sistema de arquivos temporário, alterações feitas durante o uso podem não permanecer após reinicializações. Para uso em produção, seria necessário adotar armazenamento persistente e controles adicionais de integridade e concorrência.

## 📚 Origem do projeto

Projeto baseado na aula **Sistema de Vendas com Python**, da **Jornada Python — Hashtag Programação**. A documentação descreve a implementação educacional e suas possíveis evoluções, sem atribuir resultados comerciais reais à aplicação.

## 👤 Autor

**Thiago Ramos** — [GitHub](https://github.com/ThiagoRamos16)
