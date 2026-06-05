import random
print("This is a dnd game\n")
print("This is also my first project \n")
username = input("----What is your name?----\n ")
answer = input(f"Nice to meet you {username} are you ready to get started on your journey?")
if answer == "Yes".strip().lower():
    print("Let's get started")
else:
    print("Too bad")
class Brawler():
    def __init__(self):
        self.name = username
        self.damage = random.randint(20,25)
        self.health = random.randint(110,120)

class Mage():
    def __init__(self):
        self.name = username
        self.damage = random.randint(30,35)
        self.health = random.randint(50,60)

class Archer():
    def __init__(self):
        self.name = username
        self.damage = random.randint(40,45)
        self.health = random.randint(80,100)

class Test():
    def __init__(self):
        self.name = username
        self.damage = random.randint(1000,1000)
        self.health = random.randint(8000,10000)
        self.heal = 22

choice = input("what class do you want. ")
if choice == "Brawler".strip().lower():
    player = Brawler()
if choice == "Mage".strip().lower():
    player = Mage()
if choice == "Archer".strip().lower():
    player = Archer()
if choice == "Test".strip().lower():
    player = Test()


class enemy():
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
enemy_enemy = random.randint(1,5)
if enemy_enemy == 1:
    current_enemy = enemy("Goblin", 80, 10)
elif enemy_enemy == 2:
    current_enemy = enemy("Knight", 120, 15)
elif enemy_enemy == 3:
    current_enemy = enemy("Adam", 150, 12)


print("you entered the castle.")
while True:
    print(f"{current_enemy} has appeared")
    while current_enemy.health > 0:
        enemy_action = random.randint(2,3)
        action = input("Actions: Attack, Heal, Flee \n" )
        if action == "Attack".strip().lower():
            current_enemy.health -= player.damage
            print(f"You did {player.damage} now the enemy has {current_enemy.health} ")
        if action == "Heal".strip().lower():
            player.health += player.heal
            print(f"You healed for {player.heal}. Your current health is {player.health}")
        if enemy_action <= 2:
            player.health -= current_enemy.damage
            print(f"The enemy did {current_enemy.damage} to you and your hp is now {player.health}")
        if current_enemy.health <= 0:
            print("You defeated the enemy")
            break
        if player.health == 0:
            print(f"Stand proud {player.name} you are strong")
            break

