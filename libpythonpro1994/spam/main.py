class EnviadorDeSpam():
    def __init__(self, sessao, enviador):
        self.sessao = sessao
        self.enviador = enviador

    def enviar_emails(self, remetente, assuto, corpo):
        for usuario in self.sessao.listar():
            self.enviador.enviar(
                remetente,
                usuario.email,
                assuto,
                corpo
            )
