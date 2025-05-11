'''
afile = open('Conclude.txt', 'r')
alines = afile.readlines()
number_of_lines = len(alines)
print(number_of_lines)
'''




processes = []

afile = open('Ra_n.txt', 'r')
alines = afile.readlines()
bfile = open('Dec_n.txt', 'r')
blines = bfile.readlines()
cfile = open('O_n.txt', 'r')
clines = cfile.readlines()
dfile = open('UV_n.txt', 'r')
dlines = dfile.readlines()
for i in range(39645038):
    processes.append(alines[i].strip()+','+blines[i].strip()+','+clines[i].strip()+','+dlines[i].strip()+'\n')
    print("s"+str(i))#strip()to take care of the automatically appended \n at the end of each alines[i] term
myfile = open('Conclude.txt','w')
for element in processes:
    myfile.write(element)




'''
afile = open('Ra_n.txt', 'r')
lines = afile.readlines()
number_of_lines = len(lines)
print(number_of_lines)
'''
'''

processes = []
for i in range(39645038):
    afile = open('Ra_n.txt', 'r')
    lines = afile.readlines()
    processes.append(lines[i]+',')
    bfile = open('Dec_n.txt', 'r')
    lines = bfile.readlines()
    processes.append(lines[i]+',')
    cfile = open('O_n.txt', 'r')
    lines = cfile.readlines()
    processes.append(lines[i]+',')
    dfile = open('UV_n.txt', 'r')
    lines = dfile.readlines()
    processes.append(lines[i]+'\n')

    print("s"+str(i))

myfile = open('Conclude.txt','w')
for element in processes:
    myfile.write(element)


'''




'''

crimefile = open('UVPhoton.txt', 'r')
for line in crimefile.readlines():
    result = line.replace(",","\n")


myfile = open('UV_n.txt','w')
myfile.write(result)


'''


'''
processes = []
crimefile = open('DECdataset.txt', 'r')
for line in crimefile.readlines():
    x = line.split(',')
    x = x[:-1]
    del x[2916211]
    del x[3722186]
    del x[7442958]
    del x[10789985]
    del x[12651215]
    for i in range(len(x)):
        processes.append(x[i]+',')


crimefile = open('Dec.txt','w')
for element in processes:
    crimefile.write(element)
'''

'''
processes = []
crimefile = open('RAdataset.txt', 'r')
for line in crimefile.readlines():
    x = line.split(',')
    x = x[:-1]
    for i in range(len(x)):
        processes.append(x[i]+",")
        afile = open('DECdataset.txt','r')
        for line in afile.readlines():
            y = line.split(',')
            y = y[:-1]
            processes.append(y[i]+",")
            bfile = open('OpticalPhoton.txt','r')
            for line in bfile.readlines():
                z = line.split(',')
                z = z[:-1]
                processes.append(z[i]+",")
                cfile = open('UVPhoton.txt','r')
                for line in cfile.readlines():
                    m = line.split(',')
                    m = m[:-1]
                    processes.append(m[i]+"\n")
                    print("s"+str(i))



myfile = open('Conclude.txt','w')
for element in processes:
    myfile.write(element)
'''
