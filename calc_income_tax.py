import sys

def calc_income_tax(income: float) -> float:
    # use list to hold tax bracket thresholds and rates
    tax_brackets = [10275, 41775, 89075, 170050, 215950, 539900]
    tax_rates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37]
    tax_amount = 0
    income_remaining = 0
    # calculate tax
    if income <= tax_brackets[0]:
        return income * tax_rates[0]
    elif income <= tax_brackets[1]:
        tax_amount = tax_brackets[0] * tax_rates[0]
        tax_amount += (income - tax_brackets[0]) * tax_rates[1]
        return tax_amount
    elif income <= tax_brackets[2]:
        tax_amount = tax_brackets[0] * tax_rates[0]
        tax_amount += (tax_brackets[1] - tax_brackets[0]) * tax_rates[1]
        tax_amount += (income - tax_brackets[1]) * tax_rates[2]
        return tax_amount
    elif income <= tax_brackets[3]:
        tax_amount = tax_brackets[0] * tax_rates[0]
        tax_amount += (tax_brackets[1] - tax_brackets[0]) * tax_rates[1]
        tax_amount += (tax_brackets[2] - tax_brackets[1]) * tax_rates[2]
        tax_amount += (income - tax_brackets[2]) * tax_rates[3]
        return tax_amount
    elif income <= tax_brackets[4]:
        tax_amount = tax_brackets[0] * tax_rates[0]
        tax_amount += (tax_brackets[1] - tax_brackets[0]) * tax_rates[1]
        tax_amount += (tax_brackets[2] - tax_brackets[1]) * tax_rates[2]
        tax_amount += (tax_brackets[3] - tax_brackets[2]) * tax_rates[3]
        tax_amount += (income - tax_brackets[3]) * tax_rates[4]
        return tax_amount
    elif income <= tax_brackets[5]:
        tax_amount = tax_brackets[0] * tax_rates[0]
        tax_amount += (tax_brackets[1] - tax_brackets[0]) * tax_rates[1]
        tax_amount += (tax_brackets[2] - tax_brackets[1]) * tax_rates[2]
        tax_amount += (tax_brackets[3] - tax_brackets[2]) * tax_rates[3]
        tax_amount += (tax_brackets[4] - tax_brackets[3]) * tax_rates[4]
        tax_amount += (income - tax_brackets[4]) * tax_rates[5]
        return tax_amount
    else:
        tax_amount = tax_brackets[0] * tax_rates[0]
        tax_amount += (tax_brackets[1] - tax_brackets[0]) * tax_rates[1]
        tax_amount += (tax_brackets[2] - tax_brackets[1]) * tax_rates[2]
        tax_amount += (tax_brackets[3] - tax_brackets[2]) * tax_rates[3]
        tax_amount += (tax_brackets[4] - tax_brackets[3]) * tax_rates[4]
        tax_amount += (tax_brackets[5] - tax_brackets[4]) * tax_rates[5]
        tax_amount += (income - tax_brackets[5]) * tax_rates[6]
        return tax_amount

if __name__ == "__main__":
    if len(sys.argv) == 1:
        annual_income = input("Enter in annual income: ")
        tax = calc_income_tax(float(annual_income))
        print(f"Annual taxes on ${annual_income} will be ${tax}")
        print(f"You will be left with ${float(annual_income) - tax}")
    elif len(sys.argv) == 2:
        tax = calc_income_tax(float(sys.argv[1]))
        print(f"Annual tax on ${float(sys.argv[1])} will be ${tax}")
        print(f"You will be left with ${float(sys.argv[1]) - tax}")
    else:
        print("ERROR OCCURRED")