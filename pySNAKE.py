import random

# Difficulty Class
class Difficulty:
    def __init__(self, name, enemy_damage, player_hp):
        self.name = name
        self.enemy_damage = enemy_damage
        self.player_hp = player_hp

# Define Difficulty Levels
easy = Difficulty("I'm too young to die", enemy_damage=10, player_hp=100)
normal = Difficulty("Bring it on!", enemy_damage=20, player_hp=100)
hard = Difficulty("Ultra-Violence", enemy_damage=35, player_hp=100)

# Weapon Class
class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class RangedWeapon(Weapon):
    def __init__(self, name, damage, ammo):
        super().__init__(name, damage)
        self.ammo = ammo

    def attack(self):
        if self.ammo > 0:
            self.ammo -= 1
            print(f" {self.name} fired! Ammo left: {self.ammo}")
            return self.damage
        else:
            print(" Out of ammo!")
            return 0

    def reload(self, amount):
        self.ammo += amount
        print(f" {self.name} reloaded! Ammo: {self.ammo}")

# Chainsaw Class (Melee Weapon)
class Chainsaw(Weapon):
    def __init__(self, name, damage, hp_gain):
        super().__init__(name, damage)      
        self.hp_gain = hp_gain
    
    def attack(self, player):
        print(f" {self.name} slashes! Deals {self.damage} damage.")
        player.hp += self.hp_gain
        print(f" {player.name} regained {self.hp_gain} HP! Total HP: {player.hp}")
        return self.damage

# Player Class status
class Player:
    def __init__(self, name, difficulty, weapon1, weapon2):
        self.name = name
        self.hp = difficulty.player_hp #called difficulty level for the player hp
        self.armor = 50 #armor function
        self.weapons = [weapon1, weapon2]  # Store both weapons
        self.current_weapon = 0  # Start with first weapon
        self.difficulty = difficulty

    def take_damage(self, amount):
        damage_taken = max(0, amount - (self.armor * 0.2))
        self.hp -= damage_taken

    def attack(self, enemy):
        weapon = self.weapons[self.current_weapon]
        damage_dealt = weapon.attack(self) if isinstance(weapon, Chainsaw) else weapon.attack()
        
        if damage_dealt > 0:
            enemy.take_damage(damage_dealt)
            if enemy.hp <= 0:
                print(f" {enemy.name} is dead!")
                self.reload_on_kill()
    #weapon reload logic
    def reload_on_kill(self):
        weapon = self.weapons[self.current_weapon]
        if isinstance(weapon, RangedWeapon):
            ammo_gained = random.randint(1, 5)
            weapon.reload(ammo_gained)
            print(f" You looted {ammo_gained} ammo!")
        elif isinstance(weapon, Chainsaw):
            self.hp += 10
            print(f" Chainsaw kill! {self.name} gained 10 extra HP! HP: {self.hp}")

    #weapon switch logic
    def switch_weapon(self):
        self.current_weapon = 1 - self.current_weapon  # Toggle between 0 and 1
        print(f" Switched to {self.weapons[self.current_weapon].name}!")

# Enemy Class
class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def take_damage(self, amount):
        self.hp -= amount
        print(f" {self.name} took {amount} damage! HP left: {self.hp}")

    def attack(self, player):
        player.take_damage(self.damage)
        player.hp -= player.difficulty.enemy_damage
        print(f" {player.name} took {player.difficulty.enemy_damage} damage! HP: {player.hp}")

# Create weapons
shotgun = RangedWeapon("Shotgun", damage=25, ammo=3)
chainsaw = Chainsaw("Chainsaw", damage=30, hp_gain=44)

# Get User Input from choosing tthe skill level
difficulty_input = input("Choose skill level: I'm too young to die, Bring it on!, Ultra-Violence\n").lower()

# Match the input to a difficulty level
if "young" in difficulty_input:
    chosen_difficulty = easy
elif "bring" in difficulty_input:
    chosen_difficulty = normal
elif "ultra" in difficulty_input:
    chosen_difficulty = hard
else:
    print("Invalid choice, defaulting to Normal mode.")
    chosen_difficulty = normal

# Create Player & Enemy
player = Player("Alice", chosen_difficulty, shotgun, chainsaw)

print(f"\nStarting game on {player.difficulty.name} mode with a {player.weapons[player.current_weapon].name}!\n")

# Game Loop
def gameLoop(lastEnemyLevel):
    enemy = Enemy("Demon", hp=100 + 10 * lastEnemyLevel, damage=10 + 4 * lastEnemyLevel)
    while enemy.hp > 0 and player.hp > 0:
        action = input("Do you want to attack, switch weapon, or wait? (attack/switch/wait): ").lower()

        if action == "attack":
            player.attack(enemy)
            if enemy.hp > 0:
                enemy.attack(player)
        elif action == "switch":
            player.switch_weapon()
        else:
            print("You waited...The enemy is still there.")

        if player.hp <= 0:
            print(" You died!")
            print(f"You survived {lastEnemyLevel} levels!")
            break
        elif enemy.hp <= 0:
            print(" You defeated the enemy!")
    
    if player.hp > 0:
        print("You encounter another enemy!")
        gameLoop(lastEnemyLevel + 1)
        
gameLoop(0)
