SELECT UPPER('A pessoa colaboradora ' || nome || ' de CPF ' || cpf || ' possui o seguinte endereço: '
        || endereco) as texto
        FROM Colaboradores;