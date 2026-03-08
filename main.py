import tkinter
import random

root =tkinter.Tk()
root.title("Minesweeper Game")

geometry = 900
geo_height = geometry+30
geometry_infuc = f"{geometry}x{geo_height-7}"
root.geometry(geometry_infuc)


col_and_row = 9#can't be blow 9
law_of_bomb_num=round((30/7*col_and_row)-28.51714)
name_title=tkinter.Label(root, text=f"Number of MINE: {law_of_bomb_num} | Winning Probalility: {round(100-(law_of_bomb_num/int(col_and_row^2)))}%",font=("Arial", 0), anchor="w")
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
        inno_bomb_count+=99
    
    return inno_bomb_count


#restart button, revealed button(notice messagebox**)


#7 bombs

#when the game start, all the boxes are blank.
#when one of the box is click, the text are revealed
#the clicked one has to be 0
  #untiled the click one checker(row, col), while if ending = False continue else, ending = True 

#box data include key btn_11: bomb, btn_12: 2

global begin
begin = True
def box_text(row, col):
    if begin:
        if checker(row, col): #it takes the last bom_row and bomb_col
                return "B"
        else:
                return bomb_counter(row, col)
    return ""
clicked_time=0
bomb_coordinate = []
def clicked(r, c):
    global clicked_time
    clicked_time+=1
    print("Clicked time:",clicked_time)
    global clicked_col
    global clicked_row
    clicked_row = r
    clicked_col = c
    global bomb_coordinate
    number_of_bombs=law_of_bomb_num
    #bomb generator
    if clicked_time == 1:
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
    if clicked_time==1:
        while not bomb_counter(clicked_row, clicked_col) == 0:
            bomb_coordinate = []
            bomb_generator()


    def checker_infunc(row, col):
            #row --> count, count a tine loop check
            for i in bomb_coordinate:
                if row==i[0] and col==i[1]: # if 1 is exit, it only check one time
                    return True
            return False
    print("Is it a bomb? check_infunc:",checker_infunc(clicked_row, clicked_col))
    print("Is it a bomb? checker:",checker(clicked_row, clicked_col))
    print("coordinated of the clicked box:",(r, c))
    print("all coordinate of the bombs:",bomb_coordinate)
    print('----------------------------------------------------------\n')
    buttons[(r, c)].config(
        text=(box_text(r, c)),
        bg="#B8E5B8",
        font=("Arial",18, "bold")
        )

#box button generator
buttons = {}
btn_dimension=int((900/col_and_row)-4)
pixel_virtual = tkinter.PhotoImage(width=1, height=1)
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
root.mainloop()