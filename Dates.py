import os
from collections import OrderedDict

with open('dates.csv', 'w') as w:
    w.write('')

out=open('dates.csv', 'a', encoding='utf8')

dates= {}
n = 0

#searches for WhatsApp chat files
for fil in os.listdir():
    if fil[:18] == "WhatsApp Chat with" and fil[-4:] == ".txt": 
        #opens each WhatsApp chat file
        with open(fil, 'r', encoding='utf8') as fil:
            for line in fil:
                if '/' in line[:3] and ',' in line:

                    a = line.index(',')
                    linedate = line[:a]
                    if linedate in dates:
                        dates[linedate] = dates[linedate] + 1
                    else:
                        dates[linedate] = 1

# dates = OrderedDict(sorted(dates.items(), key=lambda t:t[1], reverse=True))


out.writelines('Date,Freq' + '\n')

for key, value in dates.items():
    key = key.replace('/', '-')
    out.write(key)
    out.write(',')
    out.write(str(value) + '\n')
    n = n + 1

print(n)
