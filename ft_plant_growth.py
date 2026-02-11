#!/usr/bin/env python3

class Plant:
	def __init__(self, name: str, height: int, age: int) -> None:
		self.name: str = name
		self.height: int = height
		self.age: int = age

	def get_info(self) -> str:
		return f"{self.name}: {self.height}cm, {self.age} days old"

	def grow(self, days: int) -> None:
		self.height += days

	def increase_age(self, days: int) -> None:
		self.age += days

def main():
	plant = Plant("Rose", 25, 30)
	days_passed = 6
	print("=== Day 1 ===")
	print(plant.get_info())
	print(f"=== Day {1 + days_passed} ===")
	plant.grow(days_passed)
	plant.increase_age(days_passed)
	print(plant.get_info())
	print(f"Growth this week: +{days_passed}cm")

if __name__ == "__main__":
	main()