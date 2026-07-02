class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.set_height(height)
        self.set_age(age)
    print("=== Garden Plant Output ===")

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


if __name__ == "__main__":
    main()
