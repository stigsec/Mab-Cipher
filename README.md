For installation go to the releases tab\

Mab-Cipher Usage:
              
-e  - Encrypt
-d  - Decrypt
-s  - Encrypt with random salt
-cs - Encrypt with custom salt
-v  - Version info
-h  - prints this menu

mabc {-e/-d} {pwd1} {pwd2} {BL} {BD} {input_file} {output_file}
mabc {-s} {plaintext}
mabc {-ss} {salt} {plaintext}

BD < BL < len(pwd2)
