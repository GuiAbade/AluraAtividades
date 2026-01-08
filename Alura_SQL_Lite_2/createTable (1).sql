SELECT * FROM HistoricoEmprego
WHERE datatermino IS not null
order by salario desc 
limit 5;