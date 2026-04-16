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


def test_personaje_muere_si_hp_llega_a_cero():
    # Arrange
    heroe = Personaje()
    enemigo = Personaje()

    # Act - daño mayor que la vida del héroe
    enemigo.atacar(heroe, dano=1500)

    # Assert - HP no puede quedar en negativo
    assert heroe.hp == 0
    assert heroe.esta_vivo == False


# =============================================================
# BASE 3: Magia blanca (reto autónomo)
# Regla 4: Un personaje puede curar a otro (solo si está vivo).
# Regla 5: La curación no puede superar los 1000 HP máximos.
# =============================================================

def test_curar_personaje():
    # Arrange - héroe herido (800 HP)
    heroe = Personaje()
    heroe.hp = 800

    sanador = Personaje()

    # Act - curar 100 HP
    sanador.curar(heroe, cantidad=100)

    # Assert - debe tener 900 HP
    assert heroe.hp == 900


def test_no_curar_mas_del_maximo():
    # Arrange - héroe con 900 HP
    heroe = Personaje()
    heroe.hp = 900

    sanador = Personaje()

    # Act - intentar curar 200 HP (superaría el máximo)
    sanador.curar(heroe, cantidad=200)

    # Assert - no puede pasar de 1000 HP
    assert heroe.hp == 1000


def test_los_muertos_no_se_curan():
    # Arrange - héroe muerto
    heroe = Personaje()
    heroe.hp = 0
    heroe.esta_vivo = False

    sanador = Personaje()

    # Act - intentar curar a un personaje muerto
    sanador.curar(heroe, cantidad=500)

    # Assert - los atributos deben mantenerse intactos
    assert heroe.hp == 0
    assert heroe.esta_vivo == False
