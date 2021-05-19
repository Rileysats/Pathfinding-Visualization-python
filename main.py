import tkinter as tk
from tkinter.constants import END
import pygame
import astar

# GLOBAL VARIABLES
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (130,130,130)
WIDTH_OF_SQUARE = 15
HEIGHT_OF_SQUARE = 15
ROW = 30
COLUMN = 30
SQAURES = 30
WINDOW_SIZE = (SQAURES*WIDTH_OF_SQUARE, SQAURES*HEIGHT_OF_SQUARE+30)
GRID = []

class Path:

  def __init__(self) -> None:
      self.start = None
      self.end = None
      self.algo = None
  
  def set_start(self,start) -> None:
    self.start = start
  
  def set_end(self,end) -> None:
    self.end = end

  def set_algo(self,algo) -> None:
    self.algo = algo



# PYGAME GRID INTIALISE
def make_grid() -> None:
  for row in range(ROW):
      GRID.append([])
      for column in range(COLUMN):
          GRID[row].append(float('inf')) 

# TKINTER POPUP
def set_algo(num,path,btn_list,algos) -> None:
  path.set_algo(algos[num])
  for i in range(len(btn_list)):
    if i != num:
      btn_list[i].configure(fg="red")
    else:
      btn_list[num].configure(fg="green")

def on_submit(root,path) -> None:
  if path.algo:
    root.destroy()
    root.quit()

def algo_select(path):
  algos = ["Dijkstra's algorithm", "A* algorithm", "Sample algorithm"]
  btn_list = []

  root = tk.Tk()
  root.title("Pathfinding algorithm")
  text = tk.Label(root, text ="Choose path finding algorithm.")
  root.eval('tk::PlaceWindow . center')
  submit = tk.Button(root,pady=8,padx=12,fg='green',font=("Arial",20), text='Submit', command=lambda: on_submit(root,path))

  text.grid(row=0,columnspan=3)
  submit.grid(column=1,row=2)

  for i,v in enumerate(algos):
    b = tk.Button(root,command=lambda i=i: set_algo(i,path,btn_list,algos),text=v,fg="red")
    b.grid(row=1,column=i)
    btn_list.append(b)

  root.mainloop()


def tell_user() -> None:
  root = tk.Tk()
  root.title("Pathfinding algorithm")
  root.eval('tk::PlaceWindow . center')
  tk.Label(root, text ="First click is start point, second click is destination").pack()
  tk.Button(root,pady=6,padx=8,fg='green',font=("Arial",10), text='OK', command=root.destroy).pack()
  root.mainloop()

def draw_grid(screen) -> None:
  for row in range(len(GRID)):
    for column in range(len(GRID[0])):
      color = WHITE
      pygame.draw.rect(screen,color,
                              [(WIDTH_OF_SQUARE) * column,
                                ( HEIGHT_OF_SQUARE) * row +30, WIDTH_OF_SQUARE, HEIGHT_OF_SQUARE])

def draw_lines(screen) -> None:
  for row in range(len(GRID)):
    pygame.draw.line(screen,BLACK,(WIDTH_OF_SQUARE*row,30),(WIDTH_OF_SQUARE*row,WINDOW_SIZE[1]),1)
    for column in range(len(GRID[0])):
      pygame.draw.line(screen,BLACK,(0,WIDTH_OF_SQUARE*column+30),(WINDOW_SIZE[0],WIDTH_OF_SQUARE*column+30),1)

def update_grid(screen) -> None:
  for row in range(len(GRID)):
    for column in range(len(GRID[0])): 
      color = None
      if GRID[row][column] == -1: #BARRIER
        color = GREY
      if GRID[row][column] == -2: #START
        color = RED
      if GRID[row][column] == -3: #END
        color = BLACK
      if color:
        pygame.draw.rect(screen,color,
                              [(WIDTH_OF_SQUARE) * column,
                                ( HEIGHT_OF_SQUARE) * row +30, WIDTH_OF_SQUARE, HEIGHT_OF_SQUARE])

def draw_on_grid(screen,row,column) -> None:
  if not path.start:
    path.set_start((row,column))
    GRID[row][column] = -2
  elif not path.end and (row,column) != path.start:
    path.set_end((row,column))
    GRID[row][column] = -3
  elif (row == path.start[0] and column == path.start[1]) or (row == path.end[0] and column == path.end[1]):
    return
  else:
    GRID[row][column] = -1

# PYGAME SETUP
def main(path) -> None:
  pygame.init()
  screen = pygame.display.set_mode(WINDOW_SIZE)
  pygame.display.set_caption(path.algo)
  screen.fill(BLACK)
  done = False
  clock = pygame.time.Clock()
  game_text = "start"
  stop_drawing = False
  started = False
  draw_grid(screen)
  draw_lines(screen)
  while not done:
    position = pygame.mouse.get_pos()
    column = position[0] // WIDTH_OF_SQUARE
    row = position[1] // HEIGHT_OF_SQUARE-2

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True
      elif pygame.mouse.get_pressed()[0] and position[1] > 33 and row < ROW and column < COLUMN and stop_drawing == False:
        draw_on_grid(screen,row,column)

      elif event.type == pygame.MOUSEBUTTONDOWN and 0 < position[1] < 33 and (WINDOW_SIZE[0]//2)-35 < position[0] < (WINDOW_SIZE[0]//2)+35 and game_text == "start":    
        game_text = "stop"
        started = True
        stop_drawing = True
      elif event.type == pygame.MOUSEBUTTONDOWN and 0 < position[1] < 33 and (WINDOW_SIZE[0]//2)-35 < position[0] < (WINDOW_SIZE[0]//2)+35 and game_text == "stop":
        game_text = "start"
        started = False
      elif started:
        pass



      
      update_grid(screen)
      
    pygame.draw.rect(screen,WHITE,((WINDOW_SIZE[0]//2)-35,1,70,28))
    font = pygame.font.SysFont('times new roman',35)
    text = font.render(game_text,1,(0,0,0))
    screen.blit(text,((WINDOW_SIZE[0]//2)-32,-7))
 
    clock.tick(60)
    pygame.display.flip()

  pygame.quit()

if __name__ == "__main__":
  path = Path()
  make_grid()
  algo_select(path)
  tell_user()
  main(path)

