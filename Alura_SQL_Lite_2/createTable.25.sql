select (' O faturamento bruto médio foi R$' || CAST(ROUND (AVG(faturamento_bruto),2) AS TEXT))
        FROM  faturamento;