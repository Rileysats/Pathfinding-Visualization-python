
import tkinter as tk
from tkinter.constants import END
import pygame

# GLOBAL VARIABLES
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (130,130,130)
WIDTH_OF_SQUARE = 15
HEIGHT_OF_SQUARE = 15
MARGIN = 2
ROW = 30
COLUMN = 30
SQAURES = 30
WINDOW_SIZE = ((SQAURES+1)*MARGIN+SQAURES*WIDTH_OF_SQUARE, (SQAURES+1)*MARGIN+SQAURES*HEIGHT_OF_SQUARE+30)
GRID = []
# algos = ["Dijkstra's algorithm", "A* algorithm", "Sample algorithm"]
# BTN_LIST = []

class Path:

  def __init__(self) -> None:
      pass
  
  def set_start(self,start):
    self.start = start
  
  def set_end(self,end):
    self.end = end



# PYGAME GRID INTIALISE
def make_grid():
  for row in range(ROW):
      GRID.append([])
      for column in range(COLUMN):
          GRID[row].append(0) 

# TKINTER POPUP

def set_algo(num,path,btn_list,algos) -> None:
  global algo 
  algo = algos[num]
  for i in range(len(btn_list)):
    if i != num:
      btn_list[i].configure(fg="red")
    else:
      btn_list[num].configure(fg="green")

def algo_select(path):
  algos = ["Dijkstra's algorithm", "A* algorithm", "Sample algorithm"]
  btn_list = []

  popup = tk.Tk()
  popup.title('Pathfinding algorithm')
  text = tk.Label(popup, text ="Choose path finding algorithm.")

  submit = tk.Button(popup,pady=8,padx=12,fg='green',font=("Arial",20), text='Submit', command=popup.destroy)
  text.grid(row=0,columnspan=3)

  submit.grid(column=1,row=2)

  for i,v in enumerate(algos):
    b = tk.Button(popup,command=lambda i=i: set_algo(i,path,btn_list,algos),text=v,fg="red")
    b.grid(row=1,column=i)
    btn_list.append(b)

  popup.update()
  tk.mainloop()


# PYGAME SETUP
def main() -> None:
  pygame.init()
  screen = pygame.display.set_mode(WINDOW_SIZE)
  pygame.display.set_caption(algo)
  done = False
  clock = pygame.time.Clock()
  while not done:
    position = pygame.mouse.get_pos()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True
      elif pygame.mouse.get_pressed()[0] and position[1] > 33:
        
        column = position[0] // (WIDTH_OF_SQUARE + MARGIN)
        row = position[1] // (HEIGHT_OF_SQUARE + MARGIN)-2
        if row < ROW and column < COLUMN:
          if (row == start[1] and column == start[0]) or (row == end[1] and column == end[0]):
            continue
          GRID[row][column] = 1

      elif event.type == pygame.MOUSEBUTTONDOWN and 0 < position[1] < 33 and (WINDOW_SIZE[0]//2)-35 < position[0] < (WINDOW_SIZE[0]//2)+35:
        # find()
        pass
    screen.fill(BLACK)
      
    for row in range(len(GRID)):
      for column in range(len(GRID[0])):
        color = WHITE
        if GRID[row][column] == 1: #BARRIER
          color = GREY
        if GRID[row][column] == 2: #START
          color = RED
        if GRID[row][column] == 3: #END
          color = BLACK
        pygame.draw.rect(screen,color,
                              [(MARGIN + WIDTH_OF_SQUARE) * column + MARGIN,
                                (MARGIN + HEIGHT_OF_SQUARE) * row + MARGIN+30, WIDTH_OF_SQUARE, HEIGHT_OF_SQUARE])
    pygame.draw.rect(screen,WHITE,((WINDOW_SIZE[0]//2)-35,2,70,28))
    font = pygame.font.SysFont('times new roman',35)
    text = font.render("start",1,(0,0,0))
    screen.blit(text,((WINDOW_SIZE[0]//2)-32,-4))       
    clock.tick(60)

    pygame.display.flip()

  pygame.quit()

if __name__ == "__main__":
  path = Path()
  make_grid()
  algo_select(path)
  main()

