from collections import Counter

with open("data01.txt", 'rb') as rd:
    data = Counter(rd.read())
    print "result", data['('] - data[')']
