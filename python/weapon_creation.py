import math
import random

lvl = random.randrange(1, 10)
local_dict = {}


class Items:
    def __init__(self, name, type, effect, weight):
        self.name = name
        self.type = type
        self.effect = effect
        self.weight = weight

    def __str__(self):
        return 'Name: {} Type: {} Effect: {} Weight: {}'.format(self.name.title(), self.type.capitalize(), self.effect,
                                                                self.weight)

    def __repr__(self):
        return 'Name: {} Type: {} Effect: {} Weight: {}'.format(self.name.title(), self.type.capitalize(), self.effect,
                                                                self.weight)


basic_armor = ['Construction Chaps', 'Motorcycle Helmet', 'Leather Gloves', 'Welding Helmet']

common_armor = ['Kevlar Vest', 'Iron Chest Plate', 'Steel Toe Boots']

rare_armor = ['Bullet Proof Suit', 'Viking Helmet', 'Steel Chest Plate']

epic_armor = ['Titanium Cuffs', 'Mech Body Armor']

legendary_armor = ['Plasma shield', 'Obsidian Chest Plate']

basic_weapons = ['Baseball Bat', 'Crow Bar', 'Hunting Knife', 'Pepper Spray']

common_weapons = ['.22 Pistol', 'Pump Shotgun', 'Crossbow']

rare_weapons = ['AR-15', 'Elephant Gun', 'Hunting Rifle']

epic_weapons = ['Flamethrower', 'Rocket Launcher', 'Grenade Launcher']

legendary_weapons = ['Gatling Gun', 'Sword of Doom', 'Laser Rifle', 'Mech Cannon', 'MOAG (Mother of All Guns']

'''
Functions for creating our weapons
'''


def create_basic_weapon():
    return Items(random.choice(basic_weapons), 'basic weapon', random.randrange(1, 10) * lvl, random.randrange(1, 8))


def create_common_weapon():
    return Items(random.choice(common_weapons), 'common weapon', random.randrange(2, 10) * (lvl * 2),
                 random.randrange(1, 7))


def create_rare_weapon():
    return Items(random.choice(rare_weapons), 'rare weapon', random.randrange(3, 10) * (lvl * 2.5),
                 random.randrange(1, 6))


def create_epic_weapon():
    return Items(random.choice(epic_weapons), 'epic weapon', random.randrange(4, 10) * (lvl * 3),
                 random.randrange(1, 5))


def create_legendary_weapon():
    return Items(random.choice(legendary_weapons), 'legendary weapon', random.randrange(5, 10) * (lvl * 4),
                 random.randrange(1, 4))


'''
functions for creating certain levels and rarities of armor
'''


def create_basic_armor():
    return Items(random.choice(basic_armor), 'basic armor', random.randrange(1, 8), random.randrange(1, 10) * (lvl * 1))


def create_common_armor():
    return Items(random.choice(common_armor), 'common armor', random.randrange(2, 10) * (lvl * 2),
                 random.randrange(1, 7))


def create_rare_armor():
    return Items(random.choice(rare_armor), 'rare armor', random.randrange(2, 10) * (lvl * 2), random.randrange(1, 7))


def create_epic_armor():
    return Items(random.choice(epic_armor), 'epic armor', random.randrange(2, 10) * (lvl * 2), random.randrange(1, 7))


def create_legendary_armor():
    return Items(random.choice(legendary_armor), 'legendary armor', random.randrange(2, 10) * (lvl * 2),
                 random.randrange(1, 7))


def create_weapon():
    luck = random.randrange(1, 101)
    if luck in range(1, 50):
        return create_basic_weapon()
    elif luck in range(50, 75):
        return create_common_weapon()
    elif luck in range(75, 85):
        return create_rare_weapon()
    elif luck in range(85, 97):
        return create_epic_weapon()
        # else:
        #     luck in range(97, 101):
        #         return create_legendary_weapon()


def create_armor():
    luck = random.randrange(1, 101)
    if luck in range(1, 50):
        return create_basic_armor()
    elif luck in range(50, 75):
        return create_common_armor()
    elif luck in range(75, 85):
        return create_rare_armor()
    elif luck in range(85, 97):
        return create_epic_armor()
    else:
        if luck in range(97, 101):
            return create_legendary_armor()


'''
First aid function creates a random number and then generates a first aid based on the random number.
I made sure to give the random number a better chance of landing on something average, and
a very rare chance of landing on something rare
'''


def create_first_aid():
    random_number = random.triangular(1, 50, 20)
    aid_level = math.trunc(random_number)
    water_range = random.randrange(1, 5)
    bandages_range = random.randrange(5, 10)
    first_aid_kit_range = random.randrange(10, 15)
    antibiotics_range = random.randrange(15, 20)
    medical_pack_range = random.randrange(20, 25)
    greater_healing_potion_range = random.randrange(25, 30)
    nano_goo_range = random.randrange(30, 40)
    if aid_level in range(1, 4):
        return Items('nano goo', 'first aid', nano_goo_range * lvl, 0)
    elif aid_level in range(4, 8):
        return Items('greater healing potion', 'first aid', greater_healing_potion_range * lvl, 1)
    elif aid_level in range(8, 15):
        return Items('water', 'first aid', water_range * lvl, 1)
    elif aid_level in range(15, 35):
        return Items('bandages', 'first aid', bandages_range * lvl, 2)
    elif aid_level in range(35, 40):
        return Items('first aid kit', 'first aid', first_aid_kit_range * lvl, 3)
    elif aid_level in range(40, 47):
        return Items('antibiotics', 'first aid', antibiotics_range * lvl, 1)
    elif aid_level in range(47, 51):
        return Items('medical pack', 'first aid', medical_pack_range * lvl, 0)


class Inventory:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.coin = 0
        self.inv = self.create_inv()

    def console(self):
        print(self.inv)
        play_con = input("(U)se, (E)quip, or (D)rop an item").lower()
        if play_con == 'd':
            to_drop = input("which item do you want to drop?  ")
            self.inv[to_drop] = None
            print(inventory.inv)

    def create_inv(self, slots=15):
        dictionary = {}
        for i in range(1, slots + 1):
            dictionary[i] = None
        return dictionary

    def place_item(self, item):
        for k, v in self.inv.items():
            if v is None and self.weight - item.weight > 0:
                self.inv[k] = item
                self.weight -= item.weight
                break
            # elif v is not None:
            #     print("You're carrying too many things. You must drop something first.")
            # elif self.weight - item.weight < 0:
            #     print("You're carrying too much weight to pick that up.")



    def drop_item(self):
        print(inventory.inv)
        to_drop = input(int("which item do you want to drop?  "))
        self.inv[to_drop] = None

    def __str__(self):
        return self.inv



inventory = Inventory('player bags', 50)
print(inventory.inv)
wep = create_weapon()
inventory.place_item(wep)
print(inventory.inv)
Inventory.console()

if __name__ == '__main__':
    pass
