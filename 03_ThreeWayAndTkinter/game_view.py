import tkinter
import tkinter.messagebox as mb

from common import ButtonMeta
from common import Coords

import consts

class GameView:
    def __init__(self, rang, title, window_size, game_process):
        self._root = tkinter.Tk()
        self._root.title(title)
        self._root.geometry(window_size)
        self._root.rowconfigure(0, weight=1)
        self._root.columnconfigure(0, weight=1)
        self._root.rowconfigure(1, weight=4)
        self._rang = rang
        self._game_process = game_process

        self._game_control_buttons_holder = ButtonsHolder(
            self._root,
            self,
            row=0, 
            rows_num=1,
            columns_num=2,
            buttons={
                'new': ButtonMeta(
                    Coords(0, 0),
                    self._new_button_handler,
                ),
                'quit': ButtonMeta(
                    Coords(0, 1),
                    self._quit_button_handler,
                ),
            }
        )
        self._game_process_buttons_holder = ProcessButtonsHolder(
            self._root,
            self,
            row=1,
            rows_num=self._rang,
            columns_num=self._rang,
            buttons=self._game_process.buttons
        )
        self.draw()
        self._root.mainloop()

    def draw(self):
        self._game_control_buttons_holder.refresh_view()
        self._game_process_buttons_holder.refresh_view()

    def _new_button_handler(self):
        self._game_process_buttons_holder.clean_frame()
        self._game_process.arrange_buttons()
        self._game_process_buttons_holder.new_buttons(
            self._game_process.buttons
        )
        self._game_process_buttons_holder.refresh_view()

    def _quit_button_handler(self):
        self._root.quit()
        self._root.destroy()


class ButtonsHolder:
    def __init__(
        self,
        root,
        game_view,
        row,
        rows_num,
        columns_num,
        buttons,
    ):
        self._game_view = game_view
        self._frame = tkinter.LabelFrame(root)
        self._frame.grid(row=row, sticky=consts.STICKY_ALL)
        self._buttons = {}

        for row in range(rows_num):
            self._frame.rowconfigure(row, weight=1)
            for column in range(columns_num):
	            self._frame.columnconfigure(column, weight=1)
        
        self.new_buttons(buttons)

    def add_button(self, id, btn):
        self._buttons[id] = {
            'source': tkinter.Button(
                self._frame,
                text=id,
                command=btn.handler
            ),
            'meta': btn,
        }

    def refresh_view(self):
        for id, btn in self._buttons.items():
            if id == consts.EMPTY_BUTTON_ID:
                continue
            btn_meta = btn['meta']
            btn_source = btn['source']
            btn_source.grid(
                row=btn_meta.coords.row,
                column=btn_meta.coords.column,
                sticky=consts.STICKY_ALL
            )

    def new_buttons(self, buttons):
        for id, btn in buttons.items():
            self.add_button(id, btn)

    def clean_frame(self):
        for btn in self._frame.winfo_children():
            btn.destroy()


class ProcessButtonsHolder(ButtonsHolder):
    def add_button(self, id, btn):
        self._buttons[id] = {
            'source': tkinter.Button(
                self._frame,
                text=id,
                command=lambda: self._btn_click(btn.handler)
            ),
            'meta': btn,
        }

    def _btn_click(self, btn_handler):
        btn_handler()
        self.refresh_view()
        if self._game_view._game_process.check_finish():
            mb.showinfo(
                'You win',
                'You win! Click ok to start new game.',
            )
            self._game_view._new_button_handler()
