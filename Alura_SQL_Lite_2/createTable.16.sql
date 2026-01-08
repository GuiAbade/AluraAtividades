select instituicao, COUNT(curso)
from Treinamento
GROUP BY instituicao
HAVING count(curso) >2;