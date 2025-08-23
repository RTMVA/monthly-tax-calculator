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

pound_logo = Image.open("pound.png").convert("RGBA")

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
        text = "Hourly Wage*",
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
        text = "Monthly Work Hours*",
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

    return hourlywage_entry,monthlyHours_entry









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
    canvas.create_window(520,177,window = right_frameTitle)

    #---Pension Contribution label---
    pension_contributionL = CTkLabel(
        root,
        text = "Pension Contribution",
        text_color= "#212121",
        font = ("Segui UI",13,"bold"),
        fg_color = "#f8fafc",
        bg_color = "#f8fafc"
    )
    canvas.create_window(470,210,window = pension_contributionL)

    #---Pension Contribution entry widget---
    #pesnsion_contriVar = StringVar(value = "£0")
    pensionContri_entry = CTkEntry(
        root,
        width = 260,
        height = 48,
        corner_radius = 10,
        font = ("Segui UI",15,"bold"),
        #textvariable = pesnsion_contriVar
    )
    
    canvas.create_window(535,250,window = pensionContri_entry)

    #--Pension Contribution info_label
    pension_contributionInfoL = CTkLabel(
        root,
        text = "Monthly pension scheme contribution",
        text_color= "#717579",
        fg_color = "#f8fafc",
        bg_color = "#f8fafc",
        font = ("Comic Sans Ms",11)
    )
    canvas.create_window(499,292,window = pension_contributionInfoL)

    #---Other Deductions label---
    pension_contributionL = CTkLabel(
        root,
        text = "Other deductions",
        text_color= "#212121",
        font = ("Segui UI",13,"bold"),
        fg_color = "#f8fafc",
        bg_color = "#f8fafc"
    )
    canvas.create_window(458,320,window = pension_contributionL)

    #---Other Dection input widget---
    other_DeductionEntry = CTkEntry(
        root,
        width = 260,
        height = 48,
        corner_radius = 10,
        font = ("Segui UI",15,"bold"),
    )
    canvas.create_window(530,360, window = other_DeductionEntry)

    #---other decutions info label---
    otherInfoL = CTkLabel(
        root,
        text = "Union fees, loans, benefits, etc.",
        text_color= "#717579",
        fg_color = "#f8fafc",
        bg_color = "#f8fafc",
        font = ("Comic Sans Ms",11)
    )
    canvas.create_window(485,398,window = otherInfoL)



    def override_ni(national_insuranceEntry):
        if check_nat.get():
            national_insuranceEntry.configure(state = "normal")
            national_insuranceEntry.delete(0,END)
            national_insuranceEntry.configure(text_color = "#212121")
        else:
            national_insuranceEntry.insert(0,"Auto-calculated")
            national_insuranceEntry.configure(text_color = "#717579")
            national_insuranceEntry.configure(state = "disabled")


    #---National Insurance override---
    national_InsuranceOVL = CTkLabel(
        root,
        text = "National Insurance Override",
        text_color= "#212121",
        font = ("Segui UI",13,"bold"),
        fg_color = "#f8fafc",
        bg_color = "#f8fafc"
    )
    canvas.create_window(491,432,window = national_InsuranceOVL)

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
    national_insuranceEntry.configure(state = "disabled")
    canvas.create_window(530,474, window = national_insuranceEntry)

    #---National Insureance info label---
    nATInfoL = CTkLabel(
        root,
        text = "Tick the box to disable auto-calculation",
        text_color= "#717579",
        fg_color = "#f8fafc",
        bg_color = "#f8fafc",
        font = ("Comic Sans Ms",11)
    )
    canvas.create_window(495,513,window = nATInfoL)

#---checkbox widget that indicates whether national insurance value is being overwritten or not---#
    check_nat = IntVar(value = False)
    checkbox = CTkCheckBox(
        root,
        text = "",
        variable = check_nat,
        width= 2,
        height = 2,
        bg_color = "#f8fafc",
        border_color = "#5b43e7",
        hover_color = "white",
        fg_color = "#5b43e7",
        command = lambda:override_ni(national_insuranceEntry)
    )
    canvas.create_window(680,475,window = checkbox)

    return pensionContri_entry,other_DeductionEntry,national_insuranceEntry,check_nat





rate, hours = create_earnings_information_frame(root,canvas)
pension , other , ni , check_nat = create_deductions_frame(root,canvas)








def summary_page(rate,hours,pension,other,ni,root,canvas):
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
        
    rate_r = rate.get()
    hours_r = hours.get()
    pension_r = pension.get()
    other_r = other.get()
    ni_r = ni.get()

    #---logic implementation----
    monthly_income = calc_monthlyIncome(hours_r,rate_r)
    pension_contribution = getpension_contribution(pension_r)
    gross_income = calc_grossIncome(monthly_income)
    other_deductions = getOther_deductions(other_r)
    paye_tax = calc_payeTax(gross_income)
    national_insurance = getNational_Insurance(ni_r,monthly_income)


    total_deductions = calc_total_deductions(pension_contribution,national_insurance,other_deductions,paye_tax)
    take_homepay = calc_take_homepay(total_deductions,monthly_income)

    if monthly_income == 0:
        canvas.delete("delete")
        canvas.create_text(354,140,text = "Invalid Data Input",font = ("Comic Sans MS",12,"bold"),fill = "#FF1E00",tags = "delete")
        canvas.after(2000,lambda:canvas.delete("delete"))
    
    elif gross_income is False:
        canvas.delete("delete")
        canvas.create_text(354,140,text = "Invalid Data Input",font = ("Comic Sans MS",12,"bold"),fill = "#FF1E00",tags = "delete")
        canvas.after(2000,lambda:canvas.delete("delete"))
    
    elif pension_contribution is False:
        canvas.delete("delete")
        canvas.create_text(354,140,text = "Invalid Data Input",font = ("Comic Sans MS",12,"bold"),fill = "#FF1E00",tags = "delete")
        canvas.after(2000,lambda:canvas.delete("delete"))
    
    elif other_deductions is False:
        canvas.delete("delete")
        canvas.create_text(354,140,text = "Invalid Data Input",font = ("Comic Sans MS",12,"bold"),fill = "#FF1E00",tags = "delete")
        canvas.after(2000,lambda:canvas.delete("delete"))
    
    elif national_insurance is False:
        canvas.delete("delete")
        canvas.create_text(354,140,text = "Invalid Data Input",font = ("Comic Sans MS",12,"bold"),fill = "#FF1E00",tags = "delete")
        canvas.after(2000,lambda:canvas.delete("delete"))



    else:
        #---window config---
        window = Toplevel()
        window.geometry("750x600")
        window.title("Calculation Breakdown")

        #---canvas for flexible widget placement---
        canva = Canvas(
            window,
            width = 750,
            height = 600,
            bg = "#f8fafc",
        )
        canva.place(
            x = 0,
            y = 0,
            relheight = 1,
            relwidth = 1,
        )
        #---frame container for widget placment---
        calc_breakdownFrame = CTkFrame(
            window,
            width = 730,
            height = 580,
            bg_color = "#f8fafc",
            fg_color = "#D2DCE6",
            corner_radius = 15,
        )
        canva.create_window(375,300,window = calc_breakdownFrame)
    
        #---title widget with icon---
        calc_breakdownimg = Image.open("calc_breakdown.png").convert("RGBA")
        calc_img = ImageTk.PhotoImage(calc_breakdownimg)
        calc_breakdownlabel = CTkLabel(
            window,
            image = calc_img,
            text = " Calculation Breakdown",
            text_color = "black",
            font = ("Arial",18,"bold"),
            compound = "left",
            fg_color = "#D2DCE6",
            bg_color = "#D2DCE6"
        )
        canva.create_window(375,50,window = calc_breakdownlabel)

#--------------------------------------------------------------------------------

        #---Gross Monthly Salary Frame---
        gross_monthly_frame = CTkFrame(
            window,
            width = 300,
            height = 100,
            fg_color = "#f8fafc",
            bg_color = "#D2DCE6",
            corner_radius = 10,
        )
        canva.create_window(210,140,window = gross_monthly_frame)

        #---Gross Monthly Salary label---
        gross_monthly_label = CTkLabel(
            window,
            text = "Gross Monthly Salary",
            text_color = "#5A5A5A",
            font = ("Segui UI",15,"bold"),
            bg_color = "#f8fafc",
            fg_color = "#f8fafc"
        )
        canva.create_window(210,120,window = gross_monthly_label)
        #---Display gross monthly income value label---
        gross_monthly_value = CTkLabel(
            window,
            text = f"£ {monthly_income}",
            text_color = "#000000",
            font = ("Segui UI",30,"bold"),
            bg_color = "#f8fafc",
            fg_color = "#f8fafc"
        )
        canva.create_window(210,155,window = gross_monthly_value)

#--------------------------------------------------------------------------------

    #---National Insurance frame---
        national_insurance_frame = CTkFrame(
            window,
            width = 300,
            height = 100,
            fg_color = "#f8fafc",
            bg_color = "#D2DCE6",
            corner_radius = 10,
        )
        canva.create_window(210,260,window = national_insurance_frame)

        #---National Insurance Label---
        national_insurance_label = CTkLabel(
            window,
            text = "National Insurance",
            text_color = "#5A5A5A",
            font = ("Segui UI",15,"bold"),
            bg_color = "#f8fafc",
            fg_color = "#f8fafc"
        )
        canva.create_window(210,240,window = national_insurance_label)

        #---National Insurance value label---
        national_insurance_value = CTkLabel(
            window,
            text = f"£{national_insurance}",
            text_color = "#000000",
            font = ("Segui UI",30,"bold"),
            bg_color = "#f8fafc",
            fg_color = "#f8fafc"
        )
        canva.create_window(210,275,window = national_insurance_value)

#---------------------------------------------------------------------------------

        #---Other deductions frame---
        other_deductions_frame = CTkFrame(
            window,
            width = 300,
            height = 100,
            fg_color = "#f8fafc",
            bg_color = "#D2DCE6",
            corner_radius = 10,
        )
        canva.create_window(210,380,window = other_deductions_frame)

        #---Other Deductions Label---
        other_deductions_label = CTkLabel(
            window,
            text = "Other Deductions",
            text_color = "#5A5A5A",
            font = ("Segui UI",15,"bold"),
            bg_color = "#f8fafc",
            fg_color = "#f8fafc"
        )
        canva.create_window(210,360,window = other_deductions_label)

        #---Other Deductions value label---
        other_deductions_value = CTkLabel(
            window,
            text = f"£{other_deductions}",
            text_color = "#000000",
            font = ("Segui UI",30,"bold"),
            bg_color = "#f8fafc",
            fg_color = "#f8fafc"
        )
        canva.create_window(205,395,window = other_deductions_value)

#---------------------------------------------------------------------------------------

        #---Paye Tax frame---
        paye_tax_frame = CTkFrame(
            window,
            width = 300,
            height = 100,
            fg_color = "#f8fafc",
            bg_color = "#D2DCE6",
            corner_radius = 10,
        )
        canva.create_window(540,140,window = paye_tax_frame)

        #---Paye tax Label---
        paye_tax_label = CTkLabel(
            window,
            text = "PAYE Tax",
            text_color = "#5A5A5A",
            font = ("Segui UI",15,"bold"),
            bg_color = "#f8fafc",
            fg_color = "#f8fafc"
        )
        canva.create_window(540,120,window = paye_tax_label)

        #---Paye tax value label---
        paye_tax_value = CTkLabel(
            window,
            text = f"£{paye_tax}",
            text_color = "#000000",
            font = ("Segui UI",30,"bold"),
            bg_color = "#f8fafc",
            fg_color = "#f8fafc"
        )
        canva.create_window(540,155,window = paye_tax_value)

#-------------------------------------------------------------------------------

        #---Pension Contribution frame---
        pension_contribution_frame = CTkFrame(
            window,
            width = 300,
            height = 100,
            fg_color = "#f8fafc",
            bg_color = "#D2DCE6",
            corner_radius = 10,
        )
        canva.create_window(540,260,window = pension_contribution_frame)

        #---Pension Contribution Label---
        pension_contribution_label = CTkLabel(
            window,
            text = "Pension Contribution",
            text_color = "#5A5A5A",
            font = ("Segui UI",15,"bold"),
            bg_color = "#f8fafc",
            fg_color = "#f8fafc"
        )
        canva.create_window(540,240,window = pension_contribution_label)

        #---Pension Contribution value label---
        pension_contribution_value = CTkLabel(
            window,
            text = f"£{pension_contribution}",
            text_color = "#000000",
            font = ("Segui UI",30,"bold"),
            bg_color = "#f8fafc",
            fg_color = "#f8fafc"
        )
        canva.create_window(540,275,window = pension_contribution_value)

#-----------------------------------------------------------------------------

        #---Total Deductions frame---
        total_deductions_frame = CTkFrame(
            window,
            width = 300,
            height = 100,
            fg_color = "#f8fafc",
            bg_color = "#D2DCE6",
            corner_radius = 10,
        )
        canva.create_window(540,380,window = total_deductions_frame)

        #---Total Deductions Label---
        total_deductions_label = CTkLabel(
            window,
            text = "Total Deductions",
            text_color = "#5A5A5A",
            font = ("Segui UI",15,"bold"),
            bg_color = "#f8fafc",
            fg_color = "#f8fafc"
        )
        canva.create_window(540,360,window = total_deductions_label)

        #---Totaldeductions value label---
        total_deductions_value = CTkLabel(
            window,
            text = f"£{total_deductions}",
            text_color = "#000000",
            font = ("Segui UI",30,"bold"),
            bg_color = "#f8fafc",
            fg_color = "#f8fafc"
        )
        canva.create_window(540,395,window = total_deductions_value)

#-----------------------------------------------------------------------------------

        #---Net take-homepay frame---
        net_takehomepay_frame = CTkFrame(
            window,
            width = 630,
            height = 120,
            fg_color = "#0cac78",
            bg_color = "#D2DCE6",
            corner_radius = 10,
        )
        canva.create_window(378,510,window = net_takehomepay_frame)

        #---Net take-homepay pay label with icon---
        moneybag_img2 = Image.open("mgreen.png").convert("RGBA")
        moneybag_icon = ImageTk.PhotoImage(moneybag_img2)
        net_takehomepay_label = CTkLabel(
            window,
            image = moneybag_icon,
            text = "NET TAKE-HOME PAY",
            text_color = "#f8fafc",
            compound = "left",
            font = ("Segui UI",16,"bold"),
            fg_color = "#0cac78",
            bg_color = "#0cac78"
        )
        canva.create_window(378,485,window = net_takehomepay_label)

        #---Take home pay value---

        net_takehomepay_value = CTkLabel(
            window,
            text = f"£{take_homepay}",
            text_color = "#f8fafc",
            font = ("Segui UI",40,"bold"),
            fg_color = "#0cac78",
            bg_color = "#0cac78"
        )
        canva.create_window(378,525,window = net_takehomepay_value)

#---Button for calculating the take-home Pay---
calc_img = Image.open("calculator.png").convert("RGBA")
calculator_img = ImageTk.PhotoImage(calc_img)
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
    command = lambda:summary_page(rate,hours,pension,other,ni,root,canvas) 
)
canvas.create_window(355,700, window = Calc_TakehomePayButton)










root.mainloop()