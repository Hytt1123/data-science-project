import matplotlib.pyplot as plt
import pandas as pd

# 1. Load the global energy and compliance panel dataset
df = pd.read_csv("global_energy_compliance_panel.csv")

# Set plotting style
plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")

# Filter cross-sectional data for the latest year (2023)
recent_df = df[df["Year"] == 2023]

# --- Visualization 1: Multivariate Bubble Chart ---
plt.figure(figsize=(10, 6))
scatter = plt.scatter(
    recent_df["Renewable_Energy_Share_%"],
    recent_df["Carbon_Emission_Mt"],
    s=recent_df["GDP_per_Capita"] / 400,
    c=recent_df["Data_Compliance_Index"],
    cmap="viridis",
    alpha=0.8,
    edgecolors="k"
)

cbar = plt.colorbar(scatter)
cbar.set_label("Data Compliance Index (0-100)")

for i, txt in enumerate(recent_df["Country"]):
    plt.annotate(txt, (recent_df["Renewable_Energy_Share_%"].iloc[i] + 0.8, recent_df["Carbon_Emission_Mt"].iloc[i]), fontsize=10)

plt.title("2023 Global Energy Transition: Renewables vs. Carbon Emissions", fontsize=13, fontweight="bold")
plt.xlabel("Renewable Energy Share (%)", fontsize=12)
plt.ylabel("Carbon Emissions (Mt)", fontsize=12)
plt.tight_layout()
plt.savefig("complex_energy_bubble_chart.png", dpi=300)
plt.close()

# --- Visualization 2: Multi-Year Trend Line Chart ---
plt.figure(figsize=(10, 6))
top_countries = ["Germany", "UK", "Sweden", "Switzerland", "France"]
for country in top_countries:
    subset = df[df["Country"] == country]
    plt.plot(subset["Year"], subset["Data_Compliance_Index"], marker='o', linewidth=2, label=country)

plt.title("2015-2023 Data Compliance Index Trend for Selected Nations", fontsize=13, fontweight="bold")
plt.xlabel("Year", fontsize=12)
plt.ylabel("Data Compliance Index (0-100)", fontsize=12)
plt.legend(title="Country")
plt.tight_layout()
plt.savefig("compliance_trend_line_chart.png", dpi=300)
plt.close()

print("Advanced analysis complete! Two complex visual charts generated successfully.")
