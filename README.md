# Taller Práctico TDD: Kata "RPG Combat"

**Asignatura:** Análisis y Diseño / Calidad de Software  
**Duración estimada:** 100 minutos  
**Metodología:** Test-Driven Development (TDD)

## Objetivo

Desarrollar el motor de combate de un videojuego RPG aplicando estrictamente la metodología **Test-Driven Development (TDD)**.

> **Regla de oro:** Está prohibido escribir código de producción sin antes tener una prueba que falle (Rojo).

## Las Reglas del Negocio (Product Backlog)

El equipo de Game Design nos ha entregado las siguientes reglas para nuestra clase `Personaje`:

1. Los personajes nacen con **1000 puntos de vida (HP)**, nivel 1 y están **Vivos**.
2. Un personaje puede hacer **daño** a otro personaje. El daño se resta de los HP.
3. Si los HP llegan a **0 o menos**, el personaje **muere** (el HP no puede ser negativo, debe quedar en 0).
4. Un personaje puede **curar** a otro personaje (solo si el objetivo está vivo; los muertos no se curan).
5. La curación no puede superar los **1000 HP** iniciales (Vida máxima).

## Ciclo TDD

```text
RED  →  GREEN  →  REFACTOR
```

1. **RED**: Escribe una prueba que falle
2. **GREEN**: Escribe el código mínimo para que pase
3. **REFACTOR**: Mejora el código sin romper las pruebas

## Estructura del Proyecto

```text
.
├── rpg.py          # Código de producción
└── test_rpg.py     # Pruebas automatizadas
```

## Instalación y Ejecución

```bash
# Instalar pytest
pip install pytest

# Ejecutar las pruebas
pytest

# Ejecutar con verbose
pytest -v
```

## Fases del Taller

| Fase | Descripción | Minutos |
|------|-------------|---------|
| Base 1 | El nacimiento del héroe | 0-20 |
| Base 2 | El primer golpe | 20-45 |
| Base 3 | Magia blanca (reto autónomo) | 45-80 |
| Base 4 | Auditoría final y cierre | 80-100 |

## Historial de Commits TDD

```text
chore: setup inicial del proyecto TDD
test(RED):   personaje nace con estadísticas correctas
feat(GREEN): implementar clase Personaje con estadísticas iniciales
test(RED):   personaje recibe daño al ser atacado
feat(GREEN): implementar método atacar con lógica de daño básica
test(RED):   personaje muere si HP llega a cero o menos
feat(GREEN): ajustar atacar para manejar muerte del personaje
test(RED):   tres pruebas de curación (Reglas 4 y 5)
feat(GREEN): implementar método curar con reglas de negocio
```

## Resultado Final

```python
class Personaje:
    def __init__(self):
        self.hp = 1000
        self.nivel = 1
        self.esta_vivo = True

    def atacar(self, objetivo, dano):
        objetivo.hp -= dano
        if objetivo.hp <= 0:
            objetivo.hp = 0
            objetivo.esta_vivo = False

    def curar(self, objetivo, cantidad):
        if not objetivo.esta_vivo:
            return  # Regla 4: Los muertos no se curan
        objetivo.hp += cantidad
        if objetivo.hp > 1000:
            objetivo.hp = 1000  # Regla 5: Límite de 1000 HP
```

## Preguntas de Reflexión

1. **¿Tiene dependencias externas o código inútil?**  
   No. La clase `Personaje` solo contiene lo que las pruebas exigieron. TDD produjo código mínimo y limpio.

2. **Si los personajes pasan a nacer con 2000 HP, ¿qué es lo primero que modifican?**  
   La **prueba** `test_personaje_nace_con_estadisticas_correctas`. Cambiando el assert primero, el test se vuelve rojo y guía el cambio en producción — así funciona TDD.
