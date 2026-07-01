class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
    print("=== Garden Plant Growth ===")

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm {self.age} days old")

    def grow(self) -> None:
        print("=== Day 1 ===")
        temp_height = self.height
        self.show()
        for i in range(2, 8):
            print(f"=== Day {i} ===")
            self.age += 1
            if (self.name.capitalize() == "Rose"):
                self.height += 0.8
            if (self.name.capitalize() == "Sunflower"):
                self.height += 0.6
            if (self.name.capitalize() == "Cactus"):
                self.height += 1
                self.height = round(self.height, 2)
            self.show()
        updated_height = self.height + 0.8
        round(updated_height)
        print(f"Growth this week: {round(updated_height - temp_height) }cm")


plant1 = Plant("Rose", 25, 30)
plant2 = Plant("Sunflower", 80, 45)
plant3 = Plant("Cactus", 15, 120)

if __name__ == "__main__":
    plant2.grow()
