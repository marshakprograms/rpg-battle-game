
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
        
def main():
    player = Character("Hero", 100,15)
    enemy = Character("Goblin", 60, 10)
    
    print("Welcome to RPG Battle Game!")
    print(f"\n ")
    print(f"{player.name} vs {enemy.name}")
    
    while player.is_alive() and enemy.is_alive():
        print("\nWhat would you like to do?")
        print("1. Attack")
        print("2. Quit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            player.attack(enemy)
            
            if enemy.is_alive():
                enemy.attack(player)
        
        elif choice == "2":
            print("You quit the game.")
            break
        
        else:
            print("Invalid choice.  Please choose 1 or 2.")
            
        print(f"\n{player.name} Health: {player.health}")
        print(f"\n{enemy.name} Health: {enemy.health}")
    
    if player.is_alive() and not enemy.is_alive():
        print("\nYou defeated the enemy!")
    elif enemy.is_alive() and not player.is_alive():
        print("\nYou were defeated.")
        
main()