from __future__ import annotations
from typing import Callable

class Spell():
    def __init__(self, spell_type: str) -> None:
        self.spell_type = spell_type

class DamageSpell(Spell):
    def __init__(self, name: str, mana_cost: int, damage: int = 0, heal: int = 0) -> None:
        super().__init__("damage")
        self.name = name
        self.mana_cost = mana_cost
        self.damage = damage
        self.heal = heal

class EffectSpell(Spell):
    def __init__(self, name: str, mana_cost: int, duration: int, damage: int = 0, armor: int  = 0, mana: int = 0) -> None:
        super().__init__("effect")
        self.name = name
        self.mana_cost = mana_cost
        self.duration = duration
        self.damage = damage
        self.armor = armor
        self.mana = mana

    def copy(self):
        return EffectSpell(self.name, self.mana_cost, self.duration, self.damage, self.armor, self.mana)

def magic_missile(): return DamageSpell("Magic Missile", 53, 4)
def drain(): return DamageSpell("Drain", 72, 2, 2)
def shield(): return EffectSpell("Shield", 113, 6, armor=7)
def poison(): return EffectSpell("Poison", 173, 6, damage=3)
def recharge(): return EffectSpell("Recharge", 229, 5, mana=101)

def get_effects(): return [ shield(), poison(), recharge() ]

class Character:
    def __init__(self, hp: int, damage: int = 0, armor: int = 0, mana: int = 0) -> None:
        self.hp = hp
        self.damage = damage
        self.armor = armor
        self.mana = mana
    
class Player(Character):
    def __init__(self, hp: int, mana: int) -> None:
        super().__init__(hp)
        self.mana = mana
        self.armor = 0
        self.mana_spent = 0

    def cast_damage_spell(self, target: Boss, spell: DamageSpell) -> int:
        target.hp -= max(spell.damage, 1)
        self.hp += spell.heal
        self.mana -= spell.mana_cost
        self.mana_spent += spell.mana_cost
        return spell.mana_cost

    def cast_effect_spell(self, spell: EffectSpell) -> int:
        self.mana -= spell.mana_cost
        self.armor += spell.armor
        self.mana_spent += spell.mana_cost
        return spell.mana_cost

    def get_armor(self):
        return self.armor
    
    def copy(self):
        new_player = Player(self.hp, self.mana)
        new_player.mana_spent = self.mana_spent
        new_player.armor = self.armor
        return new_player

class Boss(Character):
    def __init__(self, hp:int, damage: int) -> None:
        super().__init__(hp)
        self.damage = damage

    def attack(self, target: Player):
        damage = self.damage - target.get_armor()
        target.hp -= max(damage, 1)

    def copy(self):
        new_boss = Boss(self.hp, self.damage)
        return new_boss

class GameStatus:
    def __init__(self, player: Player, boss: Boss, is_hard: bool = False, is_player_turn: bool = True, effects: set[EffectSpell] = set()) -> None:
        self.player = player
        self.boss = boss
        self.spells = []
        self.__is_player_turn = is_player_turn
        self.__is_hard = is_hard
        self.__effects: set[EffectSpell] = effects

    def boss_move(self):
        return self.__move(lambda player, _: self.boss.attack(player))

    def tick(self, spell: Spell):
        self.player_move(spell)
        self.boss_move()
    
    def player_move(self, spell: Spell):
        move: Callable[[Player, Boss], int] = None
        if self.__is_hard:
            self.player.hp -= 1
        if spell.spell_type == "damage":
            def deal_damage(player: Player, boss: Boss):
                return player.cast_damage_spell(boss, spell)
            move = deal_damage
        if spell.spell_type == "effect":
            def cast_spell(player: Player, boss: Boss):
                self.__effects.add(spell)
                return player.cast_effect_spell(spell)
            move = cast_spell
        self.spells.append(spell.name)
        return self.__move(move)
    
    def cast_effect_spell(self, player_move: Callable[[Player, Boss], None]):
        return self.__move(player_move)

    def __move(self, action: Callable[[Player, Boss], int]):
        self.__is_player_turn = not self.__is_player_turn
        self.__process_effects()
        if not self.can_continue():
            return 0
        mana_const = action(self.player, self.boss)
        return mana_const

    def can_continue(self):
        return self.player.hp > 0 and self.boss.hp > 0 and self.player.mana > 0
    
    def did_player_win(self):
        return self.player.hp > 0 and self.player.mana > 0
    
    def get_winner(self):
        if self.player.hp <= 0 or self.player.mana <= 0:
            return self.boss
        if self.boss.hp <= 0:
            return self.player
        
        return None

    def is_player_turn(self):
        return self.__is_player_turn
    
    def can_cast(self, spell: Spell):
        if spell.spell_type == "damage":
            return True
        if spell.name in self.__get_effects_after_turn():
            return False
        
        return True
    
    def get_possible_effects_to_cast(self) -> list[EffectSpell]:
        effects_to_cast = []
        for effect in get_effects():
            if effect.name not in self.__get_effects_after_turn(): 
                effects_to_cast.append(effect)

        return effects_to_cast
    
    def get_possible_spells_to_cast(self):
        spells_to_cast = self.get_possible_effects_to_cast()
        spells_to_cast.append(magic_missile())
        spells_to_cast.append(drain())
        return spells_to_cast
    
    def __get_effects_after_turn(self) -> list[str]:
        effects = filter(lambda effect: effect.duration > 1, self.__effects)
        effects = map(lambda x: x.name, effects)
        
        return list(effects)

    def printStatus(self):
        self.__printStatus()
    
    def __printStatus(self):
        print(f"Player: hp = {self.player.hp}, armor = {self.player.armor} mana = {self.player.mana}, Boss :hp = {self.boss.hp}")

    def __process_effects(self):
        for effect in self.__effects:
            self.player.mana += effect.mana
            self.boss.hp -= effect.damage
            effect.duration -= 1

        expired_effects = list(filter(lambda x: x.duration == 0, self.__effects))
        for expired_effect in expired_effects:
            self.player.armor -= expired_effect.armor
            if self.player.armor == -7:
                pass
            self.__effects.remove(expired_effect)

    def copy(self):
        effects = set()
        for effect in self.__effects:
            effects.add(effect.copy())

        new_game = GameStatus(self.player.copy(), self.boss.copy(), self.__is_hard, self.__is_player_turn, effects)
        new_game.spells = self.spells.copy()
        return new_game

best_mana = 1_000_000

battle = GameStatus(Player(50, 500), Boss(71, 10))
games = [battle]

while len(games):
    game = games.pop()
    spells = game.get_possible_spells_to_cast()
    for spell in spells:
        next_game = game.copy()
        next_game.tick(spell)
        if next_game.can_continue() and best_mana > next_game.player.mana_spent:
            games.append(next_game)
            continue
        
        winner = next_game.get_winner()        
        if type(winner) == Player:
            best_mana = min(winner.mana_spent, best_mana)

print(best_mana)

best_mana = 1_000_000

battle = GameStatus(Player(50, 500), Boss(71, 10), True)
games = [battle]

while len(games):
    game = games.pop()
    spells = game.get_possible_spells_to_cast()
    for spell in spells:
        next_game = game.copy()
        next_game.tick(spell)
        if next_game.can_continue() and best_mana > next_game.player.mana_spent:
            games.append(next_game)
            continue
        
        winner = next_game.get_winner()        
        if type(winner) == Player:
            best_mana = min(winner.mana_spent, best_mana)

print(best_mana)