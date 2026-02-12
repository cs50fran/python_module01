def ft_garden_intro(plant, height, age):
    print("=== Welcome to My Garden ===")
    print(f"Plant: {plant}")
    print(f"Height: {height}")
    print(f"Age: {age}\n")
    print("=== End of Program ===")


def main():
    plant: str = "Morango"
    height: str = "50cm"
    age: str = "30 days"
    ft_garden_intro(plant, height, age)


if __name__ == "__main__":
    main()
