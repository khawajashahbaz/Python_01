#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: float, age_att: int):
        self._initialized = False
        self._name = name
        self._height = height
        self._age_att = age_att
        self._initial_height = height
        self._initialized = True

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_att

    def set_name(self, a: str) -> None:
        self._name = a

    def set_height(self, a: float) -> None:
        if a >= 0:
            self._height = a
            if self._initialized:
                print(f"Height updated: {a}cm")
        else:
            print("Error, height can't be negative. "
                  "Height update rejected")

    def set_age(self, a: int) -> None:
        if a >= 0:
            self._age_att = a
            if self._initialized:
                print(f"Age updated: {a} days")
        else:
            print("Error, age can't be negative. "
                  "Age update rejected")

    def grow(self) -> None:
        self._height += 0.2

    def age(self) -> None:
        self._age_att += 1

    def show(self) -> None:
        print(f"{self.get_name()}: {round(self.get_height(), 1)}cm, "
              f"{self.get_age()} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age_att: int, color: str):
        super().__init__(name, height, age_att)
        self._color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._bloomed:
            print(f"{self.get_name().capitalize()} is blooming beautifully!")
        else:
            print(f"{self.get_name().capitalize()} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age_att: int,
                 trunk_diameter: float):
        super().__init__(name, height, age_att)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.get_name()} now produces a shade of "
              f"{round(self.get_height(), 1)}cm long and "
              f"{round(self._trunk_diameter, 1)}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self._trunk_diameter, 1)} cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age_att: int,
                 harvest_season: str, nutritional_value: int):
        super().__init__(name, height, age_att)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 1

    def age(self) -> None:
        super().age()

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


def main() -> None:
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()

    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print("\n")

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("\n")

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April", 0)
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()


if __name__ == "__main__":
    main()
