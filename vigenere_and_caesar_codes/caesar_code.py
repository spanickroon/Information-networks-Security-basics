import string


def read_file(file_path: str) -> str:
    text = None
    with open(file_path, 'r') as rf:
        text = rf.read()
    return text


def write_file(file_path: str, text: str) -> None:
    with open(file_path, 'w') as wf:
        wf.write(text)


def define_alphabet(letter: str) -> tuple:
    ENG_ALPH = string.ascii_lowercase
    RUS_ALPH = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    if letter in ENG_ALPH or letter in RUS_ALPH:
        curr_alph = ENG_ALPH if letter in ENG_ALPH else RUS_ALPH
        return (curr_alph, len(curr_alph))
    else:
        return (None, None)


def caesar_code(text: str, key: int, mode: int) -> str:
    cipher_text = []
    for letter in text:
        alph, power_alph = define_alphabet(letter.lower())
        if alph is None:
            cipher_text.append(letter)
            continue
        if mode:
            index = (alph.find(letter.lower()) - key + power_alph) % power_alph
        else:
            index = (alph.find(letter.lower()) + key) % power_alph
        ciph_let = alph[index]
        cipher_text.append(ciph_let if letter.islower() else ciph_let.upper())
    return "".join(cipher_text)


def main():
    while True:
        file_path = input("Enter filepath: ")
        key = input("Enter key: ")
        mode = input("Enter mode:\n 0 - encrypt\n 1 - decrypt\n")

        if key.isdigit() and mode.isdigit():
            try:
                text = read_file(file_path)
            except FileNotFoundError:
                print("File not found")
            cipher_text = caesar_code(text, int(key), int(mode))
            new_file_path = file_path + "_mod_by_caesar"
            write_file(new_file_path, cipher_text)
            print(f"Check file {new_file_path}")
        else:
            print("The key or mode must be a number!")


if __name__ == "__main__":
    main()
