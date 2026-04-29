import random

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        
    def is_alive(self):
        return self.health > 0
    

    def attack(self, target):
        damage = random.randint(max(1, self.attack_power - 5), self.attack_power)
        
        # 20% chance for critical hit
        if random.random() <0.2:
            damage *= 2
            print("💥 Critical Hit!")
            
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        
class Player(Character):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)
        self.potions = 3
        self.level = 1
        self.experience = 0
    
    def use_potion(self):
        if self.potions > 0:
            self.health = min(self.health + 20, 100)
            self.potions -= 1
            print(f"{self.name} uses a potion and heals 20 HP!")
        else:
            print("No potions left!")
            
    def gain_experience(self, amount):
        self.experience += amount
        print(f"{self.name} gained {amount} XP!")
        
        if self.experience >= 10:
            self.level += 1
            self.experience = 0
            self.attack_power += 2
            self.health = min(self.health + 10, 100)
            print(f"\n ")
            print (f"🌟 Level up! {self.name} is now level {self.level}!")
            print(f"\n ")
        
        
        
def main():
    player_name = input("Enter your character name: ")
    player = Player(player_name, 100,15)
    #enemy = Character("Goblin", 60, 10)
    enemies = [
        Character("Goblin", 60, 10),
        Character("Orc", 80, 12),
        Character("Skeleton", 50, 8)
    ]
    
    enemy = random.choice(enemies)
    
    
    print(f"\n Welcome to RPG Battle Game {player_name}!")
    print(f"\n ")
    print(f"{player.name} vs {enemy.name}")
    
    while player.is_alive() and enemy.is_alive():
        print("\nWhat would you like to do? Choose an action:")
        print("1. Attack")
        print("2. Use Potion")
        print("3. Quit")
        
        choice = input("Choose an option: ")
        
        print(f"\n ")
        
        if choice == "1":
            player.attack(enemy)
            
        elif choice == "2":
            player.use_potion()         
        
        elif choice == "3":
            print("You quit the game.")
            break
        
        else:
            print("Invalid choice. Try again. 1, 2 or 3")
            continue
        
        if enemy.is_alive():
            enemy.attack(player)
            
        print(f"\n{player.name} Health: {player.health} | Potions:{player.potions}")
        print(f"\n{enemy.name} Health: {enemy.health}")
    
    if player.is_alive() and not enemy.is_alive():
        print("\n 🎉 You defeated the enemy!")
        player.gain_experience(10)
    elif enemy.is_alive() and not player.is_alive():
        print("\n 💀 You were defeated.")
        

        
main()