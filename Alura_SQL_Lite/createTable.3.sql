create table TabelaProdutos (
	ID_Produto INT PRIMARY Key,
  	Nome_do_Produto VARCHAR (250),
  	Descricao TEXT,
  	Categoria INT,
  	Preco_de_Compra DECIMAL (10,2),
  	Unidade VARCHAR (50),
  	Fornecedor INT,
  	Data_de_inclusao DATE,
  
  	FOREIGN Key (Categoria) REFERENCES tabelaCategorias (id_categoria),
  	FOREIGN KEY (Fornecedor) REFERENCES tabelafornecedores (id)
  
);