import sys
from mabcapi import *

match len(sys.argv):

    case 2:
        action = sys.argv[1]
        Utils.checkAction(action)

    case 3:  #here we encrypt with random salt
        #all cases are +1 because script = sys.argv[0]
        action = sys.argv[1]
        Utils.checkAction(action)
        phrase = sys.argv[2]
        to_encode, s1, s2 = Salt.encryptRandomSalt(phrase)
        print(Salt.createCiphertext(to_encode, s1, s2))
        sys.exit()

    case 4:  #here we encrypt with custom salt
        action = sys.argv[1]
        Utils.checkAction(action)
        salt = sys.argv[2]
        phrase = sys.argv[3]
        to_encode, s1, s2 = Salt.encryptCustomSalt(salt, phrase)
        print(Salt.createCiphertext(to_encode, s1, s2))
        sys.exit()

    case 8: #arguments
        action = sys.argv[1]
        pwd1 = sys.argv[2]
        pwd2 = sys.argv[3]
        BL = int(sys.argv[4])
        BD = int(sys.argv[5])
        input_file = sys.argv[6]
        output_file = sys.argv[7]
        Utils.checkAction(action)
        Utils.checkArgs(action, pwd1, pwd2, BL, BD, input_file, output_file)

    case _:
        Utils.errorMessage("WrongArgumentCount")