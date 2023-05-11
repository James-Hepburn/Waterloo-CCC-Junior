def valid_grid (grid):
  for i in grid:
    for j in range (len (grid) - 1):
      if i[j] >= i[j+1]:
        return False
  for i in range (len (grid[0])):
    for j in range (len (grid) - 1):
      if grid[j][i] >= grid[j+1][i]:
        return False
  return True

N = int (input())
grid = []

for i in range (N):
  grid.append ([int (i) for i in input().split()])
  
while not valid_grid (grid):
  grid = [list(x) for x in zip(*grid[::-1])]
   
for i in grid:
  str_i = [str(j) for j in i]
  print (" ".join (str_i))
               
