class holiday:
    def __init__(self,monthly_income,hours):
        self.monthly_income = monthly_income
        self.hours = hours

    def calc_holiday_pay(self):
        holiday_pay = self.monthly_income * 0.1207
        return holiday_pay
    
    def calc_rate(self):
        holiday_pay = self.calc_holiday_pay()
        total = self.monthly_income + holiday_pay
        rate = total / self.hours
        return round(rate,2)
    


clintons_pay = holiday(1124.8,80)
print(clintons_pay.calc_rate())
