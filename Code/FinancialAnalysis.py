import numpy as np
import numpy_financial as npf  # Import numpy_financial for IRR

# Function to calculate Present Worth (PW)
def calculate_present_worth(future_value, interest_rate, years):
    PW = future_value / (1 + interest_rate)**years
    return PW

# Function to calculate Future Worth (FW)
def calculate_future_worth(present_value, interest_rate, years):
    FW = present_value * (1 + interest_rate)**years
    return FW

# Function to calculate Annual Worth (AW) with annuity (annual operating costs)
def calculate_annual_worth(present_value, interest_rate, years, annuity=0):
    AW = present_value * (interest_rate * (1 + interest_rate)**years) / ((1 + interest_rate)**years - 1)
    AW_total = AW - annuity  # Subtract the annual operating costs
    return AW_total

# Function to calculate Capital Recovery Factor (CRF)
def calculate_crf(interest_rate, years):
    CRF = (interest_rate * (1 + interest_rate)**years) / ((1 + interest_rate)**years - 1)
    return CRF

# Function to calculate Time Value of Money (TVM)
def time_value_of_money(amount, interest_rate, years, option='future'):
    if option == 'future':
        return calculate_future_worth(amount, interest_rate, years)
    elif option == 'present':
        return calculate_present_worth(amount, interest_rate, years)

# Function to calculate Internal Rate of Return (IRR)
def calculate_irr(cash_flows):
    irr = npf.irr(cash_flows)  # Use npf.irr instead of np.irr
    return irr

# Function to calculate Net Present Value (NPV)
def calculate_npv(cash_flows, interest_rate):
    npv = npf.npv(interest_rate, cash_flows)  # Use numpy_financial's NPV function
    return npv

# Function to calculate Benefit-Cost Ratio (BCR)
def calculate_bcr(npv, initial_cost):
    total_benefits = npv + initial_cost  # Total benefits is NPV + Initial investment
    bcr = total_benefits / initial_cost
    return bcr

# Function to calculate Profitability Index (PI)
def calculate_profitability_index(npv, initial_cost):
    pi = (npv + initial_cost) / initial_cost
    return pi

# Example Usage:
if __name__ == "__main__":
    # Parameters
    interest_rate = 0.12  # 12% interest rate
    years = 10
    initial_cost = 525000000
    salvage_value = 145950000
    annuity = 77750000  # Annual operating costs (annuity)
    revenue_per_year = 125000000  # Corrected revenue per year (1,750,000,000)

    # Calculating Present Worth (PW)
    pw = calculate_present_worth(salvage_value, interest_rate, years)
    print(f"Present Worth (PW) of Salvage Value: {pw:.2f}")

    # Calculating Future Worth (FW)
    fw = calculate_future_worth(initial_cost, interest_rate, years)
    print(f"Future Worth (FW) of Initial Investment: {fw:.2f}")

    # Calculating Annual Worth (AW) with annuity
    aw = calculate_annual_worth(initial_cost, interest_rate, years, annuity)
    print(f"Annual Worth (AW) after accounting for annuity: {aw:.2f}")

    # Calculating Capital Recovery Factor (CRF)
    crf = calculate_crf(interest_rate, years)
    print(f"Capital Recovery Factor (CRF): {crf:.4f}")

    # Calculating Time Value of Money (TVM) for future
    tvm_future = time_value_of_money(initial_cost, interest_rate, years, option='future')
    print(f"Time Value of Money (Future): {tvm_future:.2f}")

    # Calculating Internal Rate of Return (IRR)
    # Cash flows: Initial cost (-5,250,000,000), operational costs for years 1-10 (-787,500,000/year),
    # revenue for years 1-10 (+1,750,000,000/year), and salvage value (+1,459,500,000) in year 10
    cash_flows = [-initial_cost] + [revenue_per_year - annuity] * (years - 1) + [revenue_per_year - annuity + salvage_value]
    irr = calculate_irr(cash_flows)
    print(f"Internal Rate of Return (IRR): {irr*100:.2f}%")

