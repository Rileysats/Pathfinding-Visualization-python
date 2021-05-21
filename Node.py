import pygame
WIDTH_OF_SQUARE = 15
HEIGHT_OF_SQUARE = 15
class Node:

  def __init__(self,color,r_c) -> None:
    self.G = 0 #dist from start node
    self.H = 0 #heuristic
    self.F = 0 #total cost of the node
    self.row = r_c[0]
    self.column = r_c[1]
    self.color = color
    self.closed = False
    self.neighbours = []
    self.wall = False

  def set_color(self,screen) -> None:
    if self.closed == True:
      pygame.draw.rect(screen, (0,255,0), (self.column * WIDTH_OF_SQUARE, self.row * HEIGHT_OF_SQUARE, WIDTH_OF_SQUARE, HEIGHT_OF_SQUARE))
      pygame.display.update()
    else:
      pygame.draw.rect(screen, (0,0,255), (self.column * WIDTH_OF_SQUARE, self.row * HEIGHT_OF_SQUARE + 30, WIDTH_OF_SQUARE, HEIGHT_OF_SQUARE))
      pygame.display.update()

  
  def get_neighbours(self,grid) -> None:
    cols = len(grid[0])
    rows = len(grid)
    j = self.row
    i = self.column
    
    if j < cols-1 and grid[j+1][i].wall == False:
      self.neighbours.append(grid[j+1][i])
    if j > 0 and grid[j-1][i].wall == False:
      self.neighbours.append(grid[j-1][i])
    if i < rows-1 and grid[j][i+1].wall == False:
      self.neighbours.append(grid[j][i+1])
    if i > 0 and grid[j][i-1].wall == False:
      self.neighbours.append(grid[j][i-1])

    

  