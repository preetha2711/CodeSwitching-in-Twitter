#!/usr/bin/env python
# -*- coding: utf-8 -*
import re
import emoji
import sys
# reload(sys)  # Reload does the trick!
# sys.setdefaultencoding('UTF8')

file = open("DalitData1Work.txt","r")
f = open("DalitData1_clean.txt", "w")
emoji_pattern = re.compile(
    u"(\ud83d[\ude00-\ude4f])|"  # emoticons
    u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
    u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
    u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
    u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
    "+", flags=re.UNICODE)
#Works for python 2.7


for line in file : 
    s = line
    # teststring = s.encode('unicode_escape')
        
    print line
    if ("RT @" in line):
        temp_line = line.split("RT @") 
        for tweet in temp_line:
            temp = emoji_pattern.sub(r'',tweet)
            print (temp)
            f.write(temp)
            f.write("\n"+"\n")
            print(emoji_pattern.sub(r'', tweet))
    else:
        f.write(emoji_pattern.sub(r'', line) +"\n")

    line_new = ""




