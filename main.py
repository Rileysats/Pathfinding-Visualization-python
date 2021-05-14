import tkinter as tk


root = tk.Tk()
root.title("Choose pathfinding algorithm")
root.minsize(700,600)

label = tk.Label(root, text='Start(x,y): ')
startBox = tk.Entry(root)
label1 = tk.Label(root, text='End(x,y): ')
endBox = tk.Entry(root)

algos = ["Dijkstra's algorithm", "A* algorithm", "Sample algorithm"]
btn_list = []

def algoSelect():
  print('a')
for i,v in enumerate(algos):
  button = tk.Button(root,text=v,padx=10,pady=5,command=algoSelect)
  button.grid(row=0,column=i)
  btn_list.append(button)

root.update()
root.mainloop()





if __name__ == "__main__":
  print('s')