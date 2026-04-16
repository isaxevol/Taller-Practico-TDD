# Motor de combate RPG
# Este archivo se irá completando siguiendo el ciclo TDD


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
