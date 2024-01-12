
class Item:
    item_type = ""

    def __init__(self, name: str, cost: int, damage: int, armor: int) -> None:
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor

class Weapon(Item):
    item_type = "Weapon"

    def __init__(self, name: int, cost: int, damage: int) -> None:
        super().__init__(name, cost, damage, 0)


class Armor(Item):
    item_type = "Armor"

    def __init__(self, name: int, cost: int, armor: int) -> None:
        super().__init__(name, cost, 0, armor)


class Ring(Item):
    item_type = "Ring"

    def __init__(self, name: str, cost: int, damage: int, armor: int) -> None:
        super().__init__(name, cost, damage, armor)


class Character:
    def __init__(self, hp: int, damage: int = 0, armor: int = 0) -> None:
        self.hp = hp
        self.damage = damage
        self.armor = armor

    def get_armor(self):
        return self.armor

    def attack(self, target):
        damage = self.damage - target.armor
        target.hp -= max(damage, 1)


class Player(Character):
    def __init__(self, hp: int) -> None:
        super().__init__(hp)
        self.item_weapon: Weapon = None
        self.item_armor: Armor = None
        self.item_rings: list[Ring] = []


    def attack(self, target):
        return super().attack(target)
    
    def equip(self, item: Item):
        if item.item_type == "Weapon":
            self.item_weapon = item
            self.damage = self.__get_damage()
        
        if item.item_type == "Armor":
            self.item_armor = item
            self.armor = self.__get_armor()

        if item.item_type == "Ring":
            self.item_rings.append(item)
            self.damage = self.__get_damage()
            self.armor = self.__get_armor()

    def get_gold_spend(self):
        gold_spend = 0
        if self.item_weapon != None:
            gold_spend += self.item_weapon.cost
        if self.item_armor != None:
            gold_spend += self.item_armor.cost
        for ring in self.item_rings:
            gold_spend += ring.cost

        return gold_spend
    
    def __get_damage(self):
        damage = 0
        if self.item_weapon != None:
            damage += self.item_weapon.damage
        for ring in self.item_rings:
            damage += ring.damage
        return damage

    def __get_armor(self):
        armor = 0
        if self.item_armor != None:
            armor += self.item_armor.armor
        for ring in self.item_rings:
            armor += ring.armor
        return armor

class Boss(Character):
    def __init__(self, damage: int, armor: int, hp:int) -> None:
        super().__init__(hp)
        self.damage = damage
        self.armor = armor


class Battle:
    __is_player_turn = True

    def __init__(self, player: Player, boss: Boss) -> None:
        self.player = player
        self.boss = boss

    def fight(self):
        while self.boss.hp > 0 and self.player.hp > 0:
            if self.__is_player_turn:
                self.player.attack(self.boss)
            else:
                self.boss.attack(self.player)
            self.__is_player_turn = not self.__is_player_turn
        
        did_player_win = self.player.hp > 0
        # print(f"Player wins! hp={self.player.hp};{self.boss.hp}" if did_player_win  else f"Boss wins! hp={self.boss.hp};{self.player.hp}")
        return did_player_win

    def getStatus(self):
        print(self.player.hp, self.boss.hp)

dagger = Weapon("Dagger", 8, 4)
short_sword = Weapon("Shortsword", 10, 5)
war_hammer = Weapon("Warhammer", 25, 6)
long_sword = Weapon("Longsword", 40, 7)
great_axe = Weapon("Greataxe", 74, 8)

weapons = [dagger, short_sword, war_hammer, long_sword, great_axe]

leather = Armor("Leather", 13, 1)
chain_mail = Armor("Chainmail", 31, 2)
splint_mail = Armor("Splintmail", 53, 3)
banded_mail = Armor("Bandedmail", 75, 4)
plate_mail = Armor("Platemail", 102, 5)

armors = [leather, chain_mail, splint_mail, banded_mail, plate_mail]

damage_ring_1 = Ring("Damage +1", 25, 1, 0)
damage_ring_2 = Ring("Damage +2", 50, 2, 0)
damage_ring_3 = Ring("Damage +3", 100, 3, 0)

defense_ring_1 = Ring("Defense +1", 20, 0, 1)
defense_ring_2 = Ring("Defense +2", 40, 0, 2)
defense_ring_3 = Ring("Defense +3", 80, 0, 3)

rings = [damage_ring_1, damage_ring_2, damage_ring_3, defense_ring_1, defense_ring_2, defense_ring_3]

best = 100000000


def boss_factory():
    return Boss(8, 2, 109)


def prepare_battle(equipment: list[Item]):
    battle = Battle(Player(100), boss_factory()) 
    for item in equipment:
        battle.player.equip(item)
    
    return battle, battle.player

test_battle = Battle(Character(100, 5, 5), boss_factory())
test_battle.fight()

for weapon in weapons:
    # No rings just armor
    for armor in armors:
        battle, player = prepare_battle([weapon, armor])

        if battle.fight():
            best = min(player.get_gold_spend(), best)
        
        # with 1 ring
        for ring in rings:
            battle, player = prepare_battle([weapon, armor, ring])

            if battle.fight():
                best = min(player.get_gold_spend(), best)

            # with 2 rings
            for ring2 in rings:
                if ring.name == ring2.name:
                    continue
                battle, player = prepare_battle([weapon, armor, ring, ring2])

                if battle.fight():
                    best = min(player.get_gold_spend(), best)

    # with 1 ring
    for ring in rings:
        battle, player = prepare_battle([weapon, ring])

        if battle.fight():
            best = min(player.get_gold_spend(), best)

    for ring1 in rings:
        for ring2 in rings:
            if ring1.name == ring2.name:
                continue

            battle, player = prepare_battle([weapon, ring1, ring2])

            if battle.fight():
                best = min(player.get_gold_spend(), best)

print(best)

best = 0
for weapon in weapons:
    # No rings just armor
    for armor in armors:
        battle, player = prepare_battle([weapon, armor])

        if not battle.fight():
            best = max(player.get_gold_spend(), best)
        
        # with 1 ring
        for ring in rings:
            battle, player = prepare_battle([weapon, armor, ring])

            if not battle.fight():
                best = max(player.get_gold_spend(), best)

            # with 2 rings
            for ring2 in rings:
                if ring.name == ring2.name:
                    continue
                battle, player = prepare_battle([weapon, armor, ring, ring2])

                if not battle.fight():
                    best = max(player.get_gold_spend(), best)

    # with 1 ring
    for ring in rings:
        battle, player = prepare_battle([weapon, ring])

        if not battle.fight():
            best = max(player.get_gold_spend(), best)

    for ring1 in rings:
        for ring2 in rings:
            if ring1.name == ring2.name:
                continue

            battle, player = prepare_battle([weapon, ring1, ring2])

            if not battle.fight():
                best = max(player.get_gold_spend(), best)

print(best)
