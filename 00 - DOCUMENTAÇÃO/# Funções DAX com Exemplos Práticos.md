# Funções DAX com Exemplos Práticos

Este material é um **guia de consulta rápida + exemplos**, focado em **entender como cada função funciona na prática**.

Assumindo tabelas comuns:

* **Fato_Vendas** (Data, Produto, Cliente, Quantidade, Valor)
* **Dim_Produtos** (ProdutoID, Produto, Categoria)
* **Dim_Clientes** (ClienteID, Cliente)
* **Calendario** (Data, Ano, Mês)

---

## 1. Agregação

### SUM

```DAX
Total Vendas = SUM(Fato_Vendas[Valor])
```

Soma simples de uma coluna.

### SUMX

```DAX
Total Vendas = SUMX(Fato_Vendas, Fato_Vendas[Quantidade] * Fato_Vendas[Valor])
```

Itera linha a linha (row context).

### AVERAGE

```DAX
Ticket Médio = AVERAGE(Fato_Vendas[Valor])
```

### COUNTROWS

```DAX
Qtd Vendas = COUNTROWS(Fato_Vendas)
```

---

## 2. Filtro e Contexto

### CALCULATE

```DAX
Vendas 2025 =
CALCULATE(
    [Total Vendas],
    Calendario[Ano] = 2025
)
```

Altera o contexto de filtro.

### FILTER

```DAX
Vendas Alto Valor =
CALCULATE(
    [Total Vendas],
    FILTER(Fato_Vendas, Fato_Vendas[Valor] > 1000)
)
```

### ALL

```DAX
Vendas Total Geral =
CALCULATE([Total Vendas], ALL(Dim_Produtos))
```

Remove filtros.

### SELECTEDVALUE

```DAX
Produto Selecionado = SELECTEDVALUE(Dim_Produtos[Produto], "Vários")
```

---

## 3. Inteligência de Tempo

### TOTALYTD

```DAX
Vendas YTD = TOTALYTD([Total Vendas], Calendario[Data])
```

### SAMEPERIODLASTYEAR

```DAX
Vendas LY =
CALCULATE(
    [Total Vendas],
    SAMEPERIODLASTYEAR(Calendario[Data])
)
```

### DATESMTD

```DAX
Vendas MTD =
CALCULATE([Total Vendas], DATESMTD(Calendario[Data]))
```

---

## 4. Funções Lógicas

### IF

```DAX
Status Venda =
IF([Total Vendas] >= 100000, "Meta Atingida", "Abaixo da Meta")
```

### SWITCH

```DAX
Faixa Venda =
SWITCH(
    TRUE(),
    [Total Vendas] >= 100000, "Alta",
    [Total Vendas] >= 50000, "Média",
    "Baixa"
)
```

---

## 5. Texto

### CONCATENATEX

```DAX
Produtos Vendidos =
CONCATENATEX(
    VALUES(Dim_Produtos[Produto]),
    Dim_Produtos[Produto],
    ", "
)
```

---

## 6. Relacionamentos e Tabelas

### RELATED

```DAX
Categoria Produto = RELATED(Dim_Produtos[Categoria])
```

Usado em coluna calculada.

### SUMMARIZE

```DAX
Resumo Vendas =
SUMMARIZE(
    Fato_Vendas,
    Dim_Produtos[Categoria],
    "Total", [Total Vendas]
)
```

### ADDCOLUMNS

```DAX
Resumo =
ADDCOLUMNS(
    VALUES(Dim_Produtos[Categoria]),
    "Vendas", [Total Vendas]
)
```

---

## 7. Ranking

### RANKX

```DAX
Ranking Produtos =
RANKX(
    ALL(Dim_Produtos),
    [Total Vendas],
    ,
    DESC
)
```

---

## 8. Informações

### ISBLANK

```DAX
Venda Zerada = IF(ISBLANK([Total Vendas]), 0, [Total Vendas])
```

### HASONEVALUE

```DAX
É Único = HASONEVALUE(Dim_Produtos[Produto])
```

---

## 9. Segurança (RLS)

### USERPRINCIPALNAME

```DAX
Usuario Atual = USERPRINCIPALNAME()
```

---

## 10. Padrões Muito Usados

### % Atingimento da Meta

```DAX
% Meta = DIVIDE([Total Vendas], [Meta Vendas])
```

### Crescimento YoY

```DAX
Crescimento YoY =
DIVIDE([Total Vendas] - [Vendas LY], [Vendas LY])
```

---
