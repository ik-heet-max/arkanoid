import tkinter
import time
from ball import Ball
from paddle import Paddle
from score import Score

widget = tkinter.Tk()
widget.title = ('Game')
widget.resizable(0, 0)
widget.wm_attributes('-topmost', 1)
canvas = tkinter.Canvas(widget, width=500, height=400, highlightthickness=0)
canvas.pack()
widget.update()

if __name__ == '__main__':
    score = Score(canvas, 'green')
    paddle = Paddle(canvas, 'black')
    ball = Ball(canvas, paddle, score, 'blue')
    try:
        while not ball.hit_bottom:
            if paddle.started == True:
                ball.draw()
                paddle.draw()
            widget.update_idletasks()
            widget.update()
            time.sleep(0.01)
        time.sleep(3)
    except KeyboardInterrupt:
        mainloop()
