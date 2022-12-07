input = open('data.txt').read().split(',')

totals = []
ongoing = []
current = 0


for x in input: #for each item we:
  current = x
  for x in input: #check its subtract value for all others
    ongoing.append(abs(int(x) - int(current)))
  totals.append(sum(ongoing))
  ongoing.clear()
  
print(min(totals))
