import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = "capstone_data.csv"

df = pd.read_csv(file_path)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df['Timestamp (s)'], df['Voltage ai6 (V)'], label='Voltage ai6', color='b')
plt.plot(df['Timestamp (s)'], df['Voltage ai0 (V)'], label='Voltage ai0', color='r')

# Labels and title
plt.xlabel('Timestamp (s)')
plt.ylabel('Voltage (V)')

# Show grid and legend
plt.grid(True)
plt.legend()



coeffs = np.polyfit(df['Timestamp (s)'], df['Voltage ai6 (V)'], 1)
slope6, intercept6 = coeffs
print (f"Trendline for Channel 6: y = {slope6}x + {intercept6}")

coeffs = np.polyfit(df['Timestamp (s)'], df['Voltage ai0 (V)'], 1)
slope0, intercept0 = coeffs
print(f"Trendline for Channel 0: y = {slope0}x + {intercept0}")

# u6 = 2.55 * .006842007
# u0 = 2.55 * .006917585
# print(f"Uncertainty for Channel 6: {u6}")
# print(f"Uncertainty for Channel 0: {u0}")

# Display the plot
plt.show()

