class Pet:
    def __init__(self, name: str, species: str, hunger: int, energy: int):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.energy = energy

whiskers = Pet("Whiskers", "cat", 6, 8)

# TODO: Print Whiskers' initial attributes
print("Initial Attributes: " + whiskers.name + " (" + whiskers.species + ") - Hunger: "+ str(whiskers.hunger)+", Energy: "+str(whiskers.energy) )
# TODO: Modify Whiskers' attributes:
#  - Decrease hunger by 3
whiskers.hunger -= 3
#  - Increase energy by 2
whiskers.energy += 2
# TODO: Print Whiskers' modified attributes
print("Modified Attributes: " + whiskers.name + " (" + whiskers.species + ") - Hunger: "+ str(whiskers.hunger)+", Energy: "+str(whiskers.energy) )
