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

```
RED  →  GREEN  →  REFACTOR
```

1. **RED**: Escribe una prueba que falle
2. **GREEN**: Escribe el código mínimo para que pase
3. **REFACTOR**: Mejora el código sin romper las pruebas

## Estructura del Proyecto

```
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
