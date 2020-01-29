from string import ascii_lowercase


def read_file(file_path: str) -> str:
    text = None
    with open(file_path, 'r') as rf:
        text = rf.read()
    return text


def write_file(file_path: str, text: str) -> None:
    with open(file_path, 'w') as wf:
        wf.write(text)


def generate_key(key: str, text: str) -> str:
    new_key = list(key)
    while len(new_key) < len(text):
        new_key.extend(key)
    return "".join(new_key)[:len(text) + 1]


def define_alphabet(letter: str) -> tuple:
    ENG_ALPH = ascii_lowercase
    RUS_ALPH = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    if letter in ENG_ALPH or letter in RUS_ALPH:
        curr_alph = ENG_ALPH if letter in ENG_ALPH else RUS_ALPH
        return (curr_alph, len(curr_alph))
    else:
        return (None, None)


def check_key(key: str) -> bool:
    RUS_ALPH = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    if not len(set(key.lower()) - set(ascii_lowercase)):
        return True
    elif not len(set(key.lower()) - set(RUS_ALPH)):
        return True
    else:
        return False


def vigenere_code(text: str, key: str, mode: int) -> str:
    cipher_text = []
    i = 0
    for letter in text:
        alph, power_alph = define_alphabet(letter.lower())
        if alph is None:
            cipher_text.append(letter)
            continue
        kv = alph.find(key[i].lower())
        if mode:
            index = (alph.find(letter.lower()) - kv + power_alph) % power_alph
        else:
            index = (alph.find(letter.lower()) + kv) % power_alph
        ciph_let = alph[index]
        cipher_text.append(ciph_let if letter.islower() else ciph_let.upper())
        i += 1
    return "".join(cipher_text)


def main():
    while True:
        file_path = input("Enter filepath: ")
        key = input("Enter key: ")
        mode = input("Enter mode:\n 0 - encrypt\n 1 - decrypt\n")

        if mode.isdigit():
            try:
                if not check_key(key):
                    raise KeyError
                text = read_file(file_path)
                key = generate_key(key, text)
                cipher_text = vigenere_code(text, key, int(mode))
                new_file_path = file_path + "_mod_by_vigenere"
                write_file(new_file_path, cipher_text)
                print(f"Check file {new_file_path}")
            except FileNotFoundError:
                print("File not found")
            except KeyError:
                print("The key is not only letters")
        else:
            print("The mode must be a number!")


if __name__ == "__main__":
    main()
