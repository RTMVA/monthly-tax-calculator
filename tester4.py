invalid_cases = {
    "paye-tax":("a","12","34","34","40",False),#invalid paye tax
    "pension":("12","12","a","34","40",False),#invalid pension contribution
    "other":("a","12","34","a","40",False),#invalid other deductions
    "ni":("a","12","34","34","a",False),#invalid national insurance
}

for case,values in invalid_cases.items():
    if values[0] == "a":
        print(values[0])
    