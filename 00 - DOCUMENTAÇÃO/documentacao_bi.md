# Documentação Técnica do Projeto de BI - Análise de Vendas e Performance Comercial

## 1. Introdução

Este documento detalha a estrutura e o processo de construção de um projeto de Business Intelligence (BI) focado na análise de vendas e performance comercial para uma empresa de varejo fictícia. O objetivo é fornecer uma visão clara sobre o modelo de dados, o processo de Extração, Transformação e Carga (ETL) e as métricas-chave para análise no Power BI.

## 2. Modelo de Dados

O modelo de dados é baseado em um esquema estrela, otimizado para consultas analíticas e desempenho no Power BI. Ele é composto por uma tabela de fatos (Fato_Vendas) e três tabelas de dimensão (Dim_Produtos, Dim_Clientes, Dim_Tempo) e uma tabela de fatos auxiliar (Fato_Metas).

### 2.1. Tabelas de Dimensão

| Tabela         | Descrição                                                              | Colunas Chave | Outras Colunas                                |
| :------------- | :--------------------------------------------------------------------- | :------------ | :-------------------------------------------- |
| **Dim_Produtos** | Contém informações detalhadas sobre os produtos vendidos.              | ID_Produto    | Produto, Categoria, Preco_Unitario, Custo_Unitario |
| **Dim_Clientes** | Armazena dados dos clientes que realizaram compras.                    | ID_Cliente    | Nome_Cliente, Regiao, Tipo_Cliente            |
| **Dim_Tempo**    | Tabela de tempo para análises temporais (será criada no Power BI).     | Data          | Ano, Mês, Dia, Dia_da_Semana, Semana_do_Ano   |

### 2.2. Tabelas de Fatos

| Tabela         | Descrição                                                              | Colunas Chave | Outras Colunas                                |
| :------------- | :--------------------------------------------------------------------- | :------------ | :-------------------------------------------- |
| **Fato_Vendas**  | Registra cada transação de venda, incluindo detalhes do produto e cliente. | ID_Venda      | Data, ID_Produto, ID_Cliente, Quantidade, Valor_Total, Custo_Total, Lucro, Canal_Venda |
| **Fato_Metas**   | Contém as metas de vendas mensais por categoria de produto.            | Mes_Ano, Categoria | Meta_Vendas                                   |

### 2.3. Relacionamentos

Os relacionamentos entre as tabelas são os seguintes:

*   **Fato_Vendas** se relaciona com **Dim_Produtos** por `ID_Produto` (Muitos para Um).
*   **Fato_Vendas** se relaciona com **Dim_Clientes** por `ID_Cliente` (Muitos para Um).
*   **Fato_Vendas** se relaciona com **Dim_Tempo** por `Data` (Muitos para Um).
*   **Fato_Metas** se relaciona com **Dim_Tempo** por `Mes_Ano` (Muitos para Um, após a criação da coluna de data na Fato_Metas).
*   **Fato_Metas** se relaciona com **Dim_Produtos** por `Categoria` (Muitos para Um, após a criação de uma tabela de dimensão de categorias ou relacionamento direto).

## 3. Processo ETL (Extração, Transformação e Carga)

O processo ETL para este projeto envolve a extração de dados de arquivos CSV, transformações básicas e o carregamento no Power BI.

### 3.1. Extração

Os dados são extraídos dos seguintes arquivos, gerados por um script Python:

*   `Dim_Produtos.csv`
*   `Dim_Produtos.xlsx`
*   `Dim_Produtos.parquet`

*   `Dim_Clientes.csv`
*   `Dim_Clientes.xlsx`
*   `Dim_Clientes.parquet`

*   `Fato_Vendas.csv`
*   `Fato_Vendas.xlsx`
*   `Fato_Vendas.parquet`

*   `Fato_Metas.csv`
*   `Fato_Metas.xlsx`
*   `Fato_Metas.parquet`

### 3.2. Transformação

As transformações serão realizadas principalmente no Power Query (M) do Power BI e incluem:

*   **Fato_Vendas:**
    *   Garantir tipos de dados corretos para todas as colunas (Data como Data, Quantidade como Número Inteiro, Valores Monetários como Número Decimal).
    *   Criação de colunas calculadas básicas, se necessário, antes do carregamento para o modelo.
*   **Dim_Produtos:**
    *   Garantir tipos de dados corretos.
*   **Dim_Clientes:**
    *   Garantir tipos de dados corretos.
*   **Fato_Metas:**
    *   Garantir tipos de dados corretos.
    *   Transformar a coluna `Mes_Ano` para o tipo Data para permitir o relacionamento com a `Dim_Tempo`.

### 3.3. Carga

Após as transformações, os dados são carregados no modelo de dados do Power BI, onde os relacionamentos são estabelecidos e as medidas DAX são criadas para análises avançadas.

## 4. Próximos Passos

Os próximos passos incluem a criação das medidas DAX, o desenvolvimento do protótipo do dashboard e a montagem final do relatório no Power BI.
