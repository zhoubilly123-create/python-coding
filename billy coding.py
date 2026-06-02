import random
print("This is a dnd game")


username = input("What is your name? ")
class Brawler():
    def __init__(self):
        self.name = username
        self.damage = random.randint(20,25)
        self.health = random.randint(110,120)
        self.heal = 20
class Mage():
    def __init__(self):
        self.name = username
        self.damage = random.randint(30,35)
        self.health = random.randint(50,60)
        self.heal = 22
class Archer():
    def __init__(self):
        self.name = username
        self.damage = random.randint(40,45)
        self.health = random.randint(80,100)
        self.heal = 22


choice = input("what class do you want. ")
if choice == "Brawler".strip().lower():
    player = Brawler()
if choice == "Mage".strip().lower():
    player = Mage()

class enemy():
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
enemy_enemy = random.randint(1,5)
if enemy_enemy == 1:
    goblin = enemy("Goblin", 80, 10)
elif enemy_enemy == 2:
    knight = enemy("Knight", 120, 15)

print("you entered the castle. An enemy has appeared")
while True:
    enemy_action = random.randint(2,3)
    action = input("Actions: Attack, Heal, Flee \n" )
    if action == "Attack".strip().lower():
        enemy_health -= player.damage
        print(f"You did {player.damage} now the enemy has {enemy_health} ")
    if action == "Heal".strip().lower():
        player.health += player.heal
        print(f"You healed for {player.heal}. Your current health is {player.health}")
    if enemy_action <= 2:
        player.health -= damage
        print(f"The enemy did {damage} to you and your hp is now {player.health}")
    