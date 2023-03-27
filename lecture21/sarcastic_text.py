def to_sarcastic(txt: str) -> str:
    """
    Converts regular text into sarcastic text
    """
    sarcastic = ""
    for i in range(0, len(txt)):
        if i % 2 == 0:
            sarcastic += txt[i].lower()
        else:
            sarcastic += txt[i].upper()
    
    return sarcastic

def to_sarcastic_chatgpt(txt: str) -> str:
    """
    Converts regular text into sarcastic text
    """
    sarcastic_text = ""
    is_upper = True  # Start with uppercase letter
    for c in txt:
        if c.isalpha():
            if is_upper:
                sarcastic_text += c.upper()
            else:
                sarcastic_text += c.lower()
            is_upper = not is_upper
        else:
            sarcastic_text += c
    return sarcastic_text

def read_story(filename: str) -> str:
    try:
        f = open(filename, "r")
        contents = f.read()
        f.close()
    except OSError:
        print(f"Sorry, {filename} can't be read, try again")
        filename = input("Try a new filename: ")
        contents = read_story(filename) # Recursion!

    return contents

def write_story(filename: str, story: str) -> None:
    try:
        f = open(filename, "w")
        f.write(story)
        f.close()
        print(f"Successfully wrote to {filename}")
    except OSError:
        print(f"Could not write to {filename} :(")

def main() -> None:
    in_file = input("Enter the file to read: ")
    story = read_story(in_file)
    sarcastic = to_sarcastic(story)
    write_story("data/sarcastic.txt", sarcastic)

main()