class Kettle:
    def __init__(self, volume):
        self.volume = volume
        self.water_level = 0
    
    def fill_water(self, amount):
        if self.water_level + amount <= self.volume:
            self.water_level += amount
            print(f"Added {amount} ml of water to the kettle. Current water level: {self.water_level} ml")
        else:
            print("Cannot add water, kettle is full.")
    
    def boil(self):
        if self.water_level == self.volume:
            print("Boiling water...")
            self.water_level = 0
            print("Water is boiled, kettle is empty.")
        else:
            print("Cannot boil water, kettle is not full.")
    
class Stove:
    def __init__(self):
        pass

kettle = Kettle(1000)
stove = Stove()

kettle.fill_water(500)
kettle.boil()

kettle.fill_water(500)
kettle.boil()

# Модифицируем программу, чтобы она работала, когда чайник наполовину уже наполнен водой

class HalfFullKettle(Kettle):
    def __init__(self, volume, water_level):
        super().__init__(volume)
        self.water_level = water_level

half_full_kettle = HalfFullKettle(1000, 500)
half_full_kettle.boil()