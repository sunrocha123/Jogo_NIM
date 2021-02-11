<<<<<<< HEAD
import partida
import pytest

class Testes:

    @pytest.mark.parametrize("retorno_esperado",[
        (0)
    ])
    def test(self, retorno_esperado):
        caminho = partida.Partida()
        assert caminho.jogar() == retorno_esperado
=======
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
>>>>>>> 86c6be42e71c43c0c9b6fd8a91611fb1197aae29
