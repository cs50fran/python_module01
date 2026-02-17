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
            print(f"{plant.name} +{growth}cm")
        print()

    def report(self) -> None:
        print(f"=== {self.name} Report ===")
        for plant in self.plants:
            print(f"- {plant}")
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
        print(f"All healthy: {self.validate_heights()}")

    def validate_heights(self) -> bool:
        return all(p.height > 0 for p in self.plants)

    def garden_score(self) -> int:
        score = 0
        for plant in self.plants:
            score += plant.height
        for plant in self.plants:
            if hasattr(plant, 'prize_points'):
                score += plant.prize_points
        return score


class GardenManager:
    class GardenStats:
        @staticmethod
        def total_plants(gardens: list) -> int:
            total = 0
            for garden in gardens:
                total += len(garden.plants)
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

    def __init__(self) -> None:
        self.gardens = []

    def add_garden(self, garden: Garden) -> None:
        self.gardens.append(garden)

    def create_garden_network(self, names: list) -> "GardenManager":
        for name in names:
            self.add_garden(Garden(name))
        return self

    @staticmethod
    def utility_garden_tip() -> str:
        return "Water plants in the morning."

    def show_scores(self) -> None:
        score_list = []
        for garden in self.gardens:
            score = garden.garden_score()
            score_list.append(f"{garden.name}: {score}")
        scores_text = ", ".join(score_list)
        print(f"Garden scores - {scores_text}")

    def show_total_gardens(self) -> None:
        print(f"Total gardens: {len(self.gardens)}")


def ft_garden_analytics() -> None:
    print("=== Garden Demo ===\n")
    manager = GardenManager()
    manager.create_garden_network(["Alice", "Bob"])
    alice_garden = manager.gardens[0]
    bob_garden = manager.gardens[1]

    oak = Plant("Oak Tree", 100, 365)
    rose = FloweringPlant("Rose", 25, 30, "red")
    sunflower = PrizeFlower("Sunflower", 50, 60, "yellow", 10)
    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    maple = Plant("Maple", 80, 200)
    tulip = FloweringPlant("Tulip", 12, 15, "purple")
    bob_garden.plants.append(maple)
    bob_garden.plants.append(tulip)

    alice_garden.help_grow()
    alice_garden.report()
    manager.show_scores()
    manager.show_total_gardens()


if __name__ == "__main__":
    ft_garden_analytics()
