with open("cg.txt", "r",  encoding='utf8') as file:
    line = file.readlines()
    print(line[0])
    print(line[4])
    for i in line[0 : 5]:
        print(i.strip())
    print()
    for i in line[0 : 2]:
        print(i.strip())
    print()
    for i in line:
        print(i.strip())

