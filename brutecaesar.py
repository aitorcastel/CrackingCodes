# bruteforce caessar cipher

import pyperclip

print('\n## BRUTE FORCE CAESAR CIPHER v1.0 ###########')
print('#                           Code by 0x41t0r #')
print('# Based in a example from Al Sweigart       #')
print('#############################################')

SYMBOLS='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.`~@#$%^&*()_+-=[]{}|;:<>,/'
print('Enter the message: ')
message=input()

print('Starting...')

for key in range(len(SYMBOLS)):
    translated=''

    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex -key

            if translatedIndex <0:
                translatedIndex+=len(SYMBOLS)

            translated +=SYMBOLS[translatedIndex]

        else:
            translated +=symbol


    print(' KEY [#%s]: %s' %(key, translated)) 

