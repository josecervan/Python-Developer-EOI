from constants import *


class Battle:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.actual_turn = 0

    def is_finished(self):
        finished = self.pokemon1.current_hp <= 0 or self.pokemon2.current_hp <= 0
        if finished:
            self.print_winner()
        return finished

    def execute_turn(self, turn):
        command1 = turn.command1
        command2 = turn.command2
        attack1 = None
        attack2 = None
        # Se comprueba si los pokemons quieren atacar
        if DO_ATTACK in command1.action.keys():
            attack1 = self.pokemon1.attacks[command1.action[DO_ATTACK]]
        if DO_ATTACK in command2.action.keys():
            attack2 = self.pokemon2.attacks[command2.action[DO_ATTACK]]

        # Fórmula de daños (damage formula)
        self.pokemon2.current_hp -= attack1.power
        self.pokemon1.current_hp -= attack2.power

        self.actual_turn += 1

    def print_current_status(self):
        print(self.pokemon1.name + ' has ' + str(self.pokemon1.current_hp) + ' left!')
        print(self.pokemon2.name + ' has ' + str(self.pokemon2.current_hp) + ' left!')

    def print_winner(self):
        if self.pokemon1.current_hp <= 0 < self.pokemon2.current_hp:
            # Gana el pokemon 2
            print(self.pokemon2.name + ' wins! (' + str(self.actual_turn) + ' turns)')
        elif self.pokemon2.current_hp <= 0 < self.pokemon1.current_hp:
            # Gana el pokemon 1
            print(self.pokemon1.name + ' wins! (' + str(self.actual_turn) + ' turns)')
        else:
            # Doble KO
            print('Double KO!')


class Pokemon:
    def __init__(self, name, level, type1, type2):
        self.name = name
        self.level = level
        self.type1 = type1
        self.type2 = type2
        self.attacks = list()           # vector de ataques (los pokemons tienen 4 ataques)
        self.stats = dict()             # ataque, defensa, ataque especial, defensa especial
        self.current_status = 0         # sano, envenenado, paralizado...
        self.current_hp = 0             # health points (puntos de vida)


class Attack:
    def __init__(self, name, t, category, pp, power, accuracy):
        self.name = name
        self.type = t
        self.category = category
        self.pp = pp
        self.power = power
        self.accuracy = accuracy


class Turn:
    def __init__(self):
        self.command1 = None
        self.command2 = None

    def permission_to_start(self):
        return self.command1 is not None and self.command2 is not None


class Command:
    def __init__(self, action):
        self.action = action

