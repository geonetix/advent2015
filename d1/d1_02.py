pos = 0
with open("data01.txt", 'rb') as rd:
    data = rd.read()
    for idx, c in enumerate(data):
        if c == '(':
            pos += 1
        elif c == ')':
            pos -= 1
        if pos == -1:
            print "Result", (idx+1)
            break
