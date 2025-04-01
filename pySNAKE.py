import random
import sys
import time

def loading_bar(duration=3, bar_length=25):
    print("\nLoading Game please wait...")
    for i in range(bar_length + 1):
        progress = "█" * i + "-" * (bar_length - i)
        percentage = int((i / bar_length) * 100)
        sys.stdout.write(f"\r[{progress}] {percentage}%")
        sys.stdout.flush()
        time.sleep(duration / bar_length)
    print("\nGame Loaded!\n")
    print("\n made by ekness\n")

# Run the loading bar before starting the game
loading_bar()
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

# Weapon Classes
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
            print(f"{self.name} fired! Ammo left: {self.ammo}")
            return self.damage
        else:
            print("Out of ammo!")
            return 0

    def reload(self, amount):
        self.ammo += amount
        print(f"{self.name} reloaded! Ammo: {self.ammo}")

class Chainsaw(Weapon):
    def __init__(self, name, damage, hp_gain):
        super().__init__(name, damage)
        self.hp_gain = hp_gain

    def attack(self, player):
        print(f"{self.name} slashes! Deals {self.damage} damage.")
        player.hp += self.hp_gain
        print(f"{player.name} regained {self.hp_gain} HP! Total HP: {player.hp}")
        return self.damage

class ThunderPunch(Weapon):
    def __init__(self, name, damage, cooldown=2):
        super().__init__(name, damage)
        self.cooldown = cooldown
        self.current_cooldown = 0
        self.base_damage = damage  

    def attack(self, player):
        if self.current_cooldown > 0:
            print("Thunder Punch is on cooldown!")
            return 0

        if random.randint(1, 10) == 1:  # 10% chance critical hit
            print("Critical hit! Massive damage and HP restored!")
            damage_dealt = 80
            hp_gain = 50
        else:
            damage_dealt = self.base_damage
            hp_gain = 10

        player.hp += hp_gain
        print(f"{player.name} regained {hp_gain} HP! Total HP: {player.hp}")

        self.current_cooldown = self.cooldown
        return damage_dealt

    def reduce_cooldown(self):
        if self.current_cooldown > 0:
            self.current_cooldown -= 1

# Player Class
class Player:
    def __init__(self, name, difficulty, weapon1, weapon2, melee):
        self.name = name
        self.hp = difficulty.player_hp
        self.armor = 50
        self.weapons = [weapon1, weapon2]
        self.melee = melee
        self.current_weapon = 0
        self.difficulty = difficulty

    def attack(self, enemy):
        weapon = self.weapons[self.current_weapon]
        if isinstance(weapon, Chainsaw):
            damage_dealt = weapon.attack(self)
        else:
            damage_dealt = weapon.attack()

        if damage_dealt > 0:
            enemy.take_damage(damage_dealt)

    def punch(self, enemy):
        damage_dealt = self.melee.attack(self)
        if damage_dealt > 0:
            enemy.take_damage(damage_dealt)

    def switch_weapon(self):
        self.current_weapon = (self.current_weapon + 1) % len(self.weapons)
        print(f"Switched to {self.weapons[self.current_weapon].name}")

    def reduce_cooldowns(self):
        self.melee.reduce_cooldown()

    def take_damage(self, amount):
        if self.armor > 0:
            absorbed = min(self.armor, amount)
            self.armor -= absorbed
            amount -= absorbed
            print(f"{self.name}'s armor absorbed {absorbed} damage!")
        
        self.hp -= amount
        print(f"{self.name} took {amount} damage! HP: {self.hp}")

# Enemy Class
class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def take_damage(self, amount):
        self.hp -= amount
        print(f"{self.name} took {amount} damage! HP left: {self.hp}")

    def attack(self, player):
        player.take_damage(self.damage)

# Boss Class (Stronger Enemies)
class Boss(Enemy):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp, damage)

# Function to create new enemies (normal and boss)
def create_enemy(round_number, difficulty):
    if round_number % 3 == 0:  # Every 3 rounds, spawn a boss
        return Boss(f"Cyberdemon (Round {round_number})", hp=200 + (round_number * 20), damage=difficulty.enemy_damage + (round_number * 5))
    else:
        return Enemy(f"Imp (Round {round_number})", hp=100 + (round_number * 10), damage=difficulty.enemy_damage + (round_number * 2))

# Create weapons
shotgun = RangedWeapon("Super-Shotgun", damage=40, ammo=4)
chainsaw = Chainsaw("Chainsaw", damage=38, hp_gain=47)
thunder_punch = ThunderPunch("Thunder Punch", damage=15 ,)

# Get User Input for choosing the skill level
difficulty_input = input("Choose skill level: I'm too young to die, Bring it on!, Ultra-Violence\n").lower()

if "young" in difficulty_input:
    chosen_difficulty = easy
elif "bring" in difficulty_input:
    chosen_difficulty = normal
elif "ultra" in difficulty_input:
    chosen_difficulty = hard
else:
    print("Invalid choice, defaulting to Normal mode.")
    chosen_difficulty = normal

# Create Player
player = Player("Alice", chosen_difficulty, shotgun, chainsaw, thunder_punch)

print(f"\nStarting game on {player.difficulty.name} mode with a {player.weapons[player.current_weapon].name}!\n")

# Game Loop (Endless Mode with Boss Fights)
round_number = 1  
while player.hp > 0:
    enemy = create_enemy(round_number, chosen_difficulty)  
    print(f"\nA {enemy.name} has appeared! HP: {enemy.hp}, Damage: {enemy.damage}\n")

    while enemy.hp > 0 and player.hp > 0:
        action = input("Do you want to attack, punch, switch weapon, or wait? (attack/punch/switch/wait): ").lower()
                                
        if action == "attack":
            player.attack(enemy)
            if enemy.hp > 0:
                enemy.attack(player)
        elif action == "punch":
            player.punch(enemy)
            if enemy.hp > 0:
                enemy.attack(player)
        elif action == "switch":
            player.switch_weapon()
        else:
            print("You waited...WAIT U GETT-.")

        player.reduce_cooldowns()

        if player.hp <= 0:
            print("\nGame Over! You fought bravely but couldn't survive.")
            break
        elif enemy.hp <= 0:
            print(f"\nYou defeated {enemy.name}!")
            round_number += 1  
