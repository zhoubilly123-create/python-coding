import random
print("This is a dnd game")
enemy_health = 100
enemy_damage = 10

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
        self.damage = random.randint(40,45)
        self.health = random.randint(50,60)
        self.heal = 22

choice = input("what class do you want. ")
if choice == "Brawler".strip().lower():
    player = Brawler()
if choice == "Mage".strip().lower():
    player = Mage()
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
        player.health -= enemy_damage
        print(f"The enemy did {enemy_damage} to you and your hp is now {player.health}")
    