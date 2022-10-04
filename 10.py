inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
k = inFile.readline()
k = int(k)
rez = []
l = inFile.readlines()
for i in l:
    if len(i.split()) == 6:
        n1, n2, n3, s1, s2, s3 = i.split()
    if len(i.split()) == 5:
        n1, n2, s1, s2, s3 = i.split()
 
    if int(s1) >= 40 and int(s2) >= 40 and int(s3) >= 40:
        sum = int(s1) + int(s2) + int(s3)
    else:
        sum = 0
    rez.append(sum)
rez.sort(reverse=True)
if rez[k] == 0:
    print(0)
elif rez[0] == rez[k]:
    print(1)
elif rez[k] == rez[k - 1]:
    print(rez[k - 2])
 
else:
    print(rez[k - 1])
inFile.close()
outFile.close()
