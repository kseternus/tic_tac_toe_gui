import tkinter as tk


def new_game():
    global player

    player = players[0]
    info_label.config(text=f'It is {player} turn')
    for row in range(3):
        for column in range(3):
            fields[row][column].config(text='', foreground='#ffffff', background='#373854')


def next_turn(row, column):
    global player

    if fields[row][column]['text'] == '' and check_winner() is False:
        if player == players[0]:
            fields[row][column]['text'] = player
            if check_winner() is False:
                player = players[1]
                info_label.config(text=f'It is {player} turn')
            elif check_winner() is True:
                info_label.config(text=f'{players[0]} wins!')
            elif check_winner() == 'Tie':
                info_label.config(text='It is a tie!')
        else:
            fields[row][column]['text'] = player
            if check_winner() is False:
                player = players[0]
                info_label.config(text=f'It is {player} turn')
            elif check_winner() is True:
                info_label.config(text=f'{players[1]} wins!')
            elif check_winner() == 'Tie':
                info_label.config(text='It is a tie!')


def check_winner():
    for row in range(3):
        if fields[row][0]['text'] == fields[row][1]['text'] == fields[row][2]['text'] != '':
            fields[row][0].config(foreground='#7bb3ff', background='#493267')
            fields[row][1].config(foreground='#7bb3ff', background='#493267')
            fields[row][2].config(foreground='#7bb3ff', background='#493267')
            return True

    for column in range(3):
        if fields[0][column]['text'] == fields[1][column]['text'] == fields[2][column]['text'] != '':
            fields[0][column].config(foreground='#7bb3ff', background='#493267')
            fields[1][column].config(foreground='#7bb3ff', background='#493267')
            fields[2][column].config(foreground='#7bb3ff', background='#493267')
            return True

    if fields[0][0]['text'] == fields[1][1]['text'] == fields[2][2]['text'] != '':
        fields[0][0].config(foreground='#7bb3ff', background='#493267')
        fields[1][1].config(foreground='#7bb3ff', background='#493267')
        fields[2][2].config(foreground='#7bb3ff', background='#493267')
        return True

    elif fields[0][2]['text'] == fields[1][1]['text'] == fields[2][0]['text'] != '':
        fields[0][2].config(foreground='#7bb3ff', background='#493267')
        fields[1][1].config(foreground='#7bb3ff', background='#493267')
        fields[2][0].config(foreground='#7bb3ff', background='#493267')
        return True

    elif empty_fields() is False:
        return 'Tie'

    else:
        return False


def empty_fields():
    e_fields = 9

    for row in range(3):
        for column in range(3):
            if fields[row][column]['text'] != '':
                e_fields -= 1

    if e_fields == 0:
        return False
    else:
        return True


root = tk.Tk()
root.title('Tic Tac Toe')
root.geometry('640x680')
root.resizable(False, False)
root.config(background='#373854')

players = ['X', 'O']
player = players[0]
fields = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

fields_frame = tk.Frame(root)
fields_frame.pack(pady=(20, 0))

for row in range(3):
    for column in range(3):
        fields[row][column] = tk.Button(fields_frame, text='', font='Calibri 64', width=4, height=1,
                                        foreground='#ffffff', background='#373854', activebackground='#493267',
                                        activeforeground='#ffffff',
                                        command= lambda row=row, column=column: next_turn(row, column))
        fields[row][column].grid(row=row, column=column)

info_label = tk.Label(root, text=f'It is {player} turn', font='Calibri 28', foreground='#ffffff', background='#373854')
info_label.pack()

new_game_button = tk.Button(root, text='New Game', font='Calibri 16', foreground='#ffffff', background='#373854',
                            activebackground='#493267', activeforeground='#ffffff', command=new_game)
new_game_button.pack()

root.mainloop()
