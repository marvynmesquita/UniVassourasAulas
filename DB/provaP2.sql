-- Marvyn Porto de Mesquita - 202220948

CREATE TABLE IF NOT EXISTS Cliente(
	id_cliente SERIAL NOT NULL PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
	cidade VARCHAR(100) NOT NULL,
	endereco VARCHAR(300) NOT NULL,
	numero INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS Vendedor(
	id_vendedor SERIAL NOT NULL PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
	loja VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS Vendas(
	id_venda SERIAL NOT NULL PRIMARY KEY,
	id_cliente INTEGER NOT NULL,
	id_vendedor INTEGER NOT NULL,
	numero_de_vendas INTEGER NOT NULL,
	data_da_venda DATE NOT NULL,
	valor_da_venda REAL NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente),
    FOREIGN KEY (id_vendedor) REFERENCES Vendedor(id_vendedor)
);

CREATE TABLE IF NOT EXISTS LogVendas(
    id_log SERIAL NOT NULL PRIMARY KEY,
    operacao VARCHAR(100) NOT NULL,
    data_da_operacao DATE NOT NULL,
    id_venda INTEGER NOT NULL,
    id_vendedor INTEGER NOT NULL,
    numero_de_vendas INTEGER NOT NULL,
    data_da_venda DATE DEFAULT NOW(),
    valor_da_venda REAL NOT NULL
);

CREATE OR REPLACE FUNCTION log_vendas_insert()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO LogVendas(operacao, data_da_operacao, id_venda, id_vendedor, numero_de_vendas, data_da_venda, valor_da_venda)
    VALUES('INSERT', NOW(), NEW.id_venda, NEW.id_vendedor, NEW.numero_de_vendas, NEW.data_da_venda, NEW.valor_da_venda);
    RETURN NEW;
END;
$$ language plpgsql;

CREATE OR REPLACE FUNCTION log_vendas_update()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO LogVendas(operacao, data_da_operacao, id_venda, id_vendedor, numero_de_vendas, data_da_venda, valor_da_venda)
    VALUES('UPDATE', NOW(), NEW.id_venda, NEW.id_vendedor, NEW.numero_de_vendas, NEW.data_da_venda, NEW.valor_da_venda);
    RETURN NEW;
END;
$$ language plpgsql;

CREATE OR REPLACE FUNCTION log_vendas_delete()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO LogVendas(operacao, data_da_operacao, id_venda, id_vendedor, numero_de_vendas, data_da_venda, valor_da_venda)
    VALUES('DELETE', NOW(), OLD.id_venda, OLD.id_vendedor, OLD.numero_de_vendas, OLD.data_da_venda, OLD.valor_da_venda);
    RETURN NEW;
END;
$$ language plpgsql;

CREATE TRIGGER trigger_log_vendas_insert
AFTER INSERT ON Vendas
FOR EACH ROW
EXECUTE FUNCTION log_vendas_insert();

CREATE TRIGGER trigger_log_vendas_update
AFTER UPDATE ON Vendas
FOR EACH ROW
EXECUTE FUNCTION log_vendas_update();

CREATE TRIGGER trigger_log_vendas_delete
AFTER DELETE ON Vendas
FOR EACH ROW
EXECUTE FUNCTION log_vendas_delete();

INSERT INTO Cliente(nome, cidade, endereco, numero) VALUES(
    'João',
    'São Paulo',
    'Rua 1',
    1
);

INSERT INTO Cliente(nome, cidade, endereco, numero) VALUES(
    'Maria',
    'São Paulo',
    'Rua 2',
    2
);

INSERT INTO Cliente(nome, cidade, endereco, numero) VALUES(
    'José',
    'São Paulo',
    'Rua 3',
    3
);

INSERT INTO Cliente(nome, cidade, endereco, numero) VALUES(
    'Ana',
    'São Paulo',
    'Rua 4',
    4
);

INSERT INTO Cliente(nome, cidade, endereco, numero) VALUES(
    'Pedro',
    'São Paulo',
    'Rua 5',
    5
);

INSERT INTO Vendedor(nome, loja) VALUES(
    'Jorge',
    'Casas Salvador'
);

INSERT INTO Vendedor(nome, loja) VALUES(
    'Bernardina',
    'Ponto Quente'
);

INSERT INTO Vendedor(nome, loja) VALUES(
    'Mariana',
    'Casas Salvador'
);

INSERT INTO Vendedor(nome, loja) VALUES(
    'Joana',
    'Ponto Quente'
);

INSERT INTO Vendedor(nome, loja) VALUES(
    'Joaquim',
    'Casas Salvador'
);

INSERT INTO Vendas(id_cliente, id_vendedor, numero_de_vendas, data_da_venda, valor_da_venda) VALUES(
    1,
    1,
    1,
    '2021-01-01',
    100.00
);

INSERT INTO Vendas(id_cliente, id_vendedor, numero_de_vendas, data_da_venda, valor_da_venda) VALUES(
    2,
    2,
    2,
    '2021-01-02',
    200.00
);

INSERT INTO Vendas(id_cliente, id_vendedor, numero_de_vendas, data_da_venda, valor_da_venda) VALUES(
    3,
    3,
    3,
    '2021-01-03',
    300.00
);

INSERT INTO Vendas(id_cliente, id_vendedor, numero_de_vendas, data_da_venda, valor_da_venda) VALUES(
    4,
    4,
    4,
    '2021-01-04',
    400.00
);

INSERT INTO Vendas(id_cliente, id_vendedor, numero_de_vendas, data_da_venda, valor_da_venda) VALUES(
    5,
    5,
    5,
    '2021-01-05',
    500.00
);

INSERT INTO Vendas(id_cliente, id_vendedor, numero_de_vendas, data_da_venda, valor_da_venda) VALUES(
    1,
    1,
    1,
    '2021-01-06',
    600.00
);

 INSERT INTO Vendas(id_cliente, id_vendedor, numero_de_vendas, data_da_venda, valor_da_venda) VALUES(
    2,
    2,
    2,
    '2021-01-07',
    700.00
);

 INSERT INTO Vendas(id_cliente, id_vendedor, numero_de_vendas, data_da_venda, valor_da_venda) VALUES(
    3,
    3,
    3,
    '2021-01-08',
    800.00
);


UPDATE Vendas SET valor_da_venda = 1000.00 WHERE id_venda = 1;
UPDATE Vendedor SET nome = 'Jorge Silva' WHERE id_vendedor = 1;
UPDATE Cliente SET cidade = 'Rio de Janeiro' WHERE id_cliente = 1;


DELETE FROM Vendas WHERE id_vendedor = 5;
DELETE FROM Vendedor WHERE id_vendedor = 5;
DELETE FROM Cliente WHERE id_cliente = 5;

SELECT COUNT(id_venda) INTO id_vendas_count
FROM Vendas;

SELECT SUM(valor_da_venda) INTO Vendas_sum
FROM Vendas;

SELECT C.nome, C.cidade, C.endereco, C.numero, V.numero_de_vendas, V.data_da_venda, V.valor_da_venda, Ve.nome AS vendedor_nome, Ve.loja
FROM Cliente C
INNER JOIN Vendas V ON C.id_cliente = V.id_cliente
INNER JOIN Vendedor Ve ON V.id_vendedor = Ve.id_vendedor;

SELECT C.nome, C.cidade, V.numero_de_vendas, V.data_da_venda, V.valor_da_venda
FROM Cliente C
RIGHT JOIN Vendas V ON C.id_cliente = V.id_cliente;

SELECT C.nome, C.cidade, V.numero_de_vendas, V.data_da_venda, V.valor_da_venda
FROM Cliente C
LEFT JOIN Vendas V ON C.id_cliente = V.id_cliente;
