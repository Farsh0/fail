n = 0
r = 0
st = 0
with open("cg.txt", "r",  encoding='utf8') as file:
    line = file.readlines()
    for i in line:
        st += 1
        if len(i) > n:
            n = len(i)
            r = st
        
    print(n)
    print(r)
    print(line[r - 1])
