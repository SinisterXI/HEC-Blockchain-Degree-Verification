import matplotlib.pyplot as plt
import numpy as np

# Function to format numbers into readable abbreviations (k, M, Cr)
def format_cash_flow(value):
    if value >= 1e8:  # For crore (10 million)
        return f"{value / 1e7:.2f} Cr"
    elif value >= 1e6:  # For million (10^6)
        return f"{value / 1e6:.2f} M"
    elif value >= 1e3:  # For thousand (10^3)
        return f"{value / 1e3:.2f} k"
    else:
        return f"{value:.0f}"

# Cash Flow Data
years = np.arange(0, 11)  # 0 to 10 years
cash_flows = [-525000000] + [47250000] * 9 + [193200000]  # Cash flow values

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting the cash flows as bars
bars = ax.bar(years, cash_flows, color=['red' if x < 0 else 'green' for x in cash_flows])

# Adding labels and title
ax.set_xlabel("Years")
ax.set_ylabel("Cash Flow ($)")
ax.set_title("Cash Flow Diagram")

# Add annotations for each bar with proper positioning to avoid overlap
for i, value in enumerate(cash_flows):
    formatted_value = format_cash_flow(value)  # Format the value with abbreviation
    if value >= 0:
        # For positive values, place the text above the bar
        ax.text(years[i], value + 0.05 * max(cash_flows), formatted_value, ha='center', va='bottom')
    else:
        # For negative values, place the text below the bar
        ax.text(years[i], value - 0.05 * max(cash_flows), formatted_value, ha='center', va='top')

# Highlight the middle y-axis (0) in bold
ax.axhline(0, color='black', linewidth=2)  # Bold line at y=0

# Show gridlines for better readability
ax.grid(True, which='both', axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.show()
