# class Items:
#     def __init__(self):
#         pass
#
#
# class Entity:
#     def __init__(self, hp, name):
#         self.hp = hp
#         self.armor = 0
#         self.weapon = None
#         self.location = None
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#
# class Ability:
#     def __init__(self, name, dmg):
#         self.name = name
#         self.dmg = dmg
#
#
# class Monster(Entity):
#     def __init__(self, hp, name, ability):
#         Entity.__init__(self, hp, name)
#         self.ability = ability
#         self.is_alive = True
#
#     def generate_loot(self):
#         pass
#
#
# class Player(Entity):
#     def __init__(self, hp):
#         Entity.__init__(self, hp)
#
#
# fire_breath = Ability('Breath of Fire', 20)
# mnstr = Monster(100, 'Trogdor the Burninator', fire_breath)
#
# print(mnstr.ability.dmg)
# print(mnstr.ability.name)
#


def greeting():
    counter = 0
    while counter < 5:
        q = input('Give me a name!!11!: ')
        counter += 1
        yield q

for x in greeting():
    print('Hello {}'.format(x))


