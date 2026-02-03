# Scripts DAX - Projeto de BI: Análise de Vendas e Performance Comercial

Este documento contém as fórmulas DAX (Data Analysis Expressions) utilizadas para criar as métricas e medidas calculadas no Power BI.

## 1. Medidas de Vendas

### 1.1. Faturamento Total
Calcula o valor total das vendas realizadas.
```dax
Faturamento Total = SUM(Fato_Vendas[Valor_Total])
```

### 1.2. Quantidade Vendida
Calcula a quantidade total de itens vendidos.
```dax
Quantidade Vendida = SUM(Fato_Vendas[Quantidade])
```

### 1.3. Ticket Médio
Calcula o valor médio de cada venda.
```dax
Ticket Médio = DIVIDE([Faturamento Total], [Quantidade Vendida], 0)
```

## 2. Medidas de Lucratividade

### 2.1. Custo Total
Calcula o custo total dos produtos vendidos.
```dax
Custo Total = SUM(Fato_Vendas[Custo_Total])
```

### 2.2. Lucro Total
Calcula o lucro total (Faturamento - Custo).
```dax
Lucro Total = [Faturamento Total] - [Custo Total]
```

### 2.3. Margem de Lucro (%)
Calcula a margem de lucro percentual.
```dax
Margem de Lucro (%) = DIVIDE([Lucro Total], [Faturamento Total], 0)
```

## 3. Medidas de Performance e Metas

### 3.1. Meta de Vendas
Calcula a meta total de vendas.
```dax
Meta de Vendas = SUM(Fato_Metas[Meta_Vendas])
```

### 3.2. % Atingimento da Meta
Calcula o percentual de atingimento da meta de vendas.
```dax
% Atingimento da Meta = DIVIDE([Faturamento Total], [Meta_Vendas], 0)
```

## 4. Medidas de Inteligência de Tempo (Time Intelligence)

### 4.1. Faturamento Ano Anterior (LY)
Calcula o faturamento do mesmo período no ano anterior.
```dax
Faturamento LY = CALCULATE([Faturamento Total], SAMEPERIODLASTYEAR(Dim_Tempo[Data]))
```

### 4.2. Crescimento Ano a Ano (YoY %)
Calcula o crescimento percentual em relação ao ano anterior.
```dax
Crescimento YoY (%) = DIVIDE([Faturamento Total] - [Faturamento LY], [Faturamento LY], 0)
```

### 4.3. Faturamento Acumulado no Ano (YTD)
Calcula o faturamento acumulado desde o início do ano até a data atual.
```dax
Faturamento YTD = TOTALYTD([Faturamento Total], Dim_Tempo[Data])
```

## 5. Criação da Tabela de Tempo (Calendário)
Script para criar a tabela de dimensão de tempo diretamente no Power BI.
```dax
Dim_Tempo = 
ADDCOLUMNS (
    CALENDARAUTO(),
    "Ano", YEAR([Date]),
    "Mês", FORMAT([Date], "MMMM"),
    "Mês_Num", MONTH([Date]),
    "Dia", DAY([Date]),
    "Dia_da_Semana", FORMAT([Date], "dddd"),
    "Semana_do_Ano", WEEKNUM([Date]),
    "Trimestre", "T" & FORMAT([Date], "Q")
)
```
