import pandas as pd
import matplotlib.pyplot as plt

file_path = "assignment_3/data/1985-2019 Analysis of ridership.xlsx"
# LINK to the dataset: https://open.toronto.ca/dataset/ttc-ridership-analysis/

YEAR_ROW_EXCEL = 6          # year
SYSTEM_TOTAL_ROW_EXCEL = 54 # ridership
year_row_i = YEAR_ROW_EXCEL - 1
system_row_i = SYSTEM_TOTAL_ROW_EXCEL - 1

# import
df = pd.read_excel(file_path, header=None)

year_row = df.iloc[year_row_i]
system_row = df.iloc[system_row_i]

# clean year
years = pd.to_numeric(year_row, errors="coerce")
year_cols = years.dropna().index

# ridership
ridership = pd.to_numeric(system_row[year_cols].astype(str).str.replace(",", ""), errors="coerce")

plot_df = pd.DataFrame({
    "Year": years[year_cols].astype(int),
    "Ridership": ridership
}).dropna().sort_values("Year")

# Plot
plt.figure(figsize=(10, 5))

plt.plot(
    plot_df["Year"],
    plot_df["Ridership"],
    marker = "o",
    markersize = 10,         
    markerfacecolor = "white",
    markeredgewidth = 1,
    linewidth = 2
)                       

plt.yscale("log")   
plt.title("TTC Annual Ridership")
plt.xlabel("Year")
plt.ylabel("Ridership (k, log)")
plt.tight_layout()

# Save figure
plt.savefig("assignment_3/viz_1/viz_1_ridership_trend.png", dpi=300)
plt.show()

# end of script