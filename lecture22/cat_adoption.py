from cat import Cat

def add_cat(cats: list) -> None:
    """
    Get info from the user and add to the list.
    """
    name = input("Enter the cat's name: ")
    # might want some input validation here
    age = float(input("Enter the cat's age: "))
    colour = input("Enter the cat's colour: ")
    new_cat = Cat(name, age, colour)
    cats.append(new_cat)

def adopt_cat(cats: list, name: str) -> Cat:
    """
    Adopt a cat from the list.
    """
    adopted = None
    for i in range(len(cats)):
        if cats[i].name == name:
            cats[i].adopted = True
            adopted = cats[i]
    
    return adopted

def show_cats(cats: list) -> None:
    """
    Print out all the cats in the list.
    """
    print("Here are all the cats:")
    for cat in cats:
        print(cat)

def main() -> None:
    cats = []
    keep_adding = input("Would you like to add a cat? y/n: ")
    while keep_adding == "y":
        add_cat(cats)
        keep_adding = input("Add another cat? y/n: ")

    show_cats(cats)

    to_adopt = input("Which cat would you like to adopt? ")
    take_home = adopt_cat(cats, to_adopt)

    show_cats(cats)

    if take_home is not None:
        print(f"We're taking home {take_home.name}.")

main()