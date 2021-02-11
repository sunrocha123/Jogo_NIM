import partida
import pytest

class Testes:

    @pytest.mark.parametrize("retorno_esperado",[
        (0)
    ])
    def test(self, retorno_esperado):
        caminho = partida.Partida()
        assert caminho.jogar() == retorno_esperado