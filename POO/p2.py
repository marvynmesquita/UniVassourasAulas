import pandas as pd

class Aluno:
    def __init__(self, nome, idade, status):
        self.nome = nome
        self.idade = idade
        self.status = status

class Cadastro:
    def __init__(self):
        self.df = pd.DataFrame(columns=['Nome', 'Idade', 'Status'])

    def cadastrar_aluno(self, aluno):
        nova_linha = {'Nome': aluno.nome, 'Idade': aluno.idade, 'Status': aluno.status}
        self.df = self.df._append(nova_linha, ignore_index=True)

class AcaoALuno:
    def advertir(self, aluno):
        raise NotImplementedError
    
    def expulsar(self, aluno):
        raise NotImplementedError
    
class Administrador(AcaoALuno):
    def __init__(self, senha):
        self.senha = senha
    def advertir(self, aluno, senha):
        if senha != self.senha:
            raise ValueError('Senha incorreta')
        else:
            index = cadastro.df[cadastro.df['Nome'] == aluno.nome].index[0]
            cadastro.df.loc[index, 'Status'] = 'advertido'
            print(f'O aluno {aluno.nome} foi advertido')

    def expulsar(self, aluno, senha):
        if senha != self.senha:
            raise ValueError('Senha incorreta')
        else:
            index = cadastro.df[cadastro.df['Nome'] == aluno.nome].index[0]
            cadastro.df.loc[index, 'Status'] = 'expulso'
            print(f'O aluno {aluno.nome} foi expulso')
        

aluno1 = Aluno('João', 20, 'ativo')
cadastro = Cadastro()
cadastro.cadastrar_aluno(aluno1)
admin = Administrador('1234')
try:
    admin.advertir(aluno1, '1234')
    admin.expulsar(aluno1, '1234')
except ValueError as err:
    print(err)
print(cadastro.df)