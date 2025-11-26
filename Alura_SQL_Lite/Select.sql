Create table tabelaPedidosGold (
	ID_pedido_gold INT PRIMARY Key,
  	Data_do_Pedido_gold Date,
  	Status_gold VARCHAR(50),
  	Total_Do_Pedido_Gold DECIMAL (10,2),
  	Cliente_gold INT,
  	Data_de_Envio_estimada_gold Date,
  FOREIGN KEY (Cliente_gold) REFERENCES tabelaclientes(id_cliente)
);
