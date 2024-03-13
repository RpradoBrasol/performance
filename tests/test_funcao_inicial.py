from app.funcao_inicial_ import funcao_teste

def test_funcao_inicial():
    saida = funcao_teste()
    gabarito = 'teste'
    assert saida == gabarito