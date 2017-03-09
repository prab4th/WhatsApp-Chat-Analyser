import os
from collections import OrderedDict

with open('hours.csv', 'w') as w:
    w.write('')

out = open('hours.csv', 'a', encoding='utf8')

hours = {}

#searches for WhatsApp chat files
for fil in os.listdir():
    if fil[:18] == "WhatsApp Chat with" and fil[-4:] == ".txt":
        #opens each WhatsApp chat file
        with open(fil, 'r', encoding='utf8') as fil:
            for line in fil:
                if len(line) > 14 and line[14] == ':':
                    linehour = line[12:14]
                    if linehour.isdigit():
                        if linehour in hours:
                            hours[linehour] = hours[linehour] + 1
                        else:
                            hours[linehour] = 1

# hours = OrderedDict(sorted(hours.keys())

out.writelines('Hour,Freq' + '\n')

for key in sorted(hours.keys()):
    out.write(key)
    out.write(',')
    out.write(str(hours[key]) + '\n')
