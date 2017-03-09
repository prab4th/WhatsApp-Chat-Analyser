import os
from collections import OrderedDict

with open('output.csv', 'w', encoding='utf8') as o:
    o.write('')

out=open('output.csv', 'a', encoding='utf8')

users= {}
n = 0

#searches for WhatsApp chat files
for fil in os.listdir():
    if fil[:18] == "WhatsApp Chat with" and fil[-4:] == ".txt": 
        #opens each WhatsApp chat file
        with open(fil, 'r', encoding='utf8') as fil:
            for line in fil:
                if ':' in line[15:] and '-' in line[15:]:
                    a, b = line[15:].index('-')+15, line[15:].index(':')+15
                    if a < b:
                        username = line[a+2:b]
                        # print(username)
                        if username in users:
                            users[username] = users[username] + 1
                        else:
                            users[username] = 1

users = OrderedDict(sorted(users.items(), key=lambda t:t[1], reverse=True))


out.writelines('\"Name\",\"Freq\"' + '\n')

for key, value in users.items():
    if key[1] == '+':
        key = key.replace(key[8:11], '***').replace(key[1:5],'0')
    out.write('\"' + key + '\"')
    out.write(',')
    out.write(str(value) + '\n')
    n = n + value

print(n)
out.close()