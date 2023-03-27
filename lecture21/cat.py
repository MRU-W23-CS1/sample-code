class Cat:
    def __init__(self) -> None:
        self.age = 0.5
        self.fur = "shorthair"
        self.colour = "black"
        self.name = "smokey"
    
    def scratch(self) -> None:
        """
        Cat scratches
        """
        print(f"{self.name} scratches the post!")
    
def main() -> None:
    smokey = Cat()
    print(smokey)
    print(f"{smokey.name} is {smokey.age} years old")
    smokey.scratch()
    salvador = Cat()
    salvador.name = "Salvador"
    salvador.scratch()

main()