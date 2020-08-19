from libpythonpro1994.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Renzo Luiz', email='luizfernandosmh@hotmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Renzo Luiz', email='luizfernandosmh@hotmail.com'),
                Usuario(nome='Luciano Fernanda', email='mellohenriques@globo.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
