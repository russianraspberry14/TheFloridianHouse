import pandas as pd
import matplotlib.pyplot as plt
import plotly.plotly as py
d = pd.read_csv('Hurricane_file.csv')
d2 = pd.read_csv('formatted_file.csv')
dfinal = pd.merge(d, d2, on='datemonth', how='inner')
dfinal['datemonth'] = pd.to_datetime(dfinal['datemonth'], format='%Y%m')
d['datemonth'] = pd.to_datetime(d['datemonth'], format='%Y%m')
dfinal.to_csv('hurricaneFinal.csv', index = False)
plt.plot(dfinal['datemonth'], dfinal['Florida_average'], marker = ".",color='g')
plt.plot(d['datemonth'], [0] * len(d['datemonth']), marker = "*", color = 'r')
plt.xlabel("Month and Year")
plt.ylabel("Housing Average")
plt.title('Plot of Florida Average vs DateMonth')
plt.savefig('plot1.png')
mpl_fig = plt.figure()
unique_url = py.plot_mpl(mpl_fig, filename="my first plotly plot")
