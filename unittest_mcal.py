import unittest

from logic_class import Employee

class Logic_test(unittest.TestCase):
    
    def test_monthlyIncome_val(self):
        """
         This test is to ensure data validation of the inputs hours and rate.
        -Input: string hours,string rate
        -Validation: If either input is non numeric,boolean, empty string return false:
        -process: Both inputs are converted to floats and then multiplied the answer returns the monthly income
        -expected output: float Monthly income round 2 decimal places, else false
        """

        inv_cases = [
            ("a","12",False),#check if the rate input is a non numeric string return False
            ("12","a",False),#check if the hours input is a non numeric string return False
            ("","",False),#if both inputs are empty strings return False
            ("False","23",False),#if just rate input is an boolean as string return False
            (False,False,False),#if rate and hours input are boolean values return False
            ("-34","55",False),#negative numbers -> return false
            ("inf","34",False),#special string val -> return False
            ("12","NaN",False)#special string val -> return False
        ]

        for rate,hours,expected in inv_cases:
            with self.subTest(f"rate:{rate},hours:{hours}->expected{expected}"):
                userx = Employee(rate,hours)
                self.assertFalse(userx.calc_monthlyIncome())
       

        valid_cases = [
           ("14.75","143",2109.25),#validation: string float rate * string int hours = float monthly income 2dp
           ("40","40",1600.00), #validation: string integers converted to floats and calculates monthly income properly
           ("14.75","120.5",1777.375)#validation: takes string floats and converts into float -> return float monthly income
       ]
        
        for rate,hours,expected in valid_cases:
            with self.subTest(f"rate:{rate},hours:{hours}->expected{expected}"):
                userx1 = Employee(rate,hours)
                self.assertAlmostEqual(userx1.calc_monthlyIncome(),expected)



    def test_pension_contriVal(self):
        """
        Purpose: this test is to ensure that the user has entered the valid data for the program to continue
        it should display an appropriate message if the has not.
        -Input : String pension_contribution
        -Validation: Return False if input is non numeric, special strings values, boolean strings, negative string numbers values.
        -Process: Pension contribution input is converted to a float with 2dp if the conversion 
                  fails it means the user has entered an invalid input.
        -Expected Output: float pension contribution rounded to 2dp or False.

        """
        inv_cases = [
            ("14","120","a",False), #test for non-numeric values -> return False
            ("14","120","inf",False), #test for special string values(inf,NaN) -> return False
            ("14","120","NaN",False),#test for special string value NaN should return false
            ("14","120","False",False),#test for boolean strings values return false as its treated as normal strings
            ("14","120","-4",False)#tests for negative values return false if number is less than 0
        ]

        for rate,hours,pension,expected in inv_cases:
            with self.subTest(f"pension:{pension} -> expected{expected}"):
                userx = Employee(rate,hours,pension)
                self.assertFalse(userx.get_pension_contribution())


        valid_cases = [
            ("14","120","90.45",90.45),#float string vonversion check
            ("14","120","91",91.00), #integer to float conversion check
            ("14","120","90.45345435",90.45)#rounding check to 2dp
        ]
        
        for rate,hours,pension,expected in valid_cases:
            with self.subTest(f"pension:{pension} -> expected{expected}"):
                userx1 = Employee(rate,hours,pension)
                self.assertAlmostEqual(userx1.get_pension_contribution(),expected)
    
    
    def test_otherDeductionsval(self):
        """
        Purpose: The purpose of this test is to check whether the other deductions functions actually return the user input value(2dp) 
        and how it handles invalid input.
        -Input: String other_deductions
        -Validation: This method should return False if the user enters a non-numeric string value, boolean string values, 
        special string values, negative string numbers values and it should return the output accordingly
        -Process:pension contribution input is converted into a float with 2 decimal places if it fails to convert that means the user has entered an invalid input and it should return false
        -Expected Output: The output should be the other deductions value in 2dp or False.

        """

        cases = [
            ("a",False),#non-numeric
            ("inf",False),#special-string
            ("NaN",False),#special-string
            ("-4",False),#negative number
            ("90.67",90.67),#valid float
            ("100",100.00),#integer string -> float 
            ("134.66785",134.67),#rounding check
            ("0",0.00),#zero is valid
        ]

        for input_val,expected in cases:
            with self.subTest(input = input_val,expected = expected):
                other_duct = Employee("14.56","120","0",input_val)
                self.assertEqual(other_duct.getOther_deductions(),expected)


    def test_gross_inncome_val(self):
        """
        -Purpose: Test if grossIncome method returns either False or float annual gross income 2dp
        -Validation: return false if monthly income is false, calculate annual gross income correctly.
        -Cases:
            1) Invalid monthly income -> False
            2) Valid monthly Income -> return annual gross income rounded to 2dp
        -Expected output:  False or 2dp float representing annual gross income.
        """
        
       #case 1 valid
        with self.subTest("valid monthly income"):
            rate,hours = 14.75,120
            user = Employee(rate,hours)

            monthly_income = round(rate * hours,2)
            self.assertEqual(user.calc_grossIncome(),round(monthly_income * 12,2))

       #case 2 invalid
        with self.subTest("invalid monthly income"):
            userx = Employee("a",120)#trigger monthly income to return false
            self.assertFalse(userx.calc_grossIncome())

    def test_paye_TaxVal(self):
       """
       -Purpose: Test if paye tax returns false or returns float paye tax(2dp)
       -Validation: This unit test should ensure that paye tax returns False if gross income is false.
        It should calculate the paye tax according to users wage which is determined by the grossincome(monthly income x 12).
       -Cases:
               1)Invalid gross income -> False
               2)Valid gross income <= 12570 return float paye tax
               3)Valid gross income > 12570 and gross income <= 50270 return float paye tax
               4)Valid gross income > 50270 and gross income <= 100000 return float paye tax
               5)Valid gross income > 100000 and gross income <= 125140 return float paye tax
               6)Valid gross income > 125140 return float paye tax
       -Expected output: False or float  paye tax 2dp.     
       """
      
       #case 1 invalid
       with self.subTest("invalid gross income"):
           user1 = Employee("a","120")
           gross_income = user1.calc_grossIncome()
           self.assertFalse(gross_income)


       #case 2 - 6 valid
       cases = [
           (12,80,0.00),
           (15,140,210.50),
           (30,150,752.67),
           (60,150,2686.0),
           (80,150,4250.25),
       ]
      
       for rate,hour,tax in cases:
           with self.subTest(f"rate = {rate} , hours = {hour}: expected tax = {tax}"):
               userx = Employee(rate,hour)
               self.assertAlmostEqual(userx.calc_payeTax(),tax)
  
    def test_nationalInsuranceVal(self):
       """
       -Purpose: Tests if national insurance returns False if monthly income is false and returns the right national insurance otherwise.
       -Validation: This test is vital as it should ensure that national insurance is either false due to monthly income being invalid or 
        it returns the correct national insurance in float 2dp format. If user input it should return false if user enters non-numeric string , 
        special string values, negative string integers. If input is 0 override and return float national insurance 2dp. Rounding checks 2dp, 
        valid float return ni 2dp ,valid integer return ni 2dp.

       -Cases:
           1)Invalid monthly income -> False
           5)Non-numeric -> false
           2)Valid Monthly income <= 1048 = 0 national insurance
           3)Valid Monthly income > 1048 and monthly income < 4189 = float Ni 2dp
           4)Valid Monthly income > 4189
        -Overidden case:
           5)Non-numeric -> false
           6)Special string -> false
           7)Specialstring -> false
           8)Negative string integer -> 'override return float ni 2dp
           9)Valid float -> return float ni 2dp
           10)Integer string -> return float ni 2dp
           11)Rounding check -> return float 2dp
           12)String 0 -> @override return float ni 2dp 

       -Expected output: False or float national insurance 2dp.
       """
      
       #case 1 invalid
       with self.subTest("Invalid test case"):
           user1 = Employee("a",120)
           self.assertFalse(user1.calc_national_insurance())
      
       #valid test cases 2 - 4
       cases = [
           (12,60,0.00),
           (15,150,96.16),
           (30,150,257.50)
       ]
      
       for rate,hours,ni in cases:
           with self.subTest(f"rate = {rate} , hours = {hours}: expected ni = {ni}"):
               userx = Employee(rate,hours)
               self.assertAlmostEqual(userx.calc_national_insurance(),ni)

        #overidden invalid national insurance
        #cases 
       cases_ui = [
            ("12","120","4","4","a",False),#invalid data type
            ("12","120","4","4","inf",False),#special string
            ("12","120","4","4","NaN",False),#special string
        ]
       
       for rates,hour,other,pension,ni_t,expected in cases_ui:
           with self.subTest(value = ni_t,expected = expected):
               userxx = Employee(rates,hour,other,pension,ni_t)
               self.assertFalse(userxx.calc_national_insurance())
    
        #valid overriden cases
       cases_ui_valid = [
           ("12","120","4","4","13.34",13.34),#valid string float
           ("12","120","4","4","145",145.00),#valid string integer
           ("12","120","4","4","-1000",31.36),#negative numbers -> auto-calc
           ("12","120","4","4","256.986234",256.99),#rounding check
           ("12","120","4","4","0",31.36),#0 -> auto-calc
       ]

       for rate,hour,other,pension,ni,expected in cases_ui_valid:
           with self.subTest(argument = ni,expected = expected):
               user_val = Employee(rate,hour,other,pension,ni)
               self.assertAlmostEqual(user_val.calc_national_insurance(),expected)

    def test_total_deductions(self):
        """
        -Purpose: To test if total deductions returns false if any of the deductions are false.
         Tests if the calculation is correct and returns float 2dp.
        -validation: The validation concludes a test where it checks if paye tax , pension contribution , 
         other deductions and national insurance return false. If it does return False.
        -verification: The verification process checks whether total deductions 
         calculates pension contribution + paye tax + national insurance + other deductions correctly and returns the calculation in float 2dp.
        -Case:
         For invalid cases:
         1)pension contribution =  false , return false
         2)Paye tax = false, return false -> monthly income has to be false to be triggered 
         3)Get other deductions = false , return false
         4)national insurance = false , return false
         verifaction case:
         5)5)Correct calc -> pension contribution + paye tax + national insurance + other deductions return float 2dp

         Expected output:Return False or float total deductions 2dp
        """

        
        invalid_cases = [
            {"field":"m_income", "inputs":("a","12","34","34","40",False),"bad_index":0},#invalid paye tax
            {"field":"pension","inputs":("12","12","a","34","40",False),"bad_index":2},#invalid pension contribution
            {"field":"other","inputs":("12","12","34","a","40",False),"bad_index":3},#invalid other deductions
            {"field":"ni","inputs":("12","12","34","34","a",False),"bad_index":4}#invalid national insurance
        ]

        for case in invalid_cases:
            field = case["field"]
            inputs = case["inputs"]
            bad_index = case["bad_index"]
            bad_value = inputs[bad_index]

            with self.subTest(test = field,value = bad_value,expected = inputs[5]):
                userx = Employee(inputs[0],inputs[1],inputs[2],inputs[3],inputs[4])
                self.assertFalse(userx.calc_total_deductions())
        
        valid_case = [
            ("12","120","40","50","20",188.50)
        ]
        
    

        for rate,hours,pension,other,ni,expected in valid_case:
            with self.subTest(f"valid test, expected:{expected}"):
                userx1 = Employee(rate,hours,pension,other,ni)
                self.assertAlmostEqual(userx1.calc_total_deductions(),expected)

    def test_take_homepayCalc(self):
        """
        -Purpose: The purpose of this test is 
         to check whether the takehomepay method returns the total take-homepay in 2dp.
        -Validation: the validation test is to ensure that if monthly income = False and total_deductions = false it should return false. 
        -Verification: the test should ensure that if monthly income and total deductions are both valid it should return the total take-home pay. 
         Monthly income - total_deductions = float takehomepay 2dp.
        -Cases:
            Invalid values:
            1)Monthly income = false , return false 
            2)Total deductions = false , return false

            Valid values 
            3.Monthly income - total deductions = float takehome pay 2dp.
        -Expected output : false or float takehomepay 2dp.
        """

        inv_cases = [
            ("12","inf",False)#case mincome false and total deduct false    
        ]
        for rate,hours,expected in inv_cases:
            with self.subTest("invalid cases",expected = expected):
                userxx = Employee(rate,hours)
                self.assertFalse(userxx.calc_monthlyIncome())
                self.assertFalse(userxx.calc_total_deductions())
        
        valid_case = [
            ("17","140",2006.94)#calc takehomepay -> float takehomepay 2.dp
        ]
        for rate,hour,expected in valid_case:
            with self.subTest("valid case",expected = expected):
                userxx3 = Employee(rate,hour)
                self.assertAlmostEqual(userxx3.calc_take_homepay(),2006.94)




        
    


if __name__ =="__main__":
    unittest.main()