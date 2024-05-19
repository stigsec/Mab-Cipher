###MAB-CIPHER BY MABSEC
import sys
def start(action, pwd1, pwd2, BL, BD, phrase):
    if action not in ['e', 'd']:
        print("Wrong action!")
        print("Use e/d")
        usage()
    if not (pwd1.islower() and pwd2.islower()) or not (pwd1.isalpha() and pwd2.isalpha()):
        print("Uppercase letter or a number in pwd1 or pwd2!")
        print("Only use lowercase letters")
        usage()
    if not (phrase.islower() and phrase.isalpha()):
        print("Uppercase, number or a character in your phrase!")
        print("Only use lowercase letters")
    if BL >= len(pwd2):
        print("BL can't be equal or higher than the length of pwd2!")
        print("Choose a lower BL")
        usage()
    if BD > BL:
        print("BD can't be higher than BL")
        print("Choose a lower BD")
        usage()

    if action == 'e':
        alphabet = 'abcdefghijklmnopqrstuwvxyz'
        num_to_delete = len(pwd2) - BL
        total_char = len(pwd2) - num_to_delete - 1
        mod = modify_alphabet(pwd1, alphabet)
        all_lines = modify_string(pwd2, mod)
        extracted_characters = extract_characters(mod, all_lines)
        modified_extracted_characters = delete_chars_from_right(extracted_characters, num_to_delete)
        final_result = delete_chars_from_extracted(modified_extracted_characters, BD)
        cipher = encrypt_text(mod, final_result.split(), phrase)
        print(cipher)

    if action == 'd':
        alphabet = 'abcdefghijklmnopqrstuwvxyz'
        num_to_delete = len(pwd2) - BL
        total_char = len(pwd2) - num_to_delete - 1
        mod = modify_alphabet(pwd1, alphabet)
        all_lines = modify_string(pwd2, mod)
        extracted_characters = extract_characters(mod, all_lines)
        modified_extracted_characters = delete_chars_from_right(extracted_characters, num_to_delete)
        final_result = delete_chars_from_extracted(modified_extracted_characters, BD)
        divide_bits(mod, phrase, total_char, final_result)

def usage():
    print("Usage: ")
    print("mabc e/d pwd1 pwd2 BL BD phrase")
    print("")
    print("e/d - encrypt/decrypt")
    print("pwd1 - first password")
    print("pwd2 - second password")
    print("BL - has to be lower than amount of letters in pwd2")
    print("BD - can't be higher than BL")
    print("phrase - Your phrase to be encoded/decoded")
    sys.exit(1)

def index_bits(mod, divided_bits, final_result):
    indexed_bits = []
    for item in divided_bits:
        if item in final_result:
            index = final_result.index(item) + 1
            indexed_bits.append(index)
    decrypt(mod, indexed_bits)
    return indexed_bits

def divide_bits(mod, phrase, total_char, final_result):
    divided_bits = []
    for i in range(0, len(phrase), total_char):
        divided_bits.append(phrase[i:i+total_char])
    index_bits(mod, divided_bits, final_result.split())
    return divided_bits

def decrypt(mod, indexed_bits):
    result = ''
    for number in indexed_bits:
        if 0 < number <= len(mod):
            result += mod[number - 1]
    print(result)

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

def encrypt_text(mod, final_result, encrypt_me):
    encrypted_text = ''
    for char in encrypt_me:
        index = mod.find(char)
        if index != -1:
            encrypted_text += final_result[index]
        else:
            encrypted_text += char + ' '
    return encrypted_text.strip()