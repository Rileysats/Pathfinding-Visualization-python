import tkinter as tk
from tkinter.constants import END
import pygame

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
grey = (130,130,130)
width = 15
height = 15
margin = 2
ROW = 30
COLUMN = 30

grid = []
for row in range(ROW):
    grid.append([])
    for column in range(COLUMN):
        grid[row].append(0) 

window_size = (31*margin+30*height, 31*margin+30*width)


algos = ["Dijkstra's algorithm", "A* algorithm", "Sample algorithm"]
btn_list = []
def algoSelect(num) -> None:
  for i in range(len(btn_list)):
    if i != num:
      btn_list[i].configure(fg="red")
    else:
      btn_list[num].configure(fg="green")
 
def onsubmit() -> None:
  global start
  global end
  start = grid[int(startBoxx)][int(startBoxy)]
  end = grid[int(endBoxx)][int(endBoxy)]
  popup.quit()
  popup.destroy()
  
popup = tk.Tk()
text = tk.Label(popup, text ="Enter co-ords for start and end point and path finding algorithm.")
start = tk.Label(popup, text="Start(x,y): ")
startBoxx = tk.Entry(popup)
startBoxy = tk.Entry(popup)
end = tk.Label(popup, text="End(x,y): ")
endBoxx = tk.Entry(popup)
endBoxy = tk.Entry(popup)
var = tk.IntVar()

# showPath = tk.Checkbutton(popup, text='Show Steps :', onvalue=1, offvalue=0, variable=var)
# algo =

submit = tk.Button(popup,pady=8,padx=12,fg='green',font=("Arial",20), text='Submit', command=onsubmit)

# showPath.grid(columnspan=2, row=2)
text.grid(row=0,columnspan=2)
startBoxx.grid(row=1, column=2)
startBoxy.grid(row=1, column=3)
end.grid(row=2, pady=3)
start.grid(row=1, pady=3)
endBoxx.grid(row=2, column=1)
endBoxy.grid(row=2, column=2)

for i,v in enumerate(algos):
  b = tk.Button(popup,command=lambda i=i: algoSelect(i),text=v,fg="red")
  b.grid(row=4,column=i)
  btn_list.append(b)

submit.grid(column=1,row=5)

popup.update()
tk.mainloop()


pygame.init()
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Pathfinding Visualisation")

done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        elif pygame.mouse.get_pressed()[0]:
            position = pygame.mouse.get_pos()
            column = position[0] // (width + margin)
            row = position[1] // (height + margin)
            if row < ROW and column < COLUMN:
              grid[row][column] = 1
    screen.fill(black)
    
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            color = white
            if grid[row][column] == 1:
                color = grey
            pygame.draw.rect(screen,
                             color,
                             [(margin + width) * column + margin,
                              (margin + height) * row + margin, width, height])
 
    clock.tick(60)

    pygame.display.flip()
 
pygame.quit()



# if __name__ == "__main__":
#   print(' ')