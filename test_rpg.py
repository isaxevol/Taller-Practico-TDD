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


# =============================================================
# BASE 2: El primer golpe
# Regla 2: Un personaje puede hacer daño a otro. El daño se
#          resta de los HP.
# =============================================================

def test_personaje_recibe_dano():
    # Arrange
    heroe = Personaje()
    enemigo = Personaje()

    # Act
    enemigo.atacar(heroe, dano=200)

    # Assert
    assert heroe.hp == 800
