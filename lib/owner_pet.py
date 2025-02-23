class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Return all pets belonging to this owner"""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Assign this owner to a pet if it's an instance of Pet"""
        if not isinstance(pet, Pet):
            raise Exception("Only Pet instances can be added")
        pet.owner = self  # Assign this owner to the pet

    def get_sorted_pets(self):
        """Return a list of pets sorted by name"""
        return sorted(self.pets(), key=lambda pet: pet.name)  # Sort by pet name


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner  # Assign owner if provided

        Pet.all.append(self)  # Store the pet in the all list
