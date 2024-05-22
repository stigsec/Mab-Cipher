import sys, os, string
from random import randint, choice

alphabet =  string.ascii_lowercase + \
           '1234567890`~!@#$%^&*()-_=+[{]};:.,?"/\'' + \
           string.ascii_uppercase

alphabet_only_letters =  string.ascii_lowercase + string.ascii_uppercase
digits = '0123456789'

def determine(action, pwd1, pwd2, BL, BD, phrase):
    if action not in ['-h', '-v', '-s', '-ss', '-fe', '-fd']:
        print(f"Error: argument {action} not recognized")
        sys.exit(1)
    match action:
        case '-h':
            usage()
        case '-v':
            version()
        case '-s':
            salt_encrypt(phrase)
        case '-fe':
            check_arguments(pwd1, pwd2, BL, BD)
            file_encrypt(pwd1, pwd2, BL, BD, phrase)
        case '-fd':
            check_arguments(pwd1, pwd2, BL, BD)
            file_decrypt(pwd1, pwd2, BL, BD, phrase)

def usage():
    os.system('cls')
    print("MAB-CIPHER by MABSEC")
    print("")
    print("Usage: ")
    print("mabc {action} {pwd1} {pwd2} {BL} {BD} {phrase/filename}")
    print("""Actions:
          -fe - encrypt from a file
          -fd - decrypt from a file
          -v - check version info
          -s - use the salt hashing algorithm (doesn't require passwords)
          -ss - use custom set salt: 
                mabc -ss {salt} {phrase}
          -h - prints this menu
          
          Explanation of the needed arguments:
          pwd1 - first password (no repeating letters)
          pwd2 - second password
          BL - has to be lower than amount of letters in pwd2
          BD - can't be higher than BL
          phrase/filename - your phrase/file that will be encrypted/decrypted
          """)
    sys.exit(1)
    
def version():
    os.system('cls')
    print("MAB-CIPHER by MABSEC")
    print("")
    print("version 1.3")
    sys.exit(1)

def generate_salt():
    salt = ''
    i = 0
    while i != 64:
        letter_or_digit = randint(0, 1)
        if letter_or_digit == 0:
            chosen_letter = choice(alphabet_only_letters)
            salt += chosen_letter
        else:
            chosen_digit = choice(digits)
            salt += chosen_digit
        i += 1
    return salt

def salt_encrypt(phrase):
    s1 = generate_salt()
    s2 = generate_salt()
    s = s1 + s2
    print(f"Salt: {s}")
    to_encode = s1 + phrase + s2
    encrypt(to_encode, s1, s2)

def split_salt(salt, phrase):
    index = len(salt) // 2
    s1 = salt[:index]
    s2 = salt[index:]
    to_encode = s1 + phrase + s2
    encrypt(to_encode, s1, s2)

def check_arguments(pwd1, pwd2, BL, BD):
    no_repeat = len(set(pwd1)) == len(pwd1)
    if no_repeat == False:
        print(f"Repeated characters in '{pwd1}'")
        sys.exit(1)
    if BL >= len(pwd2):
        a = len(pwd2)
        print(f"BL ({BL}) can't be higher than the length of pwd2 ({a})")
        sys.exit(1)
    if BD > BL:
        print("BD ({BD}) can't be higher than BL {BL}")
        sys.exit(1)

def encrypt(to_encode, s1, s2):
    pwd1 = s1
    BL = 63
    BD = 2
    pwd2 = s2
    num_to_delete = len(pwd2) - BL
    total_char = len(pwd2) - num_to_delete - 1
    mod = modify_alphabet(pwd1)
    all_lines = modify_string(pwd2, mod)
    extracted_characters = extract_characters(mod, all_lines)
    modified_extracted_characters = delete_chars_from_right(extracted_characters, num_to_delete)
    final_result = delete_chars_from_extracted(modified_extracted_characters, BD)
    cipher = encrypt_text(mod, final_result.split(), to_encode)
    print("")
    print(cipher)

def file_encrypt(pwd1, pwd2, BL, BD, phrase):
    num_to_delete = len(pwd2) - BL
    total_char = len(pwd2) - num_to_delete - 1
    mod = modify_alphabet(pwd1)
    all_lines = extract_plaintext_from_file(phrase)
    for line in all_lines:
        extracted_characters = extract_characters(mod, modify_string(pwd2, mod))
        modified_extracted_characters = delete_chars_from_right(extracted_characters, num_to_delete)
        final_result = delete_chars_from_extracted(modified_extracted_characters, BD)
        cipher = encrypt_text(mod, final_result.split(), line.strip())
        print(cipher)

def file_decrypt(pwd1, pwd2, BL, BD, phrase):
    ciphertext = extract_ciphertext_from_file(phrase)
    num_to_delete = len(pwd2) - BL
    total_char = len(pwd2) - num_to_delete - 1
    mod = modify_alphabet(pwd1)
    for line in ciphertext:
        all_lines = modify_string(pwd2, mod)
        extracted_characters = extract_characters(mod, all_lines)
        modified_extracted_characters = delete_chars_from_right(extracted_characters, num_to_delete)
        final_result = delete_chars_from_extracted(modified_extracted_characters, BD)
        divide_bits(mod, line.strip(), total_char, final_result)
    
def index_bits(mod, divided_bits, final_result):
    indexed_bits = []
    for item in divided_bits:
        if item in final_result:
            index = final_result.index(item) + 1
            indexed_bits.append(index)
    decrypt_text(mod, indexed_bits)
    return indexed_bits

def divide_bits(mod, phrase, total_char, final_result):
    divided_bits = []
    for i in range(0, len(phrase), total_char):
        divided_bits.append(phrase[i:i+total_char])
    index_bits(mod, divided_bits, final_result.split())
    return divided_bits

def decrypt_text(mod, indexed_bits):
    result = ''
    for number in indexed_bits:
        if 0 < number <= len(mod):
            result += mod[number - 1]
        else:
            result += ' '
    print(result.strip())

def modify_alphabet(pwd1):
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
        if char in mod:
            index = mod.find(char)
            if index != -1 and index < len(final_result):
                encrypted_text += final_result[index]
            else:
                encrypted_text += char
        else:
            encrypted_text += char
    return encrypted_text

def extract_plaintext_from_file(phrase):
    try:
        with open(phrase, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print("Error: File Not Found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def extract_ciphertext_from_file(phrase):
    try:
        with open(phrase, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print("Error: File Not Found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
