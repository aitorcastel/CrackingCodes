import pyperclip
import argparse



parser = argparse.ArgumentParser(description='Encrypt with transposition cipher')
parser.add_argument('message', type=str, help='Message to encrypt')
parser.add_argument('key', type=int, help='Key for the message')
parser.add_argument('-f', '--formula', dest='control_formula', action='store_true', help='show the formula for this cipher')
parser.add_argument('-d', '--debug', dest='control_debug', action='store_true', help='[Debug] show how the cipher message is created')


args = parser.parse_args()

def main():
    
    banner()
    if(args.control_formula):
        formula()
    message =  args.message
    key = args.key

    ciphertext = encrypt(key, message)
    print("\n>>> [i] Cipher message: "+ciphertext + '|\n')
    pyperclip.copy(ciphertext)

def encrypt(key, message):
    ciphertext = [''] * key

    for column in range(key):
        currentIndex = column
        while currentIndex < len(message):
            ciphertext[column] += message[currentIndex]
            if(args.control_debug):
                print(ciphertext)
            currentIndex +=key
    
    return ''.join(ciphertext) # concatenate the list with no string between them

def banner():

    print('\n## Transposition encrypt v1.0 ###############')
    print('#                           Code by 0x41t0r #')
    print('# Based in a example from Al Sweigart       #')
    print('#############################################\n')

def formula():

    print('Formula:\n\tx = length of the message\n\tn = key\n\tn = current column\n')
    print('>>> n column = { 0*x+(n-1), 1*x+(n-1), ... y*x+(n-1)} with the condition of x*y+(n-1) > length of the message = null\n')


if __name__ == '__main__':
    main()