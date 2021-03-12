from random import shuffle

from common import ButtonMeta
from common import Coords

import consts


class GameProcess:
    def __init__(self, rang,):
        self._rang = rang
        self.arrange_buttons()

    def arrange_buttons(self):
        self.buttons = {}
        rang = self._rang
        ids = list(range(rang * rang))
        shuffle(ids)
        ids = (x for x in ids)
        for row in range(rang):
            for column in range(rang):
                id = next(ids)
                self.buttons[id] = ButtonMeta(
                    Coords(row, column),
                    handler=lambda id=id: self._button_click(id)
                )

    def _button_click(self, id):
        empty_btn = self.buttons[consts.EMPTY_BUTTON_ID]
        cur_btn = self.buttons[id]
        if (
            abs(empty_btn.coords.row - cur_btn.coords.row) +
            abs(empty_btn.coords.column - cur_btn.coords.column)
        ) > 1:
            return
        tmp_empty_btn_coords = empty_btn.coords
        empty_btn.coords = cur_btn.coords
        cur_btn.coords = tmp_empty_btn_coords

    def check_finish(self):
        right_border = self._rang * self._rang
        for i in range(right_border):
            cur_id = (i + 1) % right_border
            cur_row = self.buttons[cur_id].coords.row
            cur_column = self.buttons[cur_id].coords.column
            if (
                cur_row != i // self._rang or
                cur_column != i % self._rang
            ):
                return False
        
        return True
