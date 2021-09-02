import tkinter as tk
expression = ""


def press(num):
  global expression

  expression = expression + str(num)

  equation.set(expression)


def equalpress():
  try:
    global expression

    total = str(eval(expression))

    equation.set(total)

    expression = ""

  except BaseException as e:
    equation.set(e)
    expression = ""


def clear():
  global expression
  expression = ""
  equation.set("")


if __name__ == "__main__":
  gui = tk.Tk()

  fg = 'black'
  bg = 'white'

  gui.configure(background="teal")

  gui.title("Calculator")

  gui.geometry("270x150")

  equation = tk.StringVar()

  expression_field = tk.Entry(gui, textvariable=equation)

  expression_field.grid(columnspan=4, ipadx=70)

  button1 = tk.Button(gui, text=' 1 ', fg=fg, bg=bg,
                      command=lambda: press(1), height=1, width=7)
  button1.grid(row=2, column=0)

  button2 = tk.Button(gui, text=' 2 ', fg=fg, bg=bg,
                      command=lambda: press(2), height=1, width=7)
  button2.grid(row=2, column=1)

  button3 = tk.Button(gui, text=' 3 ', fg=fg, bg=bg,
                      command=lambda: press(3), height=1, width=7)
  button3.grid(row=2, column=2)

  button4 = tk.Button(gui, text=' 4 ', fg=fg, bg=bg,
                      command=lambda: press(4), height=1, width=7)
  button4.grid(row=3, column=0)

  button5 = tk.Button(gui, text=' 5 ', fg=fg, bg=bg,
                      command=lambda: press(5), height=1, width=7)
  button5.grid(row=3, column=1)

  button6 = tk.Button(gui, text=' 6 ', fg=fg, bg=bg,
                      command=lambda: press(6), height=1, width=7)
  button6.grid(row=3, column=2)

  button7 = tk.Button(gui, text=' 7 ', fg=fg, bg=bg,
                      command=lambda: press(7), height=1, width=7)
  button7.grid(row=4, column=0)

  button8 = tk.Button(gui, text=' 8 ', fg=fg, bg=bg,
                      command=lambda: press(8), height=1, width=7)
  button8.grid(row=4, column=1)

  button9 = tk.Button(gui, text=' 9 ', fg=fg, bg=bg,
                      command=lambda: press(9), height=1, width=7)
  button9.grid(row=4, column=2)

  button0 = tk.Button(gui, text=' 0 ', fg=fg, bg=bg,
                      command=lambda: press(0), height=1, width=7)
  button0.grid(row=5, column=0)

  plus = tk.Button(gui, text=' + ', fg=fg, bg=bg,
                   command=lambda: press("+"), height=1, width=7)
  plus.grid(row=2, column=3)

  minus = tk.Button(gui, text=' - ', fg=fg, bg=bg,
                    command=lambda: press("-"), height=1, width=7)
  minus.grid(row=3, column=3)

  multiply = tk.Button(gui, text=' * ', fg=fg, bg=bg,
                       command=lambda: press("*"), height=1, width=7)
  multiply.grid(row=4, column=3)

  divide = tk.Button(gui, text=' / ', fg=fg, bg=bg,
                     command=lambda: press("/"), height=1, width=7)
  divide.grid(row=5, column=3)

  equal = tk.Button(gui, text=' = ', fg=fg, bg=bg,
                    command=equalpress, height=1, width=7)
  equal.grid(row=5, column=2)

  clear = tk.Button(gui, text='Clear', fg=fg, bg=bg,
                    command=clear, height=1, width=7)
  clear.grid(row=5, column='1')

  Decimal = tk.Button(gui, text='.', fg=fg, bg=bg,
                      command=lambda: press('.'), height=1, width=7)
  Decimal.grid(row=6, column=0)

  gui.mainloop()
