#!/usr/bin/env python3

class Plant:
    number_of_plants = 0

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age
        Plant.number_of_plants += 1


def ft_garden_data() -> list:
    return [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Papoila", 5, 90),
        Plant("Girassol", 80, 45),
        Plant("Fern", 15, 120),
        # Plant("Túlipa", 10, 50)
    ]


def ft_plant_factory(plants: list):
    print("=== Plant Factory Output ===")
    for i in plants:
        print(f"Created: {i.name} ({i.height}cm, {i.age} days)")
    print(f"\nTotal plants created: {Plant.number_of_plants}")


def main():
    plants = ft_garden_data()
    ft_plant_factory(plants)


if __name__ == "__main__":
    main()
