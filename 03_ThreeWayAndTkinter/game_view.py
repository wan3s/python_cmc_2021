import tkinter
from dataclasses import dataclass

class GameView:
    _TITLE = 'CrazyGameDev'
    _WINDOW_SIZE = '500x500'

    def __init__(self):
        self._root = tkinter.Tk()
        self._root.title(self._TITLE)
        self._root.geometry(self._WINDOW_SIZE)

        self._game_control_buttons = ButtonsHolder(
            self._root,
            row=0, 
            rows_num=1,
            columns_num=2,
            buttons=[
                Button(
                    Coords(0, 0),
                    'new'
                ),
                Button(
                    Coords(0, 1),
                    'quit'
                ),
            ]
        )
        self._game_process_buttons = ButtonsHolder(
            self._root,
            1, 4, 4,
            buttons=[
                Button(
                    Coords(x // 4, x % 4),
                    str(x),
                )
                for x in range(0, 15)
            ]
        )

        for btn in [
            Button(
                    self._game_control_buttons,
                    Coords(0, 0),
                    'new'
                ),
                Button(
                    self._game_control_buttons,
                    Coords(0, 1),
                    'quit'
                ),
            ]:
            

        self._root.mainloop()


class ButtonsHolder:
    def __init__(
        self,
        root,
        row,
        rows_num,
        columns_num,
    ):
        self._buttons = []
        self._frame = tkinter.Frame(root)
        self._frame.grid(row=row)

        for row in range(rows_num):
            self._frame.rowconfigure(row, weight=1)
            for column in range(columns_num):
	            self._frame.columnconfigure(column, weight=1)


    def add_button(self, btn):
        self._buttons.append(btn)
        self._refresh_view()

    def _refresh_view(self):
        for btn in self._buttons:
            btn.draw()


class Button:
    def __init__(self, frame, coords, text):
        self._row = coords.row
        self._column = coords.column
        self._text = text
        self._btn = tkinter.Button(frame, text=self._text, command=self._click)
        self.draw()

    def draw(self):
        self._btn.grid(row=self._row, column=self._column)

    @property
    def coords(self):
        return Coords(self._row, self._column)

    def _click(self):
        print(f'btn {self._text} clicked')

@dataclass
class Coords:
    row: int
    column: int
