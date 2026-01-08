select id_colaborador, cargo, salario,
CASE 
when salario <3000 then 'baixo'
when salario BETWEEN 3001 AND 6000 THEN 'Médio'
else 'Alto'
end  as categoria_salario
from HistoricoEmprego;