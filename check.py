f = open("F_SearchTermsWork.txt", "r+")

for line in f:
    print(line)
    f.truncate()


    