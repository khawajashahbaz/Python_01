class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
    print("=== Garden Plant Output ===")

    def show(self) -> str:
        return f"{self.name}: {self.height}cm {self.age} days old"

    def grow(self) -> str:
        self.age += 1
        self.height += 0.8
        return self.show()


def main() -> None:
    plants = [Plant("Rose", 25, 30),
              Plant("Sunflower", 80, 45),
              Plant("Cactus", 15, 120),
              Plant("Fern", 200, 344),
              Plant("Shaljam", 14, 22)
              ]
    for i in range(0, 5):
        print(f"Created: {plants[i].grow()}")


if __name__ == "__main__":
    main()
