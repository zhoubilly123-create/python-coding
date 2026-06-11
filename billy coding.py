import random
print("This is a dnd game\n")
print("This is also my first project \n")
username = input("----What is your name?----\n ")
answer = input(f"Nice to meet you {username} are you ready to get started on your journey?")
if answer == "Yes".strip().lower():
    print("Let's get started")
else:
    print("Too bad")
level = 0
Area = ["Forest, Dungeon, Cave"]



class Default():
    def __init__(self, classes, damage, health, heal):
        self.name = username
        self.classes = classes
        self.damage = damage
        self.health = health
        self.heal = heal

def attack():
    current_enemy.health -= player.damage
    print(f"You did {player.damage} to {current_enemy.health}")

def heal():
    player.health += player.heal
    print(f"you healed for {player.heal}, and your current hp is {player.health}")

        
choice = input("what class do you want. ")
if choice == "Brawler".strip().lower():
    player = Default("Brawler", 25, 120, 8)
if choice == "Mage".strip().lower():
    player = Default("Mage", 30, 80, 8)
if choice == "Archer".strip().lower():
    player = Default("Archer", 10, 200, 13)
if choice == "Bard".strip().lower():
    player = Default("Bard", 5, 100, 20)


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


print("You entered the caste")
while player.health > 0:
    decision = input("Where do you want to go next? Options: Continue, Forest, Desert ")
    if decision.strip().lower() == "Continue":
        while current_enemy.health > 0:
            enemy_action = random.randint(1,3)
            print(f"{current_enemy.name} has appeared")
            action = input("Actions: Attack, Heal, Flee \n" )
            if action == "Attack".strip().lower():
                attack()
            elif action == "Heal".strip().lower():
                player.health += player.heal
                print(f"You healed for {player.heal}. Your current health is {player.health}")
            if enemy_action <= 2:
                player.health -= current_enemy.damage
                print(f"The enemy did {current_enemy.damage} to you and your hp is now {player.health}")
            elif enemy_action == 2:
                current_enemy.health += current_enemy.heal
                print(f"{current_enemy.name} has healed for {current_enemy.heal} and now its hp is {current_enemy.health}")
            if current_enemy.health <= 0:
                print("You defeated the enemy")
                level += 1
                print(f"{player.name} is now level {level}")
                reward = input("The ")
                break
    
       

