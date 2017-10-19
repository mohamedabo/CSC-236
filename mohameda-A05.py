# Virtual Dog Program
# Stimulates a dog
# Created by: Abdirahman Mohamed CSC 236 (B)
class Dog:
     """Gets hungry then fed and bored then played with and after that the dog rests"""

     def __init__(self, name, hunger = 5, boredom = 0, tiredness = 0,life=5):
        print("How How!")
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        self.tiredness = tiredness
        self.life = life
     def __str__(self):
        """Manage inputs and its print statements."""
        att = "Feline friend\n"
        att += "Name: " + self.name + "\n"
        if self.hunger == "1":    #If hunger is 1
                print("Your pet is hungry.")
        elif self.boredom == "2":
                print("Your pet is bored.")
        elif self.tiredness == "3":
                print("Your pet is tired.")
        return att
     def __pass_time(self):
        """Counts hunger, boredom and tirdness"""
        self.hunger += 1  #Counts self hunger
        self.boredom += 1
        self.tiredness += 1
     def eat(self, food = 5):
        """The food of the dog"""
        print("Purrrr purrr!")
        self.hunger -= food
        if self.hunger < 0: #if it was less than a zero
            self.hunger = 0
            self.__pass_time()
     def play(self, fun = 5):
        """playing with the dog"""
        print("How hooooowwww!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
            self.__pass_time()
     def rest(self, sleep = 5):
        """It will make the dog rest"""
        print("...")
        self.tiredness -= sleep
        if self.tiredness < 0:
            self.tiredness = 0
            self.__pass_time()
class Death:
     """It will make the dog die"""
     def __init__(self,dehydration=5):
        self.dehydration = dehydration
def main():
    """Feed a dog, play with it and let it rest. But, it will die out of dehydration."""
    user_input = input("Enter an appropriate name for your dog:")
    pet = Dog(user_input)
    d = Death()
    choice = None
    while choice != "0":  #While the choice is not equal to zero
        print("What would you like to do? (Enter 1 to feed the dog, enter 2 to play with the dog, enter 3 to leave the dog to rest.")
        choice = input(">")
        if choice == "1":
            pet.eat()
            d.dehydration-=3 #Dehydration begins
            print(pet)
        elif choice == "2":
            pet.play()
            d.dehydration-=1
            print(pet)
        elif choice=="3":
            pet.rest()
            d.dehydration-=1
            print(pet)
            print("Your dog just died of dehydration:(")
            break

if __name__ == '__main__':
    main()
