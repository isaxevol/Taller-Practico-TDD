# Pruebas automatizadas del motor de combate RPG
# Siguiendo el ciclo TDD: RED -> GREEN -> REFACTOR

from rpg import Personaje


# =============================================================
# BASE 1: El nacimiento del héroe
# Regla 1: Los personajes nacen con 1000 HP, nivel 1 y vivos.
# =============================================================

def test_personaje_nace_con_estadisticas_correctas():
    # Arrange (preparar)
    heroe = Personaje()

    # Assert (verificar)
    assert heroe.hp == 1000
    assert heroe.nivel == 1
    assert heroe.esta_vivo == True
