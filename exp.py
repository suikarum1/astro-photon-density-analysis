'''
y2 = 7
x2 = -2
a = abs(x2)
y0 = (375*y2)/abs(x2)
print(str(y0))
'''

with open("Conclude.txt", "r") as f:
    lines = f.readlines()
    line_num = 0
    for l in lines[0:]:
        line_num += 1
        ra = float(l.split(",")[0])
        dec = float(l.split(",")[1])
        o = float(l.split(",")[2])
        uv = float(l.split(",")[3])
        if uv > 100:
            print(str(ra)+'|'+str(dec)+'|'+str(uv))
