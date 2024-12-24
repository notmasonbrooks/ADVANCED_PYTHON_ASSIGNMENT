# Base Character class
import random


class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit
        # self.special = special

    def attack(self, opponent):
        opponent.health -= self.attack_power
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(
            f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}"
        )

    def heal(self):
        if self.health < self.max_health:
            print(f"{self.name}'s health has been restored!")
            self.health = self.max_health
        else:
            print("Health regeneration cannot exceed max health.")


# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(
            name, health=140, attack_power=random.randrange(15, 35)
        )  # Boost health and attack power

    # Add your power attack method here
    def attack(self, opponent):
        print(
            f"{self.name} used Hammer Smash on {opponent.name} for {self.attack_power} damage."
        )
        return super().attack(opponent)

    def special(self):
        print(f"{self.name} used Dodge.")


# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(
            name, health=100, attack_power=random.randrange(20, 35)
        )  # Boost attack power

    # Add your cast spell method here
    def attack(self, opponent):
        print(
            f"{self.name} used Lightning Flash on {opponent.name} for {self.attack_power} damage."
        )
        return super().attack(opponent)

    def special(self):
        print(f"{self.name} used Deflect.")


class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=random.randrange(15, 30))

    def attack(self, opponent):
        print(
            f"{self.name} used Quick Shot on {opponent.name} for {self.attack_power} damage."
        )
        return super().attack(opponent)

    def special(self):
        print(f"{self.name} used Evade.")


class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=random.randrange(22, 35))

    def attack(self, opponent):
        print(
            f"{self.name} used Holy Strike on {opponent.name} for {self.attack_power} damage."
        )
        return super().attack(opponent)

    def special(self):
        print(f"{self.name} used Devine Shield.")


# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(
            name, health=150, attack_power=random.randrange(15, 20)
        )  # Lower attack power

    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5  # Lower regeneration amount
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

    def attack(self, opponent):
        print(
            f"{self.name} used Abracadabra on {opponent.name} for {self.attack_power} damage."
        )
        return super().attack(opponent)


# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")  # Add Archer
    print("4. Paladin")  # Add Paladin

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == "1":
        return Warrior(name)
    elif class_choice == "2":
        return Mage(name)
    elif class_choice == "3":
        return Archer(name)
    elif class_choice == "4":
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)


# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == "1":
            player.attack(wizard)
        elif choice == "2":
            player.special()
        elif choice == "3":
            player.heal()
        elif choice == "4":
            player.display_stats()
        else:
            print("Invalid choice, try again.")
            continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0 and choice != "2":
            wizard.attack(player)
            wizard.regenerate()
        else:
            print(f"{wizard.name} missed their attack...")
            wizard.regenerate()

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"{wizard.name} has been defeated by {player.name}!")


# Main function to handle the flow of the game
def main():
    # Character creation phase
    player = create_character()

    # Evil Wizard is created
    wizard = EvilWizard("The Dark Wizard")

    # Start the battle
    battle(player, wizard)


if __name__ == "__main__":
    main()
