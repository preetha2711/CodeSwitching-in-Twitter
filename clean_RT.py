import random

file = open("DalitData4.txt", "r")
count = 0
non_RT_arr = []
for line in file : 
    if "RT @" not in line:
        count +=1
        non_RT_arr.append(line)

f_write = open("DalitData4_random.txt","w")
for i in range(count/2):
    tweet = random.choice(non_RT_arr)
    f_write.write(tweet)
    non_RT_arr.remove(tweet)




    


