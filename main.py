from random import randint
import os

def ascii_one():
    os.system('cls')
    print("              ___.                    .__       .__                  ")
    print("  _____ _____ \_ |__             ____ |__|_____ |  |__   ___________ ")
    print(" /     \\\\__  \\ | __ \   ______ _/ ___\|  \____ \\|  |  \\_/ __ \\_  __ \\")
    print("|  Y Y  \\/ __ \\| \\_\\ \\ /_____/ \\  \\___|  |  |_> >   Y  \\  ___/|  | \\/")
    print("|__|_|  (____  /___  /          \\___  >__|   __/|___|  /\\___  >__|   ")
    print("      \\/     \\/    \\/               \\/   |__|        \\/     \\/       ")

def ascii_two():
    os.system('cls')
    print(r"                                                              _..._                                                                                ")
    print(r"                                                           .-'_..._''.                                                                             ")
    print(r" __  __   ___               /|                           .' .'      '.\ .--. _________   _...._         .                  __.....__               ")
    print(r"|  |/  `.'   `.             ||                          / .'            |__| \        |.'      '-.    .'|              .-''         '.             ")
    print(r"|   .-.  .-.   '            ||                         . '              .--.  \        .'```'.    '. <  |             /     .-''\"'-.  `.  .-,.--.  ")
    print(r"|  |  |  |  |  |     __     ||  __      ,.----------.  | |              |  |   \      |       \     \ | |            /     /________\   \ |  .-. | ")
    print(r"|  |  |  |  |  |  .:--.'.   ||/'__ '.  //            \ | |              |  |    |     |        |    | | | .'''-.     |                  | | |  | | ")
    print(r"|  |  |  |  |  | / |   \ |  |:/`  '. ' \\            / . '              |  |    |      \      /    .  | |/.'''. \    \    .-------------' | |  | | ")
    print(r"|  |  |  |  |  | `\" __ | |  ||     | |  `'----------'   \ '.          . |  |    |     |\\`'-.-'   .'   |  /    | |     \    '-.____...---. | |  '-  ")
    print(r"|__|  |__|  |__|  .'.''| |  ||\    / '                   '. `._____.-'/ |__|    |     | '-....-'`     | |     | |      `.             .'  | |      ")
    print(r"                 / /   | |_ |/\'..' /                      `-.______ /         .'     '.              | |     | |        `''-...... -'    | |      ")
    print(r"                 \ \._,\ '/ '  `'-'`                                `        '-----------'            | '.    | '.                        |_|      ")
    print(r"                  `--'  `\"                                                                            '---'   '---'                                 ")

def random_menu_art():
    pick = randint(1, 2)
    if pick == 1:
        ascii_one()
    else:
        ascii_two()

random_menu_art()
print("")
print("")
pwd1 = input("pwd1: ")
pwd2 = input("pwd2: ")
BL = int(input("BL: "))
BD = int(input("BD: "))
alphabet = 'abcdefghijklmnopqrstuwvxyz'
num_to_delete = len(pwd2) - BL
total_char = len(pwd2) - num_to_delete - 1
print("Encrypt (E) or Decrypt (D)")
choice = input(": ")
if choice == "E":
    encrypt_me = input("Encrypt this: ")
    t = 1
if choice == "D":
    decrypt_me = input("Decrypt this: ")
    t = 2

def modify_alphabet(pwd1, alphabet):
    alphabet_list = list(alphabet)
    for char in pwd1:
        if char in alphabet_list:
            alphabet_list.remove(char)
    modified_alphabet = ''.join(alphabet_list)
    result = pwd1 + modified_alphabet
    return result

def modify_string(pwd2, mod):
    lines = []
    for char in pwd2:
        index = mod.find(char)
        if index != -1:
            before_char = mod[:index]
            after_char = mod[index:]
            mod = after_char + before_char
            lines.append(mod)
    return lines

def extract_characters(mod, all_lines):
    extracted = ''
    for i, char in enumerate(mod):
        for line in all_lines:
            if i < len(line):
                extracted += line[i]
        extracted += ' '  
    return extracted.strip()

def delete_chars_from_right(extracted, num_of_chars_to_delete):
    chars_list = extracted.split()
    modified_chars_list = [char[:-num_of_chars_to_delete] if len(char) > num_of_chars_to_delete else '' for char in chars_list]
    modified_extracted = ' '.join(modified_chars_list)
    return modified_extracted

def delete_chars_from_extracted(extracted, BD):
    chars_list = extracted.split()
    modified_chars_list = [char[:BD-1] + char[BD:] if len(char) > BD else char for char in chars_list]
    modified_extracted = ' '.join(modified_chars_list)
    return modified_extracted

mod = modify_alphabet(pwd1, alphabet)
all_lines = modify_string(pwd2, mod)
extracted_characters = extract_characters(mod, all_lines)
modified_extracted_characters = delete_chars_from_right(extracted_characters, num_to_delete)
final_result = delete_chars_from_extracted(modified_extracted_characters, BD)

def encrypt_text(mod, final_result, encrypt_me):
    encrypted_text = ''
    for char in encrypt_me:
        index = mod.find(char)
        if index != -1:
            encrypted_text += final_result[index]
        else:
            encrypted_text += char + ' '
    return encrypted_text.strip()

def index_bits(divided_bits, final_result):
    indexed_bits = []
    for item in divided_bits:
        if item in final_result:
            index = final_result.index(item) + 1
            indexed_bits.append(index)
    decrypt(mod, indexed_bits)
    return indexed_bits

def divide_bits():
    divided_bits = []
    for i in range(0, len(decrypt_me), total_char):
        divided_bits.append(decrypt_me[i:i+total_char])
    index_bits(divided_bits, final_result.split())
    return divided_bits

def decrypt(mod, indexed_bits):
    result = ''
    for number in indexed_bits:
        if 0 < number <= len(mod):
            result += mod[number - 1]
    print(result)
if t == 1:
    encrypted_text = encrypt_text(mod, final_result.split(), encrypt_me)
    print(encrypted_text)
if t == 2:
    divide_bits()