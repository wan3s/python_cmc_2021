import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None, title='IvanB', **kwargs):
        super().__init__(master, **kwargs)
        self.master.title(title)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.grid(sticky='NEWS')
        self.create_widgets()

    def create_widgets(self):
        self.label = InputLabel(self)
        self.label.grid(row=0, sticky='NW')

class App(Application):
    def create_widgets(self):
        super().create_widgets()
        self.quit_button = tk.Button(self, text='Quit', command=self.master.quit)
        self.quit_button.grid(row=1, sticky='ES')


class InputLabel(tk.Label):
    _SYMBOL_WIDTH = 7
    _LEFT_OFFSET = 4
    _CARET_POS_Y = 3
    _CARET_WIDTH = 2
    _CARET_HEIGHT = 17

    def __init__(
        self,
        master,
        *args,
        takefocus=1,
        highlightthickness=1,
        **kwargs
    ):
        super().__init__(
            master,
            *args,
            takefocus=takefocus,
            highlightthickness=highlightthickness,
            borderwidth=2,
            relief='groove',
            font='TkFixedFont',
            **kwargs,
        )

        self._caret = tk.Frame(self, bg='green')
        self._caret_pos = self._LEFT_OFFSET

        self.bind('<Any-KeyPress>', self._any_key)
        self.bind('<Button-1>', self._mouse_click)

        self['text'] = 'default text'

    def _any_key(self, event_info):
        text = self['text']
        if event_info.keysym == 'BackSpace':
            if self._caret_pos > 0:
                self['text']=text[:self._caret_pos - 1] + text[self._caret_pos:]
                self._caret_pos -= 1
        elif event_info.keysym == 'Left':
            if self._caret_pos > 0:
                self._caret_pos -= 1
        elif event_info.keysym == 'Right':
            if self._caret_pos < len(text):
                self._caret_pos += 1
        elif event_info.keysym == 'Home':
            self._caret_pos = 0
        elif event_info.keysym == 'End':
            self._caret_pos = len(text)
        elif event_info.char and event_info.char.isprintable():
            self['text']=text[:self._caret_pos] + event_info.char + text[self._caret_pos:]
            self._caret_pos += 1
        self._move_caret()

    def _mouse_click(self, event_info):
        self.focus_set()  
        self._caret_pos = (event_info.x - self._LEFT_OFFSET) // self._SYMBOL_WIDTH
        self._move_caret()

    def _move_caret(self):
        caret_pos = self._LEFT_OFFSET + self._caret_pos * self._SYMBOL_WIDTH
        self._caret.place(
            x=caret_pos,
            y=self._CARET_POS_Y,
            width=self._CARET_WIDTH,
            height=self._CARET_HEIGHT
        )
    

app = App(title='Sample application')
app.mainloop()