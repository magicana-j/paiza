s = 'PiZzA'
new_s = ''

for i in range(len(s)):
    if ord(s[i]) < ord('a'):
        print(chr(ord(s[i])+ord('a')-ord('A')))
    else:
        print(s[i])
