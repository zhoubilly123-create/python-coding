import random
print("This is a dnd game")
enemy_health = 100
enemy_damage = 10
username = input("What is your name? ")
class Brawler():
    def __init__(self):
        self.name = username
        self.damage = random.randint(30,40)
        self.health = random.randint(110,120)
choice = input("what class do you want. ")
if choice == "Brawler".strip().lower():
    player = Brawler()
print("you entered the castle. An enemy has appeared")
while True:
    action = input("Actions: Attack, Heal, Flee \n" )
    if action == "Attack".strip().lower():
        enemy_health -= player.damage
        print(f"You did {player.damage} now the enemy has {enemy_health} ")
        break
    