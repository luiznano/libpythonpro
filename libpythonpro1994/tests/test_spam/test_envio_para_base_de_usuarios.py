import pytest
from unittest.mock import Mock
from libpythonpro1994.spam.main import EnviadorDeSpam
from libpythonpro1994.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [Usuario(nome='Renzo Luiz', email='luizfernandosmh@hotmail.com'),
            Usuario(nome='Luciano Fernanda', email='mellohenriques@globo.com')],
        [Usuario(nome='Renzo Luiz', email='luizfernandosmh@hotmail.com')]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'luizfernandosmh@hotmail.com',
        'OI',
        'oi'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Renzo Luiz', email='luizfernandosmh@hotmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'mellohenriques@globo.com',
        'OI',
        'oi'
    )
    enviador.enviar.assert_called_once_with(
        'mellohenriques@globo.com',
        'luizfernandosmh@hotmail.com',
        'OI',
        'oi'
    )
