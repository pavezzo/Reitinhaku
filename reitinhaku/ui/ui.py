from tkinter import *
from PIL import ImageTk, Image
from algorithms.dijkstra import Dijkstra

class UI:
    def __init__(self, map, start, end):
        self._root = Tk()
        self._root.title("Reitinhaku")
        self._root.geometry("1000x1000")
        
        self._width = 1024
        self._height = 1024
        self._map_width = 256
        self._map_height = 256

        self._current_map = map
        self._currrent_start = start
        self._currrent_end = end
        self._dijkstra = Dijkstra()

    def start(self):
        frame = Frame(self._root)
        frame.grid(row=0, column=0, sticky="n")

        start_label = Label(
            master=frame, 
            text="Start coordinates"
        ).grid(row=0, column=0, sticky="nwe")
        
        self._start_x_entry = Entry(frame)
        self._start_x_entry.grid(row=1, column=0, sticky="w")
        self._start_y_entry = Entry(frame)
        self._start_y_entry.grid(row=1, column=1, sticky="e")
        
        end_label = Label(
            master=frame, 
            text="End coordinates"
        ).grid(row=2, column=0, sticky="nwe")
        
        self._end_x_entry = Entry(master=frame)
        self._end_x_entry.grid(row=3, column=0, sticky="w")
        self._end_y_entry = Entry(master=frame)
        self._end_y_entry.grid(row=3, column=1, sticky="e")
        
        dijkstra_button = Button(
            master=frame, 
            text="Solve with dijkstra",
            command = self._handle_dijkstra_button
        ).grid(row=4, column=0, sticky="nwe")
        
        self._canvas = Canvas(self._root, bg="black", width=1024, height=1024)
        self._canvas.grid(row=0, column=1)
        #self._canvas.pack(anchor="nw", fill="both", expand=1)

        image = Image.open("kuvat/Berlin_0_256.png")
        image.resize((1024,1024), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        self._canvas.create_image(0, 0, image=image, anchor="nw")
        self._canvas.bind("<Button-1>", self._get_mouse_coordinates)

        self._root.mainloop()

    def _draw_path(self, path):
        width_scalar = self._width / self._map_width
        heigth_scalar = self._height / self._map_height
        points = [(it[1]*width_scalar, it[0]*heigth_scalar) for it in path]
        self._canvas.create_line(points, width=width_scalar, fill="red")        

    def _handle_dijkstra_button(self):
        start = (int(self._start_y_entry.get()), int(self._start_x_entry.get()))
        end = (int(self._end_y_entry.get()), int(self._end_x_entry.get()))
        
        distance, path = self._dijkstra.solve(
            start,
            end,
            self._current_map,
        )

        if distance:
            print(distance)
            self._draw_path(path)
    
    def _get_mouse_coordinates(self, event):
        self._last_x = event.x
        self._last_y = event.y
        print(event.x, event.y)
