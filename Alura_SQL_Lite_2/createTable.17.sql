select cargo, COUNT(*) qtd
from HistoricoEmprego
GROUP BY cargo
HAVING qtd >= 2;