# start, end === (row,column)
import math
GREEN = (0, 255, 0)
BLUE = (255, 0 ,0)
WIDTH_OF_SQUARE = 15
def astar(screen,grid,start,end):
  open = []
  close = []
  
  open.append(start)

  while len(open) > 0:
    lowestIndex = 0
    for i in range(len(open)):
      if open[i].F < open[lowestIndex].F:
        lowestIndex = i

    current = open[lowestIndex]
    if current == end:
      print('done',current.F)
      
      temp = current.F
      for i in range(round(current.F)):
        pass
    
    open.pop(lowestIndex)
    close.append(current)

    neighbours = current.neighbours
    for i in range(len(neighbours)):
      neighbour = neighbours[i]
      if neighbour not in close:
        tempG = current.G + current.val
        if neighbour in open:
          if neighbour.G > tempG:
            neighbour.G = tempG
        else:
          neighbour.G = tempG
          open.append(neighbour)
      
      neighbour.H = heuristic(neighbour, end)
      neighbour.F = neighbour.G + neighbour.H

      if neighbour.previous == None:
        neighbour.previous = current
    
    for i in range(len(open)):
      open[i].set_color(screen,(0,0,255))
    for i in range(len(close)):
      if close[i] != start:
        close[i].set_color(screen,(0,255,0))
    current.closed = True




  return grid

def heuristic(node, end):
  d = math.sqrt((node.column - end.column)**2 + (node.row - end.row)**2)
  return d