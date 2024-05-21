import sys, mabcapi

try:
    if sys.argv[1] == '-s':
        phrase = sys.argv[2]
        mabcapi.salt_encrypt(phrase)
        sys.exit(1)
    if sys.argv[1] == '-h':
        mabcapi.usage()
        sys.exit(1)
    if sys.argv[1] == '-v':
        mabcapi.version()
        sys.exit(1)
    action = sys.argv[1]
    pwd1 = sys.argv[2]
    pwd2 = sys.argv[3]
    BL = int(sys.argv[4])
    BD = int(sys.argv[5])
    phrase = sys.argv[6]

    mabcapi.determine(action, pwd1, pwd2, BL, BD, phrase)

except IndexError:
    mabcapi.usage()