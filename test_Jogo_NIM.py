import partida
import pytest

class Testes:

    @pytest.mark.parametrize("numero_de_pecas, limite_de_jogada, retorno_esperado",[
        (10,5,0),
        (20,4,0),
        (5,2,0),
        (900,56,0)
    ])
    def test(self, numero_de_pecas, limite_de_jogada, retorno_esperado):
        caminho = partida.Partidas()
        assert caminho.usuario_comeca(numero_de_pecas, limite_de_jogada) == retorno_esperado
        assert caminho.computador_comeca(numero_de_pecas, limite_de_jogada) == retorno_esperado