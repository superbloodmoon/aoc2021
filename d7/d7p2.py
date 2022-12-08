input = open('data.txt').read().split(',')

totals = []
ongoing = []
current = 0 #number in focus (taking subtract values from)
add = 0

for x in input: #for each item we:
  current = x
  for x in input: #check its subtract value for all others
    add = (abs(int(x) - int(current))) * ((abs(int(x) - int(current)) +1) / 2)
    ongoing.append(add)
    
  totals.append(sum(ongoing))
  ongoing.clear()
  
print(min(totals))
