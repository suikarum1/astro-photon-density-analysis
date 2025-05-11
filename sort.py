import numpy as np
import math


def func(ra0,dec0):
    processes = []
    processes1 = []
    with open("Conclude.txt", "r") as f:
        lines = f.readlines()
        line_num = 0
        for l in lines[0:]:
            line_num += 1
            ra = float(l.split(",")[0])
            dec = float(l.split(",")[1])
            o = float(l.split(",")[2])
            uv = float(l.split(",")[3])

            ra_n = (ra * math.pi)/180
            ra0_n = (ra0 * math.pi)/180
            dec_n = (dec * math.pi)/180
            dec0_n = (dec0 * math.pi)/180


            r = 100
            z = r*np.sin(dec_n)
            y = r*np.cos(dec_n)*np.sin(ra_n)
            x = r*np.cos(dec_n)*np.cos(ra_n)
            #print(str(z)+'|'+str(y)+'|'+str(x))

            x1 = x*np.cos(ra0_n)+y*np.sin(ra0_n)
            y1 = y*np.cos(ra0_n)-x*np.sin(ra0_n)
            z1 = z
            #print(str(x1)+'|'+str(y1)+'|'+str(z1))

            x2 = x1*np.cos(dec0_n)+z1*np.sin(dec0_n)
            y2 = y1
            z2 = z1*np.cos(dec0_n)-x1*np.sin(dec0_n)
            #print(str(x2)+'|'+str(y2)+'|'+str(z2))

            x0 = (375*x2)/abs(x2)
            y0 = (375*y2)/abs(x2)
            z0 = (375*z2)/abs(x2)
            #print(str(x0)+'|'+str(y0)+'|'+str(z0))

            if x0 > 1 and -66.1226 < y0 < 66.1226 and -66.1226 < z0 < 66.1226:
                processes.append(o) #can be replaced by uv when calculating uv photons
                processes1.append(uv)
                #print(str(ra)+'|'+str(dec)+'|'+str(uv))
                if uv > 10:
                    print(str(ra)+'|'+str(dec)+'|'+str(uv))


            #print('s'+str(line_num))

        return np.sum(processes), np.sum(processes1)

print(func(200,-10))
#print(func(120,-30))

'''

x = []
y = []
z_o = []
z_uv = []
num = 0
for ra0 in range(0, 360, 20):
    for dec0 in range(-90, 95, 20):
        num += 1
        x.append(ra0)
        y.append(dec0)
        ele, ele2 = func(ra0,dec0)
        z_o.append(ele)
        z_uv.append(ele2)
        print(num)

myfile = open('x1.txt','w')
for element in x:
    myfile.write(str(element))
    myfile.write(',')
myfile = open('y1.txt','w')
for element in y:
    myfile.write(str(element))
    myfile.write(',')
myfile = open('z_o1.txt','w')
for element in z_o:
    myfile.write(str(element))
    myfile.write(',')
myfile = open('z_uv1.txt','w')
for element in z_uv:
    myfile.write(str(element))
    myfile.write(',')


'''
#print(func(1,88))
