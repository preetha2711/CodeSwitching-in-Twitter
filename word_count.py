file = open("tweets_clean.txt","r")
en = 0
hi = 0
hi_dev = 0
for line in file:
    if "##" not in line:
        words = line.split(" ")
        line = line.decode("utf-8")
        maxchar = max(line)
        # print words
        for word in words:
            if "/EN" in word:
                en +=1
            elif "/HI" in word:
                hi +=1
            elif u'\u0900' <= maxchar <= u'\u097f':
                hi_dev +=1

            
            
        

print en
print hi
print hi_dev