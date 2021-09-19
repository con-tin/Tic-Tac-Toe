from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
turn = "0"
board = ['*','*',"*",
         '*','*','*',
         '*','*','*',]
class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)

class Game(Screen):
    def __init__(self, **kwargs):
        global board
        super(Game, self).__init__(**kwargs)
        board = ['*', '*', "*",
                 '*', '*', '*',
                 '*', '*', '*', ]
        self.main_layout = GridLayout(cols=3)
        self.btn_1 = Button(text="1")
        self.btn_1.bind(on_press=self.on_press)
        self.main_layout.add_widget(self.btn_1)
        self.btn_2 = Button(text="2")
        self.btn_2.bind(on_press=self.on_press)
        self.main_layout.add_widget(self.btn_2)
        self.btn_3 = Button(text="3")
        self.btn_3.bind(on_press=self.on_press)
        self.main_layout.add_widget(self.btn_3)
        self.btn_4 = Button(text="4")
        self.btn_4.bind(on_press=self.on_press)
        self.main_layout.add_widget(self.btn_4)
        self.btn_5 = Button(text="5")
        self.btn_5.bind(on_press=self.on_press)
        self.main_layout.add_widget(self.btn_5)
        self.btn_6 = Button(text="6")
        self.btn_6.bind(on_press=self.on_press)
        self.main_layout.add_widget(self.btn_6)
        self.btn_7 = Button(text="7")
        self.btn_7.bind(on_press=self.on_press)
        self.main_layout.add_widget(self.btn_7)
        self.btn_8 = Button(text="8")
        self.btn_8.bind(on_press=self.on_press)
        self.main_layout.add_widget(self.btn_8)
        self.btn_9 = Button(text="9")
        self.btn_9.bind(on_press=self.on_press)
        self.main_layout.add_widget(self.btn_9)
        self.add_widget(self.main_layout)


    def on_press(self,instance):
        global turn
        global board
        if turn == "0":
            position = int(instance.text) - 1
            board[position] = "0"
            self.display()
            instance.text = "0"
            print("Ходят 0")
            self.win_0()
            turn = "1"


        else:
            position = int(instance.text) - 1
            board[position] = "X"
            self.display()
            print("Ходят X")
            instance.text = "X"
            self.win_x()
            turn = "0"


    def display(self):
        global board
        print(board[0] + ' | ' + board[1] + ' | ' + board[2])
        print(board[3] + ' | ' + board[4] + ' | ' + board[5])
        print(board[6] + ' | ' + board[7] + ' | ' + board[8])


    def win_0(self):
        if board[0] == "0" and board[1] == "0" and board[2] == "0":
            self.reset()
            sm.current = 'win_0'
        elif board[3] == "0" and board[4] == "0" and board[5] == "0":
            self.reset()
            sm.current = 'win_0'
        elif board[6] == "0" and board[7] == "0" and board[8] == "0":
            self.reset()
            sm.current = 'win_0'
        elif board[0] == "0" and board[3] == "0" and board[6] == "0":
            self.reset()
            sm.current = 'win_0'
        elif board[1] == "0" and board[4] == "0" and board[7] == "0":
            self.reset()
            sm.current = 'win_0'
        elif board[2] == "0" and board[5] == "0" and board[8] == "0":
            self.reset()
            sm.current = 'win_0'
        elif board[0] == "0" and board[4] == "0" and board[8] == "0":
            self.reset()
            sm.current = 'win_0'
        elif board[6] == "0" and board[4] == "0" and board[2] == "0":
            self.reset()
            sm.current = 'win_0'
        elif board[0] != "*" and board[1] != "*" and board[2] != "*" and board[3] != "*" and board[4] != "*" and board[
            5] != "*" and board[6] != "*" and board[7] != "*" and board[8] != "*":
            self.reset()
            sm.current = 'draw'

    def win_x(self):
        if board[0] == "X" and board[1] == "X" and board[2] == "X":
            self.reset()
            sm.current = 'win_x'
        elif board[3] == "X" and board[4] == "X" and board[5] == "X":
            self.reset()
            sm.current = 'win_x'
        elif board[6] == "X" and board[7] == "X" and board[8] == "X":
            self.reset()
            sm.current = 'win_x'
        elif board[0] == "X" and board[3] == "X" and board[6] == "X":
            self.reset()
            sm.current = 'win_x'
        elif board[1] == "X" and board[4] == "X" and board[7] == "X":
            self.reset()
            sm.current = 'win_x'
        elif board[2] == "X" and board[5] == "X" and board[8] == "X":
            self.reset()
            sm.current = 'win_x'
        elif board[0] == "X" and board[4] == "X" and board[8] == "X":
            self.reset()
            sm.current = 'win_x'
        elif board[6] == "X" and board[4] == "X" and board[2] == "X":
            self.reset()
            sm.current = 'win_x'
        elif board[0] != "*" and board[1] != "*" and board[2] != "*" and board[3] != "*" and board[4] != "*" and board[
            5] != "*" and board[6] != "*" and board[7] != "*" and board[8] != "*":
            self.reset()
            sm.current = 'draw'

    def reset(self):
        self.btn_1.text="1"
        self.btn_2.text="2"
        self.btn_3.text="3"
        self.btn_4.text="4"
        self.btn_5.text="5"
        self.btn_6.text="6"
        self.btn_7.text="7"
        self.btn_8.text="8"
        self.btn_9.text="9"
class Win_0(Screen):
    def __init__(self, **kwargs):
        super(Win_0, self).__init__(**kwargs)
        global turn

        self.gl = GridLayout(cols=1)
        self.lbl = Label(text="Win 0")
        self.btn = Button(text="Restart")
        self.btn.bind(on_press=self.restart)
        self.gl.add_widget(self.lbl)
        self.gl.add_widget(self.btn)
        self.add_widget(self.gl)
    def restart(self, *args):
        global board
        print(board)
        board = ['*', '*', "*",
                 '*', '*', '*',
                 '*', '*', '*', ]
        print(board)
        sm.current = "game"

class Win_x(Screen):
    def __init__(self, **kwargs):
        super(Win_x, self).__init__(**kwargs)
        global turn

        self.gl = GridLayout(cols=1)
        self.lbl = Label(text="Win X")
        self.btn = Button(text="Restart")
        self.btn.bind(on_press=self.set_screen)
        self.gl.add_widget(self.lbl)
        self.gl.add_widget(self.btn)
        self.add_widget(self.gl)
    def set_screen(self, *args):
        global board
        print(board)
        board = ['*', '*', "*",
                 '*', '*', '*',
                 '*', '*', '*', ]
        print(board)
        sm.current = "game"

class draw(Screen):
    def __init__(self, **kwargs):
        super(draw, self).__init__(**kwargs)
        global turn

        self.gl = GridLayout(cols=1)
        self.lbl = Label(text="Draw")
        self.btn = Button(text="Restart")
        self.btn.bind(on_press=self.set_screen)
        self.gl.add_widget(self.lbl)
        self.gl.add_widget(self.btn)
        self.add_widget(self.gl)
    def set_screen(self, *args):
        global board
        print(board)
        board = ['*', '*', "*",
                 '*', '*', '*',
                 '*', '*', '*', ]
        print(board)
        sm.current = "game"


def set_screen(name_screen):
    sm.current = name_screen

sm = ScreenManagement(transition=FadeTransition())
sm.add_widget(Game(name='game'))
sm.add_widget(Win_0(name='win_0'))
sm.add_widget(Win_x(name='win_x'))
sm.add_widget(draw(name='draw'))



class Application(App):
    def build(self):
        return sm


if __name__ == "__main__":
    Application().run()