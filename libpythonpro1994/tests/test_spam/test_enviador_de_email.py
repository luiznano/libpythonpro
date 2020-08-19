import pytest

from libpythonpro1994.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize('remetente', ['luizfernandosmh@hotmail.com', 'luizfernandosmh@gmail.com'])
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'mellohenriques@globo.com',
        'OI',
        'oi'
    )

    assert remetente in resultado


@pytest.mark.parametrize('remetente', ['', 'luizfernandosmhgmail.com'])
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'mellohenriques@globo.com',
            'OI',
            'oi'
        )
