# import random

# file = open("Collated.txt", "r")
# f = open("Seg_Collated.txt","w")
# count = 0
# non_RT_arr = []
# for line in file: 
#     f.write(line)
#     if line == "\n":
#         f.write("!!!!!!!!!EOT!!!!!!!!!" + "\n")
#     if "RT @" in line:
#         f.write("\n"+"!!!!!!!!!EOT!!!!!!!!!!!" + "\n")
#     f.write(line + "\n"+"!!!!!!!!!EOT!!!!!!!!!!!" +"\n")



# f_read = open("Seg_Collated.txt", "r")
# f_write = open("Seg_Collated_NonRT.txt", "w")

# for line in f_read:
#     if "RT @" in line:
#         continue
#     elif line == "\n":
#         continue
#     elif (("!!!!!!!!!EOT!!!!!!!!!" in line) or ("!!!!!!!!!EOT!!!!!!!!!!!" in line)):
#         continue
#     else :
#         f_write.write(line)

    

f_read_seg_coll = open("Seg_Collated_NonRT.txt", "r+")
f_write_1 = open("Final_Seg_Tweets.txt", "w")
i = 0
for line in f_read_seg_coll:
    if (i%2==0):
        f_write_1.write(line)
    i = i+1
    