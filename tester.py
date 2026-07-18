from logic_class import Employee

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
    print(bad_value)
    userx = Employee(inputs[0],inputs[1])
    print(userx.calc_total_deductions())



