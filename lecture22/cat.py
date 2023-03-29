from random import randint

class Cat:
    def __init__(self, name: str, age: float, colour: str) -> None:
        self.name = name
        self.age = age
        self.colour = colour
        self.adopted = False
    
    def __str__(self) -> str:
        """
        Called when cat object is printed.
        """
        desc = f"Cat with name {self.name}"
        if self.adopted:
            desc += " has been adopted!"
        else:
            desc += " is available for adoption."
        return desc

    def scratch(self, thing: str) -> int:
        """
        Cat scratches the thing. Returns amount of damage done.
        """
        print(f"{self.name} scratches the {thing}!")
        return randint(0, 10)

if __name__ == '__main__':
    # name = input("What is the cat's name? ")
    test_cat = Cat("Salvador", 5, "Tuxedo")
    print(f"Created a cat object: {test_cat}")
    c_damage = test_cat.scratch("couch")
    d_damage = test_cat.scratch("Dog")
    print(f"{test_cat.name} did a total of {c_damage + d_damage} damage")
