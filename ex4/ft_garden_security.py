#!/usr/bin/env python3

class SecurePlant:
    _name: str
    __height: int = 0
    __age: int = 0

    def __init__(self, name: str, height: int, age: int):
        self._name = name.capitalize()
        print(f"Plant created: {self._name}")
        self.set_height(height)
        self.set_age(age)

    def _reject(self, operation: str, message: str):
        print(f"Invalid operation attempted: {operation} [REJECTED]")
        print(f"Security: {message}")

    def _accept(self, field: str, value):
        print(f"{field} updated: {value} [OK]")

    def set_height(self, height: int):
        if height < 0:
            self._reject(f"height {height}cm", "Negative height rejected.")
        else:
            self.__height = height
            self._accept("Height", f"{height}cm")

    def set_age(self, age: int):
        if age < 0:
            self._reject(f"age {age} days", "Negative age rejected.")
        else:
            self.__age = age
            self._accept("Age", f"{age} days")

    def get_name(self):
        return self._name

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 25, 30)
    print()
    rose.set_height(-5)
    print()
    print(f"Current plant: {rose.get_name()}",
          f"({rose.get_height()}cm, {rose.get_age()} days)")
