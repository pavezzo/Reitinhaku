from tkinter import (
    Tk, Frame, Label, Button, Canvas, Entry, OptionMenu, StringVar, constants
)
from PIL import ImageTk, Image
from algorithms.dijkstra import Dijkstra
from algorithms.jps import JPS
from utils.filereader import FileReader


class UI:
    """
        Luokka, joka hallitsee ohjelman graafista näkymää
    """

    def __init__(self):
        self._root = Tk()
        self._root.title("Reitinhaku")

        self._screen_width = self._root.winfo_screenwidth()
        self._screen_height = self._root.winfo_screenheight()

        self._root.geometry(f"{self._screen_width}x{self._screen_height}")

        self._width = 1024
        self._height = 1024

        self._dijkstra = Dijkstra()
        self._jps = JPS()
        self._filereader = FileReader()
        self._custom_map = False

        self._path = None
        self._visited = None

    def start(self):
        """
            Alustaa tarvittavat muutujat ja graafiset oliot
        """

        frame = Frame(self._root)
        # frame.grid(row=0, column=0, sticky="n")

        map_names = self._filereader.read_map_names()
        map_names.append("Custom")
        self._current_map = self._filereader.read_map(map_names[0])
        self._map_width = len(self._current_map[0])
        self._map_height = len(self._current_map)

        self._menu_text = StringVar()
        self._menu_text.set("Select map")
        self._menu_text.trace("w", self._map_changed)

        dropdown_menu = OptionMenu(frame, self._menu_text, *map_names)
        dropdown_menu.grid(row=0, column=0, sticky="nwe")

        Label(
            master=frame,
            text="Start coordinates"
        ).grid(row=1, column=0, sticky="nwe")

        self._start_x_entry = Entry(frame)
        self._start_x_entry.grid(row=2, column=0, sticky="w")
        self._start_y_entry = Entry(frame)
        self._start_y_entry.grid(row=2, column=1, sticky="e")

        Label(
            master=frame,
            text="End coordinates"
        ).grid(row=3, column=0, sticky="nwe")

        self._end_x_entry = Entry(master=frame)
        self._end_x_entry.grid(row=4, column=0, sticky="w")
        self._end_y_entry = Entry(master=frame)
        self._end_y_entry.grid(row=4, column=1, sticky="e")

        Button(
            master=frame,
            text="Solve with dijkstra",
            command=self._handle_dijkstra_button
        ).grid(row=5, column=0, sticky="nwe")

        Button(
            master=frame,
            text="Solve with JPS",
            command=self._handle_jps_button
        ).grid(row=6, column=0, sticky="nwe")

        self._distance_label = Label(
            master=frame,
            text=""
        )
        self._distance_label.grid(row=7, sticky="nw")

        self._time_label = Label(
            master=frame,
            text=""
        )
        self._time_label.grid(row=8, sticky="nw")

        self._visited_label = Label(
            master=frame,
            text=""
        )
        self._visited_label.grid(row=9, sticky="nw")

        self._frame = frame
        self._frame.pack(side=constants.LEFT, anchor="nw")
        # self._frame.pack(anchor="nw")
        self._canvas = Canvas(
            self._root,
            bg="black",
            width=self._screen_width//2,
            height=self._screen_height
        )
        # self._canvas.grid(row=0, column=1)
        # self._root.columnconfigure(1, weight=1)
        self._canvas.pack(expand=1, fill=constants.BOTH, side=constants.RIGHT, anchor="ne")
        # image = Image.open(f"kuvat/{map_names[0]}.png")
        # image.resize((256,256), Image.ANTIALIAS)
        # image = ImageTk.PhotoImage(image)
        # self._canvas.create_image(0, 0, image=image, anchor="nw")
        # self._image_container = self._canvas.create_image(
        #    0, 0, image=image, anchor="nw")

        self._canvas.bind("<Button-1>", self._get_mouse_coordinates)
        self._canvas.bind("<B1-Motion>", self._mouse_down)

        self._width_scalar = self._width / self._map_width
        self._heigth_scalar = self._height / self._map_height

        # self._root.bind("<Configure>", self._resize)
        self._root.mainloop()

    def _draw_path(self, path):
        """
            Piirtää algoritmin palauttaman polun kartan päälle
        """
        self._path = path

        for y, x in path:
            self._canvas.itemconfig(self._rectangles[y][x], fill="red")

    def _draw_visited(self, visited):
        if self._path:
            for y, x in self._path:
                if y < self._map_height and x < self._map_width:
                    self._canvas.itemconfig(self._rectangles[y][x], fill="white")
        if self._visited:
            for y, x in self._visited:
                if y < self._map_height and x < self._map_width:
                    self._canvas.itemconfig(self._rectangles[y][x], fill="white")
        self._visited = visited

        for y, x in visited:
            self._canvas.itemconfig(self._rectangles[y][x], fill="blue")

    def _handle_dijkstra_button(self):
        """
            Käynnistää kartan ratkaisemisen dijkstran-algoritmilla
        """
        start, end = self._get_start_end_coordinates()
        distance, path, time, visited = self._dijkstra.solve(
            start,
            end,
            self._current_map,
        )

        if distance:
            self._distance_label["text"] = "Distance: " + str(distance)
            self._time_label["text"] = "Took: " + str(time) + " seconds"
            self._visited_label["text"] = "Visited: " + \
                str(len(visited)) + " nodes"
            self._draw_visited(visited)
            self._draw_path(path)

    def _handle_jps_button(self):
        start, end = self._get_start_end_coordinates()
        distance, path, time, visited = self._jps.solve(
            start, end, self._current_map)

        if distance:
            self._distance_label["text"] = "Distance: " + str(distance)
            self._time_label["text"] = "Took: " + str(time) + " seconds"
            self._visited_label["text"] = "Visited: " + \
                str(len(visited)) + " nodes"
            self._draw_visited(visited)
            self._draw_path(path)

    def _get_start_end_coordinates(self):
        start = (int(self._start_y_entry.get()),
                 int(self._start_x_entry.get()))
        end = (int(self._end_y_entry.get()),
               int(self._end_x_entry.get()))

        return start, end

    def _get_mouse_coordinates(self, event):
        """
            Palauttaa hiiren koordinaatit Canvas-oliossa, ei käyttöä vielä
        """

        self._last_x = event.x
        self._last_y = event.y
        print(round(event.x/self._width_scalar),
              round(event.y/self._heigth_scalar))

    def _map_changed(self, *args):
        """
            Hallinnoi kartan vaihtamisen
        """

        self._canvas.delete("boxes")

        new_map_name = self._menu_text.get()

        if new_map_name == "Custom":
            self._custom_map = True
            return self._draw_custom_map()

        self._custom_map = False

        self._current_map = self._filereader.read_map(new_map_name)
        self._map_width = len(self._current_map[0])
        self._map_height = len(self._current_map)

        box_w = self._canvas.winfo_width() / self._map_width
        box_h = self._canvas.winfo_height() / self._map_height
        self._rectangles = [[None for _ in range(
            self._map_width)] for _ in range(self._map_height)]

        for i in range(self._map_height):
            for j in range(self._map_width):
                rec = None
                if self._current_map[i][j] == ".":
                    rec = self._canvas.create_rectangle(
                        j*box_w, i*box_h, j*box_w+box_w, i*box_h+box_h,
                        fill="white",
                        tags="boxes",
                        outline=""
                    )
                else:
                    rec = self._canvas.create_rectangle(
                        j*box_w, i*box_h, j*box_w+box_w, i*box_h+box_h,
                        fill="black",
                        tags="boxes",
                        outline=""
                    )
                self._rectangles[i][j] = rec

        self._heigth_scalar = self._canvas.winfo_height() / self._map_height
        self._width_scalar = self._canvas.winfo_width() / self._map_width

    def _draw_custom_map(self):
        """
            Piirtää 10x10 kartan, jota voidaan käyttää debuggaamiseen
        """
        box_w = self._canvas.winfo_width() / 10
        box_h = self._canvas.winfo_height() / 10
        self._rectangles = [[None for _ in range(10)] for _ in range(10)]
        for i in range(10):
            for j in range(10):
                rec = self._canvas.create_rectangle(
                    j*box_w, i*box_h, j*box_w+box_w, i*box_h+box_h,
                    fill="white",
                    tags="boxes"
                )
                self._rectangles[i][j] = rec

        self._heigth_scalar = self._canvas.winfo_height() / 10
        self._width_scalar = self._canvas.winfo_width() / 10
        self._current_map = [["." for _ in range(10)] for _ in range(10)]
        self._map_height = 10
        self._map_width = 10

    def _draw_obstacle_to_custom_map(self, x, y):
        """
            Piirtää esteen custom kartalle
        """
        x = int(x // self._width_scalar)
        y = int(y // self._heigth_scalar)
        self._current_map[y][x] = "@"
        self._canvas.itemconfig(self._rectangles[y][x], fill="black")

    def _mouse_down(self, event):
        """
            Välittää hiiren koordinaatit eteenpäin esteen piirtämistä varten
        """
        if self._custom_map:
            self._draw_obstacle_to_custom_map(event.x, event.y)

    def _resize(self, event):
        width = event.width - self._frame.winfo_width()
        height = event.height - self._frame.winfo_height()
        if self._width == width and self._height == height:
            return

        self._canvas.config(width=width, height=height)
        self._width = width
        self._height = height
