import copy

dwarf_9 = []
dwarf_9backup = []
dwarf_7 = 0
for i in range(9):
   dwarf = int(input())
   dwarf_9.append(dwarf) 
   
dwarf_9.sort()

dwarf_9backup = dwarf_9.copy() 

for i in range(8):
    for j in range(8):
        dwarf_9.remove(dwarf_9[i])
        dwarf_9.remove(dwarf_9[j])
        
        if sum(dwarf_9) == 100:
            dwarf_7 = dwarf_9
            dwarf_9 = dwarf_9backup.copy()
        else:
            dwarf_9 = dwarf_9backup.copy()

for i in range(len(dwarf_7)):
    print(dwarf_7[i])
