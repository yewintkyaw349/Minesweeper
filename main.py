import tkinter
import random
import time
from tkinter import messagebox

root =tkinter.Tk()
root.title("Minesweeper Game")

geometry = 900
geo_height = geometry+30
geometry_infuc = f"{geometry}x{geo_height-7}"
root.geometry(geometry_infuc)

col_and_row = 9#can't be blow 9
law_of_bomb_num=round((30/7*col_and_row)-28.51714)
name_title=tkinter.Label(root, text=f"Number of MINE: {law_of_bomb_num} | Winning Probalility: {round(100-(law_of_bomb_num/int(col_and_row*col_and_row)*100))}%",font=("Arial", 0), anchor="w")
name_title.grid(row=0, column=0, columnspan=col_and_row)


#bomb: bg color, reveal, lose messagebox - add background color for bomb and lose
#0: no text for 0 - reveal
def checker(row, col):
    #row --> count, count a tine loop check
    for i in bomb_coordinate:
        if row==i[0] and col==i[1]: # if 1 is exit, it only check one time
            return True
    return False
    # True = the coordinate is a bomb
    # False = the coordinate is not a bomb
def surrending_zero_checker(row, col):
    reveal_coordinate = []
    #if text(r,c) == 0: if text
    if bomb_counter(row+1, col) == 0:
        reveal_coordinate.append([row+1, col])
    if bomb_counter(row-1, col) == 0:
        reveal_coordinate.append([row-1, col])
    if bomb_counter(row, col+1) == 0:
        reveal_coordinate.append([row, col+1])
    if bomb_counter(row, col-1) == 0:
        reveal_coordinate.append([row, col-1])
    if bomb_counter(row+1, col+1) == 0:
        reveal_coordinate.append([row+1, col+1])
    if bomb_counter(row+1, col-1) == 0:
        reveal_coordinate.append([row+1, col-1])
    if bomb_counter(row-1, col+1) == 0:
        reveal_coordinate.append([row-1, col+1])
    if bomb_counter(row-1, col-1) == 0:
        reveal_coordinate.append([row-1, col-1])
    return reveal_coordinate

revealed = []#use set!!!!!!!!!!!! for winning
def surrending_zero_reveal(row, col):
    #if text(r,c) == 0: if text
    #အောက်ကို ဆင်း အပေါ်ပြန်တတ် nk လည် နေတာ 
    global revealed
    if bomb_counter(row, col) == 0:
        if bomb_counter(row+1, col) >= 0 and [row+1, col] in valid_button and not [row+1, col] in revealed: # wall ပိတ်ရင် လည်းရေ ေအာင် 
            buttons[(row+1, col)].config(
                text=(box_text(row+1, col)),
                bg="#B8E5B8",
                font=("Arial",18, "bold")
                )
            revealed.append([row+1, col])
            surrending_zero_reveal(row+1, col)
        if bomb_counter(row-1, col) >= 0 and [row-1, col] in valid_button and not [row-1, col] in revealed:
            buttons[(row-1, col)].config(
                text=(box_text(row-1, col)),
                bg="#B8E5B8",
                font=("Arial",18, "bold")
                )
            revealed.append([row-1, col])
            surrending_zero_reveal(row-1, col)
        if bomb_counter(row, col+1) >= 0 and [row, col+1] in valid_button and not [row, col+1] in revealed:
            buttons[(row, col+1)].config(
                text=(box_text(row, col+1)),
                bg="#B8E5B8",
                font=("Arial",18, "bold")
                )
            revealed.append([row, col+1])
            surrending_zero_reveal(row, col+1)
        if bomb_counter(row, col-1) >= 0 and [row, col-1] in valid_button and not [row, col-1] in revealed:
            buttons[(row, col-1)].config(
                text=(box_text(row, col-1)),
                bg="#B8E5B8",
                font=("Arial",18, "bold")
                )
            revealed.append([row, col-1])
            surrending_zero_reveal(row, col-1)
        if bomb_counter(row+1, col+1) >= 0 and [row+1, col+1] in valid_button and not [row+1, col+1] in revealed:
            buttons[(row+1, col+1)].config(
                text=(box_text(row+1, col+1)),
                bg="#B8E5B8",
                font=("Arial",18, "bold")
                )
            revealed.append([row+1, col+1])
            surrending_zero_reveal(row+1, col+1)
        if bomb_counter(row+1, col-1) >= 0 and [row+1, col-1] in valid_button and not [row+1, col-1] in revealed:
            buttons[(row+1, col-1)].config(
                text=(box_text(row+1, col-1)),
                bg="#B8E5B8",
                font=("Arial",18, "bold")
                )
            revealed.append([row+1, col-1])
            surrending_zero_reveal(row+1, col-1)
        if bomb_counter(row-1, col+1) >= 0 and [row-1, col+1] in valid_button and not [row-1, col+1] in revealed:
            buttons[(row-1, col+1)].config(
                text=(box_text(row-1, col+1)),
                bg="#B8E5B8",
                font=("Arial",18, "bold")
                )
            revealed.append([row-1, col+1])
            surrending_zero_reveal(row-1, col+1)
        if bomb_counter(row-1, col-1) >= 0 and [row-1, col-1] in valid_button and not [row-1, col-1] in revealed:
            buttons[(row-1, col-1)].config(
                text=(box_text(row-1, col-1)),
                bg="#B8E5B8",
                font=("Arial",18, "bold")
                )
            revealed.append([row-1, col-1])
            surrending_zero_reveal(row-1, col-1)
    return

def bomb_counter(row, col):
    #surrending bomb number of each innocent square
    #count the bomb_num
    inno_bomb_count=0
    if checker(row+1, col):
        inno_bomb_count+=1
    if checker(row-1, col):
        inno_bomb_count+=1
    if checker(row, col+1):
        inno_bomb_count+=1
    if checker(row, col-1):
        inno_bomb_count+=1
    if checker(row+1, col+1):
        inno_bomb_count+=1
    if checker(row+1, col-1):
        inno_bomb_count+=1
    if checker(row-1, col+1):
        inno_bomb_count+=1
    if checker(row-1, col-1):
        inno_bomb_count+=1
    if checker(row, col):
        inno_bomb_count-=99
    
    return inno_bomb_count

def box_text(row, col):
    if checker(row, col): #it takes the last bom_row and bomb_col
            return "B"
    elif not checker(row, col):
        if bomb_counter(row, col) == 0:
            return ""
        return bomb_counter(row, col)
    
clicked_time=0
real_click_time = 0
bomb_coordinate = []
def clicked(r, c): #button click
    global clicked_time
    global real_click_time
    local_clicked_time = clicked_time
    local_clicked_time+=1
    global clicked_col
    global clicked_row
    clicked_row = r
    clicked_col = c
    global bomb_coordinate
    number_of_bombs=law_of_bomb_num

    #bomb generator
    if local_clicked_time == 1:
        def bomb_generator():
            for i in range(number_of_bombs):
                condition = False
                    #repeat the randoming until the bomb_counter(r and c) is zero
                while not condition:
                    bomb_row = random.randint(1,col_and_row)
                    bomb_col = random.randint(1,col_and_row)

                    #checking duplication
                    if checker(bomb_row, bomb_col):
                        continue
                    else: 
                        bomb_coordinate.append([bomb_row, bomb_col])
                        condition=True
        bomb_generator()
    if local_clicked_time==1:
        while not bomb_counter(clicked_row, clicked_col) == 0:
            bomb_coordinate = []
            bomb_generator()
    clicked_time=local_clicked_time
    #bomb_generator//

    #result
    if checker(r, c):
        buttons[(r, c)].config(
            text=(box_text(r, c)),
            bg="#FD3131",
            font=("Arial",18, "bold")
            )
        clicked_time=0
        
        messagebox.showinfo("Game Status", "Game Over!")
        game_start()
    else:
        real_click_time+=1
        buttons[(r, c)].config(
            text=(box_text(r, c)),
            bg="#B8E5B8",
            font=("Arial",18, "bold")
            )
        
        #if zero: reveal the surrounding
        if bomb_counter(r, c)==0:
            surrending_zero_reveal(r, c)
        revealed.append([r,c])

        #if zero: reveal the surrounding//
        print (revealed.count)
        if local_clicked_time==( col_and_row*col_and_row - law_of_bomb_num ): #needa fix
            messagebox.showinfo("Game Status", "You Win!")
            game_start()
    print(real_click_time)
#box button generator
buttons = {}
btn_dimension=int((900/col_and_row)-4)
pixel_virtual = tkinter.PhotoImage(width=1, height=1)
def game_start():
    global revealed
    revealed = []
    for row in range(1, col_and_row+1):
        for col in range(1, col_and_row+1):
            btn = tkinter.Button(
                root, 
                image=pixel_virtual,
                width=btn_dimension, 
                height=btn_dimension, 
                compound="c",
                borderwidth=1,
                highlightthickness=0,
                padx=0,
                pady=0,
                command=lambda r=row, c=col: clicked(r, c)
            )
            btn.grid(row=row, column=col)
            buttons[(row, col)] = btn
valid_button = []
for row in range(col_and_row):
    for col in range(col_and_row):
        valid_button.append([row+1, col+1])

game_start()
root.mainloop()