#!/usr/bin/env python3

class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name: str = name
        self._height: int = height
        self._age: int = age

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"

    def grow(self, days: int) -> None:
        self.height += days

    def increase_age(self, days: int) -> None:
        self.age += days
