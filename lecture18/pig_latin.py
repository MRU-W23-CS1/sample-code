def to_pig_latin(word: str) -> str:
    """
    Converts the word to pig latin.
    """
    first = word[0]
    rest = word[1:] # shorthand for word[1:len(word)]
    return rest + first + "ay"

def convert_sentence(sentence: str) -> str:
    s_list = sentence.split()
    pig_sentence = ""
    # for q in range(len(s_list)):
        # pig_sentence += to_pig_latin(s_list[q]) + " "
    for word in s_list:
        pig_sentence += to_pig_latin(word) + " "
        word = "bob"
    
    return pig_sentence

def test_single_word() -> None:
    to_convert = input("Enter a word to translate: ")
    pig = to_pig_latin(to_convert)
    print(f"{to_convert} in pig latin is {pig}")

def main() -> None:
    to_convert = input("Enter a sentence to translate: ")
    pig = convert_sentence(to_convert)
    print(pig)

main()