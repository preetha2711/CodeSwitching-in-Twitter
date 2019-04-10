file = open("Dalit_Collated_Cleaned.txt", "r")
f2 = open("Dalit_col_fin.txt", "w")

for line in file:
    words = line.split(" ")
    for word in words:
        count_sent = 0
        while count_sent < 3:
            if word == "sentenceender":
                count_sent += 1