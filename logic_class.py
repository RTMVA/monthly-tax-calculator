import math

class Employee:
    def __init__(self,rate,hours,pension_contribution = "",other_deductions = "",national_insurance = "Auto-calculated"):
        """
        Initialize an Employe instance.
        Args: rate(string),
              hours(string),
              pension contribution(string),
              other deductions(string)
        """

        self.rate = rate
        self.hours = hours
        self.pension_contribution = pension_contribution
        self.other_deductions = other_deductions
        self.national_insurance = national_insurance

#--------Method: calculate monthly income-----------------------------------------
    def calc_monthlyIncome(self):
        """
        Calculates the monthly income prior to deductions.
        Args(uses instance attributes):
            self.rate(string),
            self.hours(string)
        
        returns:monthly_income(int)
        """
        if type(self.rate) == bool or type(self.hours) == bool:
            return False

        monthly_pay = 0
        try:
            hours = float(self.hours)
            rate = float(self.rate)

            if hours < 0 or rate < 0:
                return False

            if math.isinf(hours) or math.isnan(hours):
                return False
        
            if math.isinf(rate) or math.isnan(rate):
                return False
            
            monthly_pay = hours * rate
        except ValueError:
            return False
        
        return monthly_pay

#--------Method: get pension contributions-------------------------------------    
    def get_pension_contribution(self):
        """
        returns the pension contribution.
        Args:(uses instance attributes)
              self.pension_contribution(string)

        returns:pension contributions
        """
        try:
            if not self.pension_contribution:
                self.pension_contribution = "0"

            pension_contrib = float(self.pension_contribution)

            if math.isinf(pension_contrib) or math.isnan(pension_contrib):
                return False
        
            if pension_contrib >= 0:
                return round(pension_contrib,2)
            else:
                return False

        except ValueError:
            return False
        
#-------Method: get other deductions----------------------------------------------
    def getOther_deductions(self):
        """
        returns the other deductions.
        Args:(uses instance attributes)
              self.other_deductions(string)

        returns:other deductions 
        """
        try:
            if not self.other_deductions:
                self.other_deductions = "0"
        
            other_deduct = float(self.other_deductions)

            if math.isinf(other_deduct) or math.isnan(other_deduct):
                return False

            if other_deduct >= 0:
                return round(other_deduct,2)
            else:
                return False

        except ValueError:
            return False

#--------Method: calculate gross income---------------------------------------
    def calc_grossIncome(self):
        """
        calculates the gross income.
        args(uses class ):
            self.monthly_income(int)

        returns:gross income
        """
        monthly_income = self.calc_monthlyIncome()
        if monthly_income is False:
            return False
        else:
            monthly_income = self.calc_monthlyIncome()
            return monthly_income * 12

#--------Method: calculate paye tax---------------------------------------------
    def calc_payeTax(self):
        """
        Calculates the paye tax of the Employee based on annual salary.
        Args(uses class method):
             self.calc_grossIncome(int)

        returns: paye tax     
        """
        taxable_amount = 0
        monthly_tax = 0
        annual_tax = 0
        taxfree_allowance = 12570
        max_basic_taxable = 37700
        max_upper_taxable = 74870
        gross_income = self.calc_grossIncome()
        if gross_income is False:
            return False

        if gross_income <= 12570:
            monthly_tax = 0.00

        elif gross_income > 12570 and gross_income <= 50270:
            taxable_amount = gross_income - taxfree_allowance
            annual_tax = taxable_amount * 0.2 
            monthly_tax = annual_tax / 12

        elif gross_income > 50270 and gross_income <= 100000:
            taxable_amount = gross_income - taxfree_allowance
            basic_band = max_basic_taxable * 0.2
            taxable_amountH = taxable_amount - max_basic_taxable
            upper_band = taxable_amountH * 0.4
            annual_tax = basic_band + upper_band
            monthly_tax = annual_tax / 12

        elif gross_income > 100000 and gross_income <= 125140:
            taxfree_amount_reduction = (gross_income - 100000) / 2
            taxfree_allowance = taxfree_allowance - taxfree_amount_reduction
            taxfree_allowance = max(0, taxfree_allowance)
            taxable_amount = gross_income - taxfree_allowance
            basic_band = max_basic_taxable * 0.2
            taxable_amountH = taxable_amount - max_basic_taxable
            upper_band = taxable_amountH * 0.4
            annual_tax = basic_band + upper_band
            monthly_tax = annual_tax / 12

        elif gross_income > 125140:
            taxable_amount = gross_income
            basic_band = max_basic_taxable * 0.2
            taxable_amount = gross_income - max_basic_taxable
            taxable_amountH = taxable_amount - (max_upper_taxable + taxfree_allowance)
            upper_band = (max_upper_taxable + taxfree_allowance) * 0.4
            highest_band = taxable_amountH * 0.45
            annual_tax = basic_band + upper_band + highest_band
            monthly_tax = annual_tax / 12
    

        return round(monthly_tax,2)


#--------Method: calculate National insurance---------------------------------------------
    def calc_national_insurance(self):
        """
        Calculates the National Insurance based on the monthly income.
        Args(uses instance attributes):
            self.national_insurance(int)
            self.monthly_income(int)
    
        returns: national insurance
        """
        def auto_calc(monthly_income):
            taxable = 0
            ptm = 1048
            utm = 4189
            if monthly_income <= ptm:
                national_insurance = 0

            elif monthly_income <= utm:
                taxable = monthly_income - ptm
                national_insurance = taxable * 0.08

            else:
                taxable = monthly_income - ptm  
                basic_taxable = utm - ptm
                basic_rate = basic_taxable * 0.08
                taxable = taxable - basic_taxable
                national_insurance = taxable * 0.02
                national_insurance += basic_rate

            return round(national_insurance,2)
        
        monthly_income = self.calc_monthlyIncome()
        if monthly_income is False:
            return False
        
        if self.national_insurance and self.national_insurance != "Auto-calculated":
            try:
                insurance = float(self.national_insurance)

            except (ValueError,TypeError):
                    return False
            
            if math.isinf(insurance) or math.isnan(insurance):
                    return False
                
            if insurance <= 0:
                    return auto_calc(monthly_income)
            
            else:
                return round(insurance,2)
        
            
        else:
            return auto_calc(monthly_income)
        

#--------Method:calculate total deduction-------------------------------------------------------------
    def calc_total_deductions(self):
        pension = self.get_pension_contribution()
        paye_tax = self.calc_payeTax()
        other = self.getOther_deductions()
        ni = self.calc_national_insurance()

        if any(val is False for val in(pension,paye_tax,other,ni)):
            return False
        
        return round(pension + paye_tax + other + ni,2)

#--------method:calculate take home pay--------------------------------------------------------------
    def calc_take_homepay(self):
        monthly_income = self.calc_monthlyIncome()
        total_deductions = self.calc_total_deductions()

        if any(val is False for val in (monthly_income,total_deductions)):
            return False

        monthly_income = monthly_income - total_deductions
        return round(monthly_income,2)



Clinton = Employee("60","150")


print(Clinton.calc_payeTax())