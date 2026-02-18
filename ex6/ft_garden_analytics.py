class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> int:
        self.height += 1
        return 1

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm"

    def get_kind(self):
        return "regular"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm, {self.color} flowers (blooming)"

    def get_kind(self):
        return "flower"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int,
                 color: str, prize_points: int) -> None:
        super().__init__(name, height, age, color)
        self.prize_points = prize_points

    def __str__(self) -> str:
        return (f"{self.name}: {self.height}cm, {self.color} flowers "
                f"(blooming), Prize points: {self.prize_points}")

    def get_kind(self):
        return "prize"


class Garden:
    def __init__(self, name: str) -> None:
        self.name = name
        self.plants = []
        self.total_growth = 0
        self.added_count = 0

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        self.added_count += 1
        print(f"Added {plant.name} to {self.name}")

    def help_grow(self) -> None:
        print(f"\n{self.name} is helping all plants grow...")
        for plant in self.plants:
            growth = plant.grow()
            self.total_growth += growth
            print(f"{plant.name} grew {growth}cm")
        print()

    def report(self) -> None:
        print(f"=== {self.name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant}")
        print()
        print(f"Plants added: {self.added_count}, Total growth: "
              f"{self.total_growth}cm")

        regular_count = 0
        flowering_count = 0
        prize_count = 0

        for plant in self.plants:
            kind = plant.get_kind()
            if kind == "prize":
                prize_count += 1
            elif kind == "flower":
                flowering_count += 1
            else:
                regular_count += 1

        print(f"Types: {regular_count} regular, {flowering_count} flowering, "
              f"{prize_count} prize")

    def validate_heights(self) -> bool:
        result = True
        for p in self.plants:
            if p.height <= 0:
                result = False
            break
        print("Height validation test:", result)

    def garden_score(self) -> int:
        score = 0
        for plant in self.plants:
            score += plant.height
        for plant in self.plants:
            kind = plant.get_kind()
            if kind == "prize":
                score += plant.prize_points
        return score


class GardenManager:
    class GardenStats:
        @staticmethod
        def total_plants(gardens: list) -> int:
            total = 0
            for garden in gardens:
                for plant in garden.plants:
                    total += 1
            return total

        @staticmethod
        def average_garden_height(gardens: list) -> float:
            if not gardens:
                return 0
            total_height = 0
            count = 0
            for garden in gardens:
                if garden.plants:
                    garden_height = 0
                    for plant in garden.plants:
                        garden_height += plant.height
                    total_height += garden_height
                    count += 1
            if count == 0:
                return 0
            return total_height / count

        @staticmethod
        def gardens_score(gardens: list) -> int:
            for garden in gardens:
                print(f"Garden Score - {garden.name}:"
                      f"{garden.garden_score()}")

    def __init__(self) -> None:
        self.gardens = []

    def add_garden(self, garden: Garden) -> None:
        self.gardens.append(garden)

    def create_garden_network(self, names: list) -> "GardenManager":
        for name in names:
            self.add_garden(Garden(name))
        return self

    @classmethod
    def from_names(cls, names: list) -> "GardenManager":
        """Create a new GardenManager and populate gardens from given names."""
        manager = cls()
        for name in names:
            manager.add_garden(Garden(name))
        return manager

    @staticmethod
    def utility_garden_tip() -> str:
        return "Water plants in the morning."

    def show_total_gardens(self) -> None:
        count = 0
        for _ in self.gardens:
            count += 1
        print(f"Total gardens: {count}")

    @staticmethod
    def gardens_managed(gardens: list) -> int:
        count = 0
        for _ in gardens:
            count += 1
        return count


def ft_garden_analytics() -> None:
    alice_garden = Garden("Alice")
    bob_garden = Garden("Bob")

    oak = Plant("Oak Tree", 100, 365)
    rose = FloweringPlant("Rose", 25, 30, "red")
    sunflower = PrizeFlower("Sunflower", 50, 60, "yellow", 10)
    # Regular plants
    # cactus = Plant("Cactus", 20, 100)
    # bamboo = Plant("Bamboo", 150, 200)
    # Flowering plants
    # daisy = FloweringPlant("Daisy", 15, 10, "white")
    # orchid = FloweringPlant("Orchid", 25, 40, "pink")
    # lily = FloweringPlant("Lily", 18, 12, "yellow")
    # Prize flowers
    # dahlia = PrizeFlower("Dahlia", 28, 20, "red", 8)
    # camellia = PrizeFlower("Camellia", 24, 22, "white", 7)

    print("=== Garden Management System Demo ===\n")

    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)
    # alice_garden.add_plant(bamboo)
    # alice_garden.add_plant(dahlia)
    # bob_garden.add_plant(cactus)
    # bob_garden.add_plant(daisy)
    # bob_garden.add_plant(orchid)
    # bob_garden.add_plant(lily)
    # bob_garden.add_plant(camellia)

    gardens = [alice_garden, bob_garden]
    alice_garden.help_grow()

    # maple = Plant("Maple", 80, 200)
    # tulip = FloweringPlant("Tulip", 12, 15, "purple")
    alice_garden.report()
    print()
    alice_garden.validate_heights()

    # bob_garden.add_plant(maple)
    # bob_garden.add_plant(tulip)
    # print()
    # bob_garden.report()

    print(f"Total Gardens managed: {GardenManager.gardens_managed(gardens)}")
    print(f"Total plants: {GardenManager.GardenStats.total_plants(gardens)}")
    GardenManager.GardenStats.gardens_score(gardens)
    print()
    print(f"Average garden height: "
          f"{GardenManager.GardenStats.average_garden_height(gardens)}")


if __name__ == "__main__":
    ft_garden_analytics()
