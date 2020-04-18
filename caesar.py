# caesar cipher

import pyperclip

print('## CAESAR CIPHER v1.0 #######################')
print('#                           Code by 0x41t0r #')
print('# Based in a example from Al Sweigart       #')
print('#############################################')

print('Enter the message: ')
message = input()
print('Enter the arimetic key: ')
key = int(input())
print('Enter your mode (encrypt/decrypt): ');
mode = input()

SYMBOLS='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'#`~@#$%^&*()_+-=[]{}|;:<>,/'

translated=''
warning=False

for symbol in message:
        if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)

                # encryption or decryption
                if mode == 'encrypt':
                    translatedIndex = symbolIndex + key
                elif mode == 'decrypt':
                    translatedIndex = symbolIndex - key

                # handle wraparound, if needed:
                if translatedIndex >=len(SYMBOLS):
                    translatedIndex -=len(SYMBOLS)
                elif translatedIndex < 0:
                    translatedIndex = translatedIndex + len(SYMBOLS)

                translated +=SYMBOLS[translatedIndex]
        else:
            translated +=symbol
            warning=True

print('Ouput: ')
print(translated)
if(warning):
    print('[!] Some symbols are not supported')
pyperclip.copy(translated)








                
