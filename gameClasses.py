import random


class Monster(object):
    def __init__(self, name, description, attack, dmg_res, health, lvl):
        self.name = name
        self.description = description
        self.attack = attack
        self.dmg_res = dmg_res
        self.health = random.randrange(health[0], health[1])
        self.lvl = lvl
        self.max_health = self.health

    def Attack(self, dmg_res):
        dmg = random.randrange(self.attack[0], self.attack[1])
        return int((dmg / 100) * (100 - dmg_res))

    def health_check(self):
        if self.health/self.max_health >= 0.75:
            return f"The {self.name} isn't showing much damage."
        elif 0.75 > self.health/self.max_health >= 0.50:
            return f"The {self.name} is looking a little bloodied."
        elif 0.50 > self.health/self.max_health >= 0.25:
            return f"The {self.name} is getting pretty bloodied."
        elif 0.25 > self.health/self.max_health >= 0.05:
            return f"The {self.name} is not going to last much longer."


class Character(object):
    def __init__(self, name='', attack={'st': [0, 70], 'sl': [0, 70], 'sp': [10, 60], }, dmg_res=0, description=None, health=200, lvl=1, inventory=None, armor=None, weapon=None):
        self.name = name
        self.description = description
        self.attack = attack
        self.dmg_res = dmg_res
        self.health = health
        self.lvl = lvl
        self.inventory = inventory
        self.armor = armor
        self.weapon = weapon
        self.max_health = health

    def reName(self, new_name):
        self.name = new_name

    def Attack(self, atk_type, dmg_res):
        dmg = random.randrange(
            self.attack[atk_type][0], self.attack[atk_type][1])
        return int((dmg / 100) * (100 - dmg_res[atk_type]))

    def Heal(self, item=None, amount=None):
        if item is not None:
            self.health = min(self.max_health, self.health + item.healing)
        if amount in ['max', 'full']:
            self.health = self.max_health
        if amount is not None:
            self.health = min(self.max_health, self.health + amount)

    def Lvl_up(self):
        self.lvl += 1
        self.max_health += 50
        self.health = self.max_health
        self.dmg_res += 5
        for n in self.attack:
            self.attack[n][1] += 10

    def health_check(self):
        if self.health/self.max_health >= 0.75:
            return f"You're not showing much damage."
        elif 0.75 > self.health/self.max_health >= 0.50:
            return f"You're looking a little bloodied."
        elif 0.50 > self.health/self.max_health >= 0.25:
            return f"You're getting pretty bloodied."
        elif 0.25 > self.health/self.max_health >= 0.05:
            return f"You're not going to last much longer."

    def reset_all(self):
        self.__init__()

    def print_stats(self):
        print(f'{self.name = } {self.description = } {self.attack = } {self.dmg_res = } {self.health = } {self.lvl = } {self.inventory = } {self.armor = } {self.weapon = } {self.max_health = }')
