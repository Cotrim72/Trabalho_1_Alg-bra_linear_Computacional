class Log:
    def __init__(self, iteracao, erro, x):
        self.iteracao = iteracao
        self.erro = erro
        self.x = x

    def __repr__(self):
        return f'Iteração {self.iteracao}: Erro = {self.erro}, x = {self.x}'