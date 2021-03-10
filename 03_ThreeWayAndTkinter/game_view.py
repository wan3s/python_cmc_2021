import tkinter
from dataclasses import dataclass

class GameView:
    def __init__(self, title, window_size):
        self._root = tkinter.Tk()
        self._root.title(title)
        self._root.geometry(window_size)

        self._game_control_buttons = ButtonsHolder(
            self._root,
            row=0, 
            rows_num=1,
            columns_num=2,
            buttons=[
                ButtonMeta(
                    Coords(0, 0),
                    'new'
                ),
                ButtonMeta(
                    Coords(0, 1),
                    'quit'
                ),
            ]
        )
        self._game_process_buttons = ButtonsHolder(
            self._root,
            row=1,
            rows_num=4,
            columns_num=4,
            buttons=[
                ButtonMeta(
                    Coords(x // 4, x % 4),
                    str(x),
                )
                for x in range(0, 15)
            ]
        )
        self._root.mainloop()


class ButtonsHolder:
    def __init__(
        self,
        root,
        row,
        rows_num,
        columns_num,
        buttons=[]
    ):
        self._frame = tkinter.Frame(root)
        self._frame.grid(row=row)
        self._buttons = []

        for row in range(rows_num):
            self._frame.rowconfigure(row, weight=1)
            for column in range(columns_num):
	            self._frame.columnconfigure(column, weight=1)

        for btn in buttons:
            self.add_button(btn)

    def add_button(self, btn):
        self._buttons.append(
            {
                'source': tkinter.Button(self._frame, text=btn.text, command=btn.click),
                'meta': btn,
            }
        )
        self._refresh_view()

    def _refresh_view(self):
        for btn in self._buttons:
            btn_meta = btn['meta']
            btn_source = btn['source']
            btn_source.grid(row=btn_meta.row, column=btn_meta.column)


class ButtonMeta:
    def __init__(self, coords, text):
        self.row = coords.row
        self.column = coords.column
        self.text = text

    @property
    def coords(self):
        return Coords(self.row, self.column)

    def click(self):
        print(f'btn {self.text} clicked')

@dataclass
class Coords:
    row: int
    column: int
