import tkinter as tk
from tkinter.constants import END
import pygame
import astar
import Node

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
# START = (-1,-1)
# END = 9

  
def make_grid() -> None:
  global grid
  grid = []
  for row in range(ROW):
    grid.append([])
    for column in range(COLUMN):
      grid[row].append(Node.Node(0,(row,column)))

          # self.grid[row].append(float('inf')) 


def set_neighbours(grid) -> None:
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      grid[row][col].get_neighbours(grid)

# # PYGAME GRID INTIALISE
# def make_grid() -> None:
#   for row in range(ROW):
#       GRID.append([])
#       for column in range(COLUMN):
#           GRID[row].append(float('inf')) 

# TKINTER POPUP
def set_algo(num,btn_list,algos) -> None:
  global ALGO
  ALGO = algos[num]
  for i in range(len(btn_list)):
    if i != num:
      btn_list[i].configure(fg="red")
    else:
      btn_list[num].configure(fg="green")

def on_submit(root) -> None:
  if ALGO:
    root.destroy()
    root.quit()

def algo_select():
  algos = ["Dijkstra's algorithm", "A* algorithm", "Sample algorithm"]
  btn_list = []

  root = tk.Tk()
  root.title("Pathfinding algorithm")
  text = tk.Label(root, text ="Choose path finding algorithm.")
  root.eval('tk::PlaceWindow . center')
  submit = tk.Button(root,pady=8,padx=12,fg='green',font=("Arial",20), text='Submit', command=lambda: on_submit(root))

  text.grid(row=0,columnspan=3)
  submit.grid(column=1,row=2)

  for i,v in enumerate(algos):
    b = tk.Button(root,command=lambda i=i: set_algo(i,btn_list,algos),text=v,fg="red")
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
  for row in range(len(grid)):
    for column in range(len(grid[0])):
      color = WHITE
      pygame.draw.rect(screen,color,
                              [(WIDTH_OF_SQUARE) * column,
                                ( HEIGHT_OF_SQUARE) * row +30, WIDTH_OF_SQUARE, HEIGHT_OF_SQUARE])

def draw_lines(screen) -> None:
  for row in range(len(grid)):
    pygame.draw.line(screen,BLACK,(WIDTH_OF_SQUARE*row,30),(WIDTH_OF_SQUARE*row,WINDOW_SIZE[1]),1)
    for column in range(len(grid[0])):
      pygame.draw.line(screen,BLACK,(0,WIDTH_OF_SQUARE*column+30),(WINDOW_SIZE[0],WIDTH_OF_SQUARE*column+30),1)

def update_grid(screen) -> None:
  for row in range(len(grid)):
    for column in range(len(grid[0])): 
      # color = None
      # if grid[row][column].color == -1: #BARRIER
      #   color = GREY
      # if grid[row][column].color == -2: #START
      #   color = RED
      # if grid[row][column].color == -3: #END
      #   color = BLACK
      # if grid[row][column].color == -4: #PATH
      #   color = GREEN
      if grid[row][column].color:
        pygame.draw.rect(screen,grid[row][column].color,
                              [(WIDTH_OF_SQUARE) * column,
                                ( HEIGHT_OF_SQUARE) * row +30, WIDTH_OF_SQUARE, HEIGHT_OF_SQUARE])

def draw_on_grid(screen,row,column) -> None:
  if "start" not in globals():
    global start
    start = grid[row][column]
    start.color = (255,0,0)
  elif "end" not in globals() and (row,column) != (start.row,start.column):
    global end
    end = grid[row][column]
    end.color = (0,0,0)
  elif (row == start.row and column == start.column) or (row == end.row and column == end.column):
    return
  else:
    grid[row][column].color = (130,130,130)
    grid[row][column].wall = True


# PYGAME SETUP
def main() -> None:
  pygame.init()
  screen = pygame.display.set_mode(WINDOW_SIZE)
  pygame.display.set_caption(ALGO)
  screen.fill(BLACK)
  done = False
  clock = pygame.time.Clock()
  game_text = "start"
  stop_drawing = False
  started = False
  draw_grid(screen)
  draw_lines(screen)
  finished = False
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
      # elif started:
      #   if ALGO == "Dijkstra's algorithm":
      #     pass
      #   elif ALGO == "A* algorithm":
      #     # path.grid = astar.astar(screen,path,path.grid,path.start,path.end)
          
      #     done = False
      #     break
      #   elif ALGO ==  "Sample algorithm":
      #     pass
 
    update_grid(screen)
    if started and not finished:
      if ALGO == "Dijkstra's algorithm":
        pass
      if ALGO == "A* algorithm":
        astar.astar(screen,grid,start,end)
        finished = True
      if ALGO == "Sample algorithm":
        pass

    
    
    pygame.draw.rect(screen,WHITE,((WINDOW_SIZE[0]//2)-35,1,70,28))
    font = pygame.font.SysFont('times new roman',35)
    text = font.render(game_text,1,(0,0,0))
    screen.blit(text,((WINDOW_SIZE[0]//2)-32,-7))
 
    clock.tick(1000)
    pygame.display.flip()

  
  # pygame.quit()


if __name__ == "__main__":
  make_grid()
  set_neighbours(grid)
  algo_select()
  tell_user()
  main()

