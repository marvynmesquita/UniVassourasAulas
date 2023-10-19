class Banco:
    def __init__(self, conta, usuario, senha, saldo, cpf):
        self.conta = conta
        self.usuario = usuario
        self.senha = senha
        self.saldo = saldo
        self.cpf = cpf
    
class Pessoa:
    def __init__(self, nome, idade, sexo, endereco, cpf):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.endereco = endereco
        self.cpf = cpf

user1 = Pessoa('Enzo', '18', 'M','Saquarema', '123.456.789-00')
user2 = Pessoa('Valentina', '19', 'F','Saquarema', '322.255.496-20')
user3 = Pessoa('Stefan', '20', 'O','Saquarema', '432.234.243-32')

conta1 = Banco(1, {user1.nome}, 123456, 1320.00, {user1.cpf})
conta2 = Banco(2, {user2.nome}, 123456, 700.00, {user2.cpf})
conta3 = Banco(3, {user3.nome}, 123456, 0.00, {user3.cpf})

