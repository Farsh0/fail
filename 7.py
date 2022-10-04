
        
with open('cg.txt', 'r', encoding='utf8') as file:
    lines = [line.rstrip()[::-1] + '\n' for line in file.readlines()]
# Прямой порядок
with open('w.txt', 'w') as file:
    file.writelines(lines)
    
    file.writelines(lines[::-1])
