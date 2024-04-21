import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Read the CSV file
df = pd.read_csv('SeaLevelZillowDisastersRent(final).csv')

# Convert 'month_year' column to datetime format
df['month_year'] = pd.to_datetime(df['month_year'], format='%Y%m')
filtered_df = df[df['incident_value'] >= 1]

# Plotting
plt.plot(df['month_year'], df['price_increased_count'], color='g', label='Price Increase Count')
plt.plot(filtered_df['month_year'], filtered_df['incident_value'], marker="*", color='r', label='Disasters')
plt.xlabel("Month and Year")
plt.ylabel("Price Increase Count")
plt.title('Price Increase Count and Disasters vs Month')
plt.legend()

# Creating Plotly figure
plotly_fig = go.Figure()

# Adding traces to Plotly figure
for line in plt.gca().get_lines():
    y = line.get_ydata()
    x = line.get_xdata()
    mode = 'lines' if line.get_label() == 'Price Increase Count' else 'markers'
    name = line.get_label()
    plotly_fig.add_trace(go.Scatter(x=x, y=y, mode=mode, name=name))

# Show Plotly figure
plotly_fig.show()
