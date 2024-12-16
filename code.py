import pandas as pd
import plotly.express as px

# Load the dataset
file_path = "path_to_your_nasa_battery_dataset.csv"  # Replace with the correct file path
df = pd.read_csv(file_path)

# Display the first few rows of the dataset to understand its structure
df.head()

# Explore the columns and identify relevant ones
print(df.columns)

# Drop rows with missing values in the relevant columns: 'Cycle', 'Battery_impedance', 'Re', 'Rct'
df_cleaned = df[['Cycle', 'Battery_impedance', 'Re', 'Rct']].dropna()

# Verify the cleaned dataset
print(df_cleaned.head())

# --- Create Interactive Plots Using Plotly ---

# 1. Plot Battery Impedance vs Cycle Number
fig_impedance = px.line(df_cleaned, x='Cycle', y='Battery_impedance',
                        title='Battery Impedance vs Charge/Discharge Cycles',
                        labels={'Battery_impedance': 'Battery Impedance (Ohms)', 'Cycle': 'Cycle Number'})

# Show the plot
fig_impedance.show()

# 2. Plot Estimated Electrolyte Resistance (Re) vs Cycle Number
fig_Re = px.line(df_cleaned, x='Cycle', y='Re',
                 title='Electrolyte Resistance (Re) vs Charge/Discharge Cycles',
                 labels={'Re': 'Electrolyte Resistance (Ohms)', 'Cycle': 'Cycle Number'})

# Show the plot
fig_Re.show()

# 3. Plot Estimated Charge Transfer Resistance (Rct) vs Cycle Number
fig_Rct = px.line(df_cleaned, x='Cycle', y='Rct',
                  title='Charge Transfer Resistance (Rct) vs Charge/Discharge Cycles',
                  labels={'Rct': 'Charge Transfer Resistance (Ohms)', 'Cycle': 'Cycle Number'})

# Show the plot
fig_Rct.show()

# --- Optional: Add Trendlines to the Plots for Insight ---

# 4. Add a trendline to the Battery Impedance vs Cycle plot
fig_impedance_trendline = px.scatter(df_cleaned, x='Cycle', y='Battery_impedance',
                                     title='Battery Impedance vs Charge/Discharge Cycles with Trendline',
                                     labels={'Battery_impedance': 'Battery Impedance (Ohms)', 'Cycle': 'Cycle Number'},
                                     trendline="ols")

# Show the plot with trendline
fig_impedance_trendline.show()

# 5. Add a trendline to the Electrolyte Resistance (Re) vs Cycle plot
fig_Re_trendline = px.scatter(df_cleaned, x='Cycle', y='Re',
                              title='Electrolyte Resistance (Re) vs Charge/Discharge Cycles with Trendline',
                              labels={'Re': 'Electrolyte Resistance (Ohms)', 'Cycle': 'Cycle Number'},
                              trendline="ols")

# Show the plot with trendline
fig_Re_trendline.show()

# 6. Add a trendline to the Charge Transfer Resistance (Rct) vs Cycle plot
fig_Rct_trendline = px.scatter(df_cleaned, x='Cycle', y='Rct',
                               title='Charge Transfer Resistance (Rct) vs Charge/Discharge Cycles with Trendline',
                               labels={'Rct': 'Charge Transfer Resistance (Ohms)', 'Cycle': 'Cycle Number'},
                               trendline="ols")

# Show the plot with trendline
fig_Rct_trendline.show()


# Save the plots as interactive HTML files
fig_impedance.write_html("battery_impedance_plot.html")
fig_Re.write_html("electrolyte_resistance_plot.html")
fig_Rct.write_html("charge_transfer_resistance_plot.html")

# Save plots with trendlines as well
fig_impedance_trendline.write_html("battery_impedance_trendline_plot.html")
fig_Re_trendline.write_html("electrolyte_resistance_trendline_plot.html")
fig_Rct_trendline.write_html("charge_transfer_resistance_trendline_plot.html")
