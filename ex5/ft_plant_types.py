class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.set_height(height)
        self.set_age(age)
    print("\n=== Garden Plant Output ===")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_age(self, new_age: int) -> None:
        if new_age <= 0:
            raise ValueError(f"Age Rejected {new_age}: Enter Valid Age")
        else:
            self._age = new_age

    def set_height(self, new_height: float) -> None:
        if new_height <= 0:
            raise ValueError(
                f"{new_height} Rejected: Height can't"
                "be zero or negative"
                            )
        else:
            self._height = new_height

    def show(self) -> str:
        return f"{self.name}: {self.get_height()}cm {self.get_age()} days old"

    def grow(self) -> str:
        return self.show()


class Flower(Plant): 
    def __init__(self, name, height, age, Color :str) -> None: 
        self.Color = Color
        super().__init__(name, height, age)
        self._bloomed = False

    
    def bloom(self) -> None:
        self._bloomed = True


    def show(self) ->None: 
        print(super().show())
        print(f"Color : {self.Color}")
        if (self._bloomed):
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter :float):
        self.trunk_diameter = trunk_diameter
        super().__init__(name, height, age)

    def show(self) -> None:
        print(super().show())
        print(f"Trunk Diameter: {self.trunk_diameter}")
        
    def produce_shade(self) -> None:
        self
        print(f"Tree {self.name} now produces a shade of {self.get_height()}cm long and {self.trunk_diameter}cm wide.")
        


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season:str, nutritional_value: float):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self._nutritional_value = nutritional_value
    def show(self) -> None:
        print(super().show())
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")
    
    def grow(self) -> None:
        self._nutritional_value = self.get_age()
        growing = self.get_age() + super().
        print(self.grow())

        
def main() -> None:
    plants_data = [("Rose", 11, 11),
                   ("Sunflower", 80, 12),
                   ("Cactus", 15, 120),
                   ("Fern", 200, 344),
                   ("Shaljam", 14, 22)
                   ]

    plants = []
    for name, height, age in plants_data:
        try:
            new_plants = Plant(name, height, age)
            plants.append(new_plants)
            print(f"Created: {new_plants.grow()}")
        except ValueError as e:
            print(f"Fail to create {name} -> {e}")

    sunflower = plants[1]
    try:
        print("\n=== Trying to set new Height ===")
        sunflower.set_height(5)
        print(f"Sunflower Height updated: {sunflower.grow()}")
    except ValueError as e:
        print(f"Error occured --> {e}")
    print("\n=== Flower ===")
    flowers = Flower("Rosy", 22, 65, "red")
    flowers.show()
    print("\n[asking the rose to bloom]")
    flowers.bloom()
    flowers.show()
    print("\n=== Tree ===")
    trees = Tree("Oak", 11, 33, 2.5)
    trees.show()
    print("[asking the oak to produce shade]")
    trees.produce_shade()

    print("\n=== Vegetable===")
    vegetable = Vegetable("Tomato", 5, 10, "April", 0)
    vegetable.show()
    vegetable.set_age(20)
    print(f"[make {vegetable.name} grow and age for {vegetable.get_age()} days]")
    vegetable.grow()

if __name__ == "__main__":
    main()
