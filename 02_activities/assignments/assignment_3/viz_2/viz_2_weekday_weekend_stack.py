import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

file_path = "assignment_3/data/1985-2019 Analysis of ridership.xlsx"
# LINK to the dataset: https://open.toronto.ca/dataset/ttc-ridership-analysis/

YEAR_ROW_EXCEL = 6
WEEKDAY_ROW_EXCEL = 66
WEEKEND_ROW_EXCEL = 67

year_row_i = YEAR_ROW_EXCEL - 1
weekday_row_i = WEEKDAY_ROW_EXCEL - 1
weekend_row_i = WEEKEND_ROW_EXCEL - 1

# import
df = pd.read_excel(file_path, header=None)

year_row = df.iloc[year_row_i]
weekday_row = df.iloc[weekday_row_i]
weekend_row = df.iloc[weekend_row_i]

# clean years: e.g., 2015* is weird
year_str = year_row.astype(str)
years = pd.to_numeric(year_str.str.extract(r"(\d{4})", expand=False), errors="coerce")
year_cols = years.dropna().index

# clean data/numbers
def to_num(series):
    return pd.to_numeric(
        series.astype(str).str.replace(",", "", regex=False),
        errors="coerce"
    )

weekday = to_num(weekday_row[year_cols])
weekend = to_num(weekend_row[year_cols])

plot_df = pd.DataFrame({
    "Year": years[year_cols].astype(int),
    "Weekday": weekday,
    "Weekend/Holiday": weekend
}).dropna().sort_values("Year")

# convert to percentages
plot_df["Total"] = plot_df["Weekday"] + plot_df["Weekend/Holiday"]
plot_df["Weekday_pct"] = plot_df["Weekday"] / plot_df["Total"]
plot_df["Weekend_pct"] = plot_df["Weekend/Holiday"] / plot_df["Total"]

# plot (stacked bar plot)
plt.figure(figsize=(12, 6))

plt.bar(
    plot_df["Year"],
    plot_df["Weekday_pct"],
    label="Weekday",
    color="lightcoral"  
)

plt.bar(
    plot_df["Year"],
    plot_df["Weekend_pct"],
    bottom=plot_df["Weekday_pct"],
    label="Weekend/Holiday",
    color="seagreen"     
)

plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
plt.ylim(0, 1)

plt.title("TTC Ridership Composition: Weekday vs Weekend/Holiday")
plt.xlabel("Year")
plt.ylabel("Annual Ridership")
plt.legend()
plt.tight_layout()

plt.savefig("assignment_3/viz_2/viz_2_weekday_weekend.png", dpi=300)
plt.show()

# end of script