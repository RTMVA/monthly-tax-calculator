from tkinter import*
from customtkinter import*
from icons import*

#window config
root = Tk()
root.geometry("715x780")
root.title("Monthly Tax Calculator")
root.resizable(False,False)

#canvas where i will place my widgets
canvas = Canvas(
    root,
    width = 780,
    height = 780,
)

canvas.place(
    x = 0,
    y = 0,
    relwidth = 1,
    relheight = 1
)



#title frame , different colour
title_frame = CTkFrame(
    root,
    width = 800,
    height = 130,
    fg_color = "#6640e9",
)
canvas.create_window(390,60,window = title_frame)

#Label within frame
Monthly_taxTitle = CTkLabel(
    root,
    text = "Monthly Tax Calculator",
    font = ("Arial",21,"bold"),
    fg_color = "#6640e9",
    bg_color = "#6640e9",
    text_color= "White"
)
canvas.create_window(390,35,window = Monthly_taxTitle)

moneybag_logo = Image.open("Money_baglogo.png").convert("RGBA")
moneybag_img = ImageTk.PhotoImage(moneybag_logo)
moneybag_imglabel = CTkLabel(
    root,
    image = moneybag_img,
    text = "",
    fg_color = "#6640e9",
    bg_color = "#6640e9"
)
canvas.create_window(150,30,window = moneybag_imglabel)


#sublabel within frame
catch_phrase = CTkLabel(
    root,
    text = "Your monthly take home-pay calculated to perfection",
    font = ("Arial",13),
    fg_color = "#6640e9",
    bg_color = "#6640e9",
    text_color= "White"
)
canvas.create_window(390,60,window = catch_phrase)

#Frame Left Earnings Information
frame_earningsInformation = CTkFrame(
    root,
    width = 320,
    height = 465,
    fg_color = "#f8fafc",
    corner_radius = 15,
    border_width = 2,
    border_color = "#6640e9"
    
)
canvas.create_window(175,393,window = frame_earningsInformation)

bookbag_icon = Image.open("bookbag.png").convert("RGBA")
bookbag_img = ImageTk.PhotoImage(bookbag_icon)
bookbag_label = CTkLabel(
    root,
    width=5,
    image = bookbag_img,
    text = "  Earnings Information",
    font = ("Arial",16,"bold"),
    fg_color = "#f8fafc",
    bg_color = "#f8fafc",
    compound = "left"
) 
canvas.create_window(130,192,window = bookbag_label)

Hourly_wageL = CTk

















#Frame Right Deducations & Contributions
frame_deductions = CTkFrame(
    root,
    width = 320,
    height = 465,
    fg_color = "#f8fafc",
    corner_radius = 15,
    border_width = 2,
    border_color = "#6640e9"
)
canvas.create_window(540,393,window = frame_deductions)







root.mainloop()