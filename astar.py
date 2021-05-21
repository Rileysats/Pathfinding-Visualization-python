# start, end === (row,column)
GREEN = (0, 255, 0)
BLUE = (255, 0 ,0)
WIDTH_OF_SQUARE = 15
def astar(screen,grid,start,end):
  open = []
  close = []
  
  open.append(start)
  for i in start.neighbours:
    i.set_color(screen)
  # while len(open) > 0:
  #   lowestIndex = 0
  #   for i in range(len(open)):
  #     if open[i].F < open[lowestIndex].F:
  #       lowestIndex = i

  #   current = open[lowestIndex]
  #   if current == end:
  #     print('done',current.F)
      
  #     temp = current.F
  #     for i in range(round(current.F)):
  #       pass
    
  #   open.pop(lowestIndex)
  #   close.append(lowestIndex)

  #   neighbours = current.neighbours
  #   print(neighbours)




  return grid

def heuristic():
  pass