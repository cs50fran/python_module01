#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age_ = age

    def get_info(self):
        return (f"{self.name} ({self.get_type()}): "
                f"{self.height}cm, {self.age_} days old")

    def get_type(self):
        return "Generic Plant"


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def get_info(self):
        self.basic_info = super().get_info()
        return f"{self.basic_info}, {self.color} color"

    def get_type(self):
        return "Flower"


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def provide_shade(self):
        shade_area: int = self.height * self.trunk_diameter * 0.00312
        print(f"{self.name} provides {shade_area} square meters of shade!")

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, {self.trunk_diameter}cm diameter"

    def get_type(self):
        return "Tree"


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def nutritional_info(self):
        print(f"{self.name} is rich in {self.nutritional_value}")

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, {self.harvest_season} harvest"

    def get_type(self):
        return "Vegetable"


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print()
    rose = Flower("Rose", 25, 30, "red")
    print(rose.get_info())
    rose.bloom()
    print()
    oak = Tree("Oak", 500, 1825, 50)
    print(oak.get_info())
    oak.provide_shade()
    print()
    carrot = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    print(carrot.get_info())
    carrot.nutritional_info()
