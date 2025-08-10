from tkinter import*
from customtkinter import*
from icons import*
from Logic import*

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
    fg_color = "#5b43e7",
    bg_color = "#5b43e7",
    text_color= "White"
)
canvas.create_window(390,35,window = Monthly_taxTitle)

moneybag_logo = Image.open("Money_baglogo.png").convert("RGBA")
moneybag_img = ImageTk.PhotoImage(moneybag_logo)
moneybag_imglabel = CTkLabel(
    root,
    image = moneybag_img,
    text = "",
    fg_color = "#5b43e7",
    bg_color = "#5b43e7"
)
canvas.create_window(250,30,window = moneybag_imglabel)


#sublabel within frame
catch_phrase = CTkLabel(
    root,
    text = "Your monthly take home-pay calculated with precision",
    font = ("Arial",13),
    fg_color = "#5b43e7",
    bg_color = "#5b43e7",
    text_color= "White"
)
canvas.create_window(390,60,window = catch_phrase)

tax_code = CTkLabel(
    root,
    text = "Based on tax-code 1257L",
    text_color = "#717579",
    font = ("Arial",12,"bold"),
    fg_color = "#5b43e7",
    bg_color = "#5b43e7",
)
canvas.create_window(640,10,window = tax_code)

def create_earnings_information_frame(root,canvas):
    """
    Sets up the left-side Earnings Infromation which includes:
    -Hourly wage input
    -Monthly hours input
    -Monthly salary calcualtion 
    -Fixed salary override option
    """


    #--- Container Frame ---
    frame_earningsInformation = CTkFrame(
        root,
        width = 320,
        height = 505,
        fg_color = "#f8fafc",
        corner_radius = 15,
        border_width = 2,
        border_color = "#5b43e7"
        )
    canvas.create_window(175,408,window = frame_earningsInformation)

    #---Bookbag icon with Header---
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
    canvas.create_window(130,177,window = bookbag_label)

    #---Hourly Wage Label---
    Hourly_wageL = CTkLabel(
        root,
        text = "Hourly Wage",
        text_color= "#212121",
        font = ("Segui UI",13,"bold"),
        fg_color = "#f8fafc",
        bg_color = "#f8fafc"
    )
    canvas.create_window(78,210,window = Hourly_wageL)

    #---Hourly wage entry widget---
    hourlywage_entry = CTkEntry(
        root,
        width = 260,
        height = 48,
        corner_radius = 10,
        font = ("Segui UI",15,"bold"),
    )
    hourlywage_entry.insert(0,"£14.16")
    canvas.create_window(168,250,window = hourlywage_entry)

    #---hourly rate info label---
    info_hourlywage = CTkLabel(
        root,
        text = "Your hourly rate of pay",
        text_color= "#717579",
        fg_color = "#f8fafc",
        bg_color = "#f8fafc",
        font = ("Comic Sans Ms",11)
    )
    canvas.create_window(100,288,window = info_hourlywage)

    #---Monthly hours label---
    monthly_hourlabel = CTkLabel(
        root,
        text = "Monthly Work Hours",
        text_color= "#212121",
        fg_color = "#f8fafc",
        bg_color = "#f8fafc",
        font = ("Segui UI",13,"bold")
    )
    canvas.create_window(100,318,window = monthly_hourlabel)

    #---monthly hours entry widget---
    monthlyHours_entry = CTkEntry(
        root,
        width = 260,
        height = 48,
        corner_radius = 10,
        font = ("Segui UI",15,"bold"),
    )
    monthlyHours_entry.insert(0,"160")
    canvas.create_window(168,358,window = monthlyHours_entry)

    #---monthly hours info label---
    tip_monthlyHours = CTkLabel(
        root,
        text = "Total hours worked per month",
        text_color= "#717579",
        fg_color = "#f8fafc",
        bg_color = "#f8fafc",
        font = ("Comic Sans Ms",11)
    )
    canvas.create_window(112,397,window = tip_monthlyHours)

    #---calcualtion preview frame---
    tip_calculatedFrame = CTkFrame(
        root,
        width = 270,
        height = 75,
        fg_color = "#e6f5fd",
        corner_radius = 15,
        border_width = 2,
        border_color = "#3399cc",
        bg_color = "#f8fafc"
    )
    canvas.create_window(170,455,window = tip_calculatedFrame)

    #---title for tip label---
    mcalSalarayLabel = CTkLabel(
        root,
        text = "(EG)Calculated Monthly Salary",
        text_color= "#003366",
        bg_color = "#e6f5fd",
        font = ("Segui UI",13,"bold"),
        fg_color = "#e6f5fd"
    )
    canvas.create_window(145,445,window = mcalSalarayLabel)

    #---monthly pay tip label---
    tip_calculation = 14.16 * 160
    calculatedSalaray = CTkLabel(
        root,
        text = f"£14.16 x 160 hours = {tip_calculation}",
        text_color= "#003366",
        bg_color = "#e6f5fd",
        font = ("Segui UI",13),
        fg_color = "#e6f5fd"
    )
    calc_placement = canvas.create_window(133,470,window = calculatedSalaray)

    #---Alternative monthly salary label---
    or_option = CTkLabel(
        root,
        text = "Annual Gross Income ",
        text_color = "#212121",
        bg_color = "#f8fafc",
        fg_color = "#f8fafc",
        font = ("Segui UI",13,"bold")
    )
    canvas.create_window(108,515,window = or_option)

    #---Gross income input widget---
    Yearly_grossIncome = CTkEntry(
        root,
        width = 260,
        height = 48,
        corner_radius = 10,
        font = ("Segui UI",15,"bold"),
    )
    Yearly_grossIncome.insert(0,"£1000")
    canvas.create_window(163,555,window = Yearly_grossIncome)

    #alternative tip label
    override_label = CTkLabel(
        root,
        text = "Enter your expected gross income for the current tax year ",
        text_color = "#717579",
        bg_color = "#f8fafc",
        fg_color = "#f8fafc",
        font = ("Comic Sans MS",11)
    )
    canvas.create_window(175,595,window = override_label)

    override_label2 = CTkLabel(
        root,
        text = "(6 April 2025 to 5 April 2026):",
        text_color = "#717579",
        bg_color = "#f8fafc",
        fg_color = "#f8fafc",
        font = ("Comic Sans MS",11)
    )
    canvas.create_window(105,615,window = override_label2)
    

    return hourlywage_entry.get(),monthlyHours_entry.get(),Yearly_grossIncome.get()

create_earnings_information_frame(root,canvas)








def create_deductions_frame(root,canvas):
    """
    Sets up the right-side of the window which includes:
    -Pension Contribution input
    -Other decutions
    -Override for National insurance
    """

    #---container frame---
    frame_deductions = CTkFrame(
        root,
        width = 320,
        height = 505,
        fg_color = "#f8fafc",
        corner_radius = 15,
        border_width = 2,
        border_color = "#6640e9"
    )
    canvas.create_window(540,410,window = frame_deductions)

    st = Image.open("Stats.png").convert("RGBA")
    stats_image = ImageTk.PhotoImage(st)

    #---logistics icon with title label---
    right_frameTitle = CTkLabel(
        root,
        width = 5,
        image = stats_image,
        text ="  Deductions & Contributions",
        text_color = "#212121",
        font = ("Arial",16,"bold"),
        bg_color = "#f8fafc",
        fg_color = "#f8fafc",
        compound = "left"
    )
    canvas.create_window(520,192,window = right_frameTitle)

    #---Pension Contribution label---
    pension_contributionL = CTkLabel(
        root,
        text = "Pension Contribution",
        text_color= "#212121",
        font = ("Segui UI",13,"bold"),
        fg_color = "#f8fafc",
        bg_color = "#f8fafc"
    )
    canvas.create_window(470,225,window = pension_contributionL)

    #---Pension Contribution entry widget---
    pensionContri_entry = CTkEntry(
        root,
        width = 260,
        height = 48,
        corner_radius = 10,
        font = ("Segui UI",15,"bold"),
    )
    pensionContri_entry.insert(0,"£24.00")
    canvas.create_window(535,265,window = pensionContri_entry)

    #--Pension Contribution info_label
    pension_contributionInfoL = CTkLabel(
        root,
        text = "Monthly pension scheme contribution",
        text_color= "#717579",
        fg_color = "#f8fafc",
        bg_color = "#f8fafc",
        font = ("Comic Sans Ms",11)
    )
    canvas.create_window(499,303,window = pension_contributionInfoL)

    #---Other Deductions label---
    pension_contributionL = CTkLabel(
        root,
        text = "Other deductions",
        text_color= "#212121",
        font = ("Segui UI",13,"bold"),
        fg_color = "#f8fafc",
        bg_color = "#f8fafc"
    )
    canvas.create_window(458,335,window = pension_contributionL)

    #---Other Dection input widget---
    other_DeductionEntry = CTkEntry(
        root,
        width = 260,
        height = 48,
        corner_radius = 10,
        font = ("Segui UI",15,"bold"),
    )
    other_DeductionEntry.insert(0,"£0.00")
    canvas.create_window(530,375, window = other_DeductionEntry)

    #---other decutions info label---
    otherInfoL = CTkLabel(
        root,
        text = "Union fees, loans, benefits, etc.",
        text_color= "#717579",
        fg_color = "#f8fafc",
        bg_color = "#f8fafc",
        font = ("Comic Sans Ms",11)
    )
    canvas.create_window(485,413,window = otherInfoL)

    #---National Insurance override---
    national_InsuranceOVL = CTkLabel(
        root,
        text = "National Insurance Override",
        text_color= "#212121",
        font = ("Segui UI",13,"bold"),
        fg_color = "#f8fafc",
        bg_color = "#f8fafc"
    )
    canvas.create_window(491,447,window = national_InsuranceOVL)

    #---National Insurance input widget---
    national_insuranceEntry = CTkEntry(
        root,
        width = 260,
        height = 48,
        corner_radius = 10,
        font = ("Segui UI",15,"bold"),
        text_color = "#717579",
    )
    national_insuranceEntry.insert(0,"£Auto-calculated")
    canvas.create_window(530,490, window = national_insuranceEntry)

    #---National Insureance info label---
    nATInfoL = CTkLabel(
        root,
        text = "leave blank for automatic calculation",
        text_color= "#717579",
        fg_color = "#f8fafc",
        bg_color = "#f8fafc",
        font = ("Comic Sans Ms",11)
    )
    canvas.create_window(495,528,window = nATInfoL)

create_deductions_frame(root,canvas)

#---Button for calculating the take-home Pay---
calc_img = Image.open("calculator.png").convert("RGBA")
calculator_img = ImageTk.PhotoImage(calc_img)

rate, hours , monthly_income = create_earnings_information_frame(root,canvas)
Grossmonthly_income = calc_monthlyIncome(hours,rate)




def summary_page():
    """
    Opens a Toplevel window once the Calculate take home pay button has been clicked
    -displays gross monthly salary
    -displays PAYE tax
    -displays National Insurance
    -displays pension Contributions
    -displays any other deductions
    -displays the total amount of deductions
    - Displays the Total net take home-pay
    """

    #---window config---
    window = Toplevel()
    window.geometry("700x500")
    window.title("Calculation Breakdown")

    #---canvas for flexible widget placement---
    canva = Canvas(
        window,
        width = 700,
        height = 500,
        bg = "#f8fafc",
    )
    canva.place(
        x = 0,
        y = 0,
        relheight = 1,
        relwidth = 1,
    )

    calc_breakdownimg = Image.open("calc_breakdown.png").convert("RGBA")

    

Calc_TakehomePayButton = CTkButton(
    root,
    text = "Calculate take Home Pay",
    width = 300,
    height = 50,
    image = calculator_img,
    corner_radius = 20,
    bg_color = "#f0f0f0",
    fg_color = "#6640e9",
    font = ("Arial",18,"bold"),
    text_color = "#f0f0f0",
    compound = "left",
    hover_color = "#6640e9",
    command = summary_page
)
canvas.create_window(355,700, window = Calc_TakehomePayButton)










root.mainloop()