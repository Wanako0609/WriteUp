# Source Generated with Decompyle++
# File: ch19.pyc (Python 3.1)

#Warning: Stack history is not empty!
if __name__ == '__main__':
    print('Welcome to the RootMe python crackme')
    PASS = input('Enter the Flag: ')
    KEY = 'I know, you love decrypting Byte Code !'
    I = 5
    SOLUCE = [
        57,
        73,
        79,
        16,
        18,
        26,
        74,
        50,
        13,
        38,
        13,
        79,
        86,
        86,
        87]
    PASS = input('Enter the Flag: ')
    KEY = 'I know, you love decrypting Byte Code !'
    I = 5
    KEYOUT = []
    for char in PASS:
        KEYOUT.append((ord(char) + I ^ ord(KEY[I])) % 255)
        I = (I + 1) % len(KEY)
    
    if SOLUCE == KEYOUT:
        print('You Win')
    else:
        print('Try Again !')
