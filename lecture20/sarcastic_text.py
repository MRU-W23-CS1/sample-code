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
    f = open(filename, "r")
    contents = f.read()
    f.close()
    return contents

def write_story(filename: str, story: str) -> None:
    f = open(filename, "w")
    f.write(story)
    f.close()

def main() -> None:
    story = read_story("data/story.txt")
    sarcastic = to_sarcastic(story)
    write_story("data/sarcastic.txt", sarcastic)

main()