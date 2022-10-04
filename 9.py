l = []

with open('pac.txt', 'r', encoding='utf8') as file:
    line = file.readlines()
    
    station_count = int(line[0])
    passengers = line[1:]
    for i in passengers:
        l.append(i.split())

    for i in range(len(l)):
        for j in range(1,3):
            l[i][j] = int(l[i][j])
            
at_every_station = [0 for _ in range(station_count)]
for name, start_station, end_station in l:
    for station in range(start_station - 1, end_station - 1):
        at_every_station[station] += 1
 
max_passengers = max(at_every_station)
 
for station, count in enumerate(at_every_station, start=1):
    if count == max_passengers:
        print(f'{station} - {station + 1}')

    










 
