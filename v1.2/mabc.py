###MAB-CIPHER BY MABSEC
import sys, mabcapi

try:
    if sys.argv[1] == '-h':
        mabcapi.usage()
        sys.exit(1)
    if sys.argv[1] == '-v':
        mabcapi.version()
        sys.exit(1)
    if sys.argv[1] == 'fe':
        action = sys.argv[1]
        pwd1 = sys.argv[2]
        pwd2 = sys.argv[3]
        BL = int(sys.argv[4])
        BD = int(sys.argv[5])
        filename = sys.argv[6]
        mabcapi.start(action, pwd1, pwd2, BL, BD, filename)
        sys.exit(1)
    if sys.argv[1] == 'fd':
        action = sys.argv[1]
        pwd1 = sys.argv[2]
        pwd2 = sys.argv[3]
        BL = int(sys.argv[4])
        BD = int(sys.argv[5])
        filename = sys.argv[6]
        mabcapi.start(action, pwd1, pwd2, BL, BD, filename)
        sys.exit(1)

    if len(sys.argv) != 7:
        mabcapi.usage()
        sys.exit(1)

    action = sys.argv[1]
    pwd1 = sys.argv[2]
    pwd2 = sys.argv[3]
    BL = int(sys.argv[4])
    BD = int(sys.argv[5])
    phrase = sys.argv[6]

    mabcapi.start(action, pwd1, pwd2, BL, BD, phrase)

except IndexError:
    mabcapi.usage()
