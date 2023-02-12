from tkinter import Tk, Frame, Label, Button, Canvas, Entry, OptionMenu, StringVar
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
        self._root.geometry("1500x1500")

        self._width = 1024
        self._height = 1024

        self._dijkstra = Dijkstra()
        self._jps = JPS()
        self._filereader = FileReader()
        self._custom_map = False

    def start(self):
        """
            Alustaa tarvittavat muutujat ja graafiset oliot
        """

        frame = Frame(self._root)
        frame.grid(row=0, column=0, sticky="n")

        map_names = self._filereader.read_map_names()
        map_names.append("Custom")
        self._current_map = self._filereader.read_map(map_names[0])
        self._map_width = len(self._current_map[0])
        self._map_height = len(self._current_map)

        self._menu_text = StringVar()
        self._menu_text.set(map_names[0])
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

        self._canvas = Canvas(self._root, bg="black", width=1024, height=1024)
        self._canvas.grid(row=0, column=1)
        # self._canvas.pack(anchor="nw", fill="both", expand=1)

        image = Image.open(f"kuvat/{map_names[0]}.png")

        # image.resize((256,256), Image.ANTIALIAS)

        image = ImageTk.PhotoImage(image)

        # self._canvas.create_image(0, 0, image=image, anchor="nw")

        self._image_container = self._canvas.create_image(
            0, 0, image=image, anchor="nw")
        self._canvas.bind("<Button-1>", self._get_mouse_coordinates)
        self._canvas.bind("<B1-Motion>", self._mouse_down)

        self._width_scalar = self._width / self._map_width
        self._heigth_scalar = self._height / self._map_height
        self._root.mainloop()

    def _draw_path(self, path):
        """
            Piirtää algoritmin palauttaman polun kartan päälle
        """

        self._canvas.delete("line")

        points = [(it[1]*self._width_scalar, it[0]*self._heigth_scalar)
                  for it in path]

        if self._custom_map:
            for p in points:
                self._canvas.create_rectangle(
                    p[0], p[1],
                    p[0]+self._width_scalar, p[1]+self._heigth_scalar,
                    fill="red",
                    tags="line"
                )
        else:
            self._canvas.create_line(
                points, width=self._width_scalar, fill="red", tags="line")

    def _handle_dijkstra_button(self):
        """
            Käynnistää kartan ratkaisemisen dijkstran-algoritmilla
        """

        start = (int(self._start_y_entry.get()),
                 int(self._start_x_entry.get()))
        end = (int(self._end_y_entry.get()),
               int(self._end_x_entry.get()))

        distance, path = self._dijkstra.solve(
            start,
            end,
            self._current_map,
        )

        if distance:
            print(distance)
            self._draw_path(path)
            print(self._jps.solve(start, end, self._current_map))

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

        self._canvas.delete("line")
        self._canvas.delete("boxes")

        new_map_name = self._menu_text.get()
        if new_map_name == "Custom":
            self._custom_map = True
            return self._draw_custom_map()

        self._custom_map = False
        self._current_map = self._filereader.read_map(new_map_name)
        self._map_width = len(self._current_map[0])
        self._map_height = len(self._current_map)
        self._width_scalar = self._width / self._map_width
        self._heigth_scalar = self._height / self._map_height

        image = Image.open(f"kuvat/{new_map_name}.png")
        image = ImageTk.PhotoImage(image)
        self._canvas.itemconfig(self._image_container, image=image)
        self._canvas.imgref = image

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

        self._heigth_scalar = self._height / 10
        self._width_scalar = self._width / 10
        self._current_map = [["." for _ in range(10)] for _ in range(10)]

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
