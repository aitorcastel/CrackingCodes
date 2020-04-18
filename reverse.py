# reverse cipher

print('Write a message: ')
message = input()
rev=''

i = len(message) - 1
while i >= 0:
    rev = rev + message[i]
    i -=1

print('[>] Reverse: \t'+rev)

message=''
i = len(rev) -1
while i>=0:
    message+=rev[i]
    i-=1

print('[>] Original: \t'+message)

