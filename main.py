
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        
    def is_alive(self):
        return self.health > 0
    
    def attack(self, target):
        target.health -= self.attack_power
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
        
class Player(Character):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)
        self.potions = 3
    
    def use_potion(self):
        if self.potions > 0:
            self.health += 20
            self.potions -= 1
            print(f"{self.name} uses a potion and heals 20 HP!")
        else:
            print("No potions left!")
        
def main():
    player_name = input("Enter your character name: ")
    player = Player(player_name, 100,15)
    enemy = Character("Goblin", 60, 10)
    
    
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
    elif enemy.is_alive() and not player.is_alive():
        print("\n 💀 You were defeated.")
        
main()