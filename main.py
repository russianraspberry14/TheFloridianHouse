import pandas as pd
import matplotlib.pyplot as plt
import plotly.plotly as py
def generateWholeGraph():
    d = pd.read_csv('us_disaster_declarations.csv')
    """d -> US Disaster -> Modified File
    d2 -> date, Florida state index, statefile -> formatted file
    df -> d with only Florida data, particular columns, and year >=2000
    df4 -> Particular disaster files
    """
    # Filter DataFrame to keep only rows where the second column is 'FL'
    df = d[d.iloc[:, 0].isin(['FL', 'state'])]
    df.iloc[:, 2] = pd.to_numeric(df.iloc[:, 2], errors='coerce')
    columns_to_keep = [0,2,3,4,5, 10, 11, 12, 18] 
    df = df.iloc[:, columns_to_keep]
    df = df[df.iloc[:, 2] >= 2000]
    df.dropna(axis=1, how='all', inplace=True)
    df.drop_duplicates(inplace=True)
    df['incident_begin_date'] = pd.to_datetime(df['incident_begin_date'])
    df['incident_begin_date'] = df['incident_begin_date'].dt.strftime('%Y%m')
    df.rename(columns={'incident_begin_date': 'datemonth'}, inplace=True)
    # Save filtered DataFrame to CSV
    df.to_csv('modified_file.csv', index=False)

    #Making files for different disaster types:
    df4 = df[df.iloc[:, 2] == 'Fire']
    df4.to_csv("Fire" + '_file.csv', index=False)
    df4 = df[df.iloc[:, 2] == 'Severe Storm']
    df4.to_csv("Freezing" + '_file.csv', index=False)
    df4 = df[df.iloc[:, 2] == 'Hurricane']
    df4.to_csv("Hurricane" + '_file.csv', index=False)
    df4 = df[df.iloc[:, 2] == 'Biological']
    df4.to_csv("Biological" + '_file.csv', index=False)
    #################################

    d2 = pd.read_csv("State_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv")
    # Convert the date column to datetime format
    d2['Date'] = pd.to_datetime(d2['Date'], format='%m/%d/%y')
    # Format the date column to yyyy format
    d2['Date'] = d2['Date'].dt.strftime('%Y%m')
    d2.rename(columns={'Date': 'datemonth'}, inplace=True)
    d2.to_csv('formatted_file.csv', index=False)

    # Group by the values in the first column and calculate the average of the second column
    average_values = d2.groupby('datemonth')['Florida'].mean()

    # Merge the average values back into the original DataFrame
    d2 = d2.merge(average_values, left_on='datemonth', right_index=True, suffixes=('', '_average'))
    d2.to_csv('formatted_file.csv', index=False)
    # Rename the column containing the average values
    d2.rename(columns={'year': 'average'}, inplace=True)
    d2.to_csv('formatted_file.csv', index=False)
    d2.drop(columns=['Florida'], inplace=True)
    d2.drop_duplicates(inplace=True)
    d2.to_csv('formatted_file.csv', index=False)

    # Save the DataFrame back to the same CSV file
    dfinal = pd.merge(df, d2, on='datemonth', how='outer')
    dfinal.to_csv('final_file.csv', index=False)

    #Start plotting the graph:
    dfinal['datemonth'] = pd.to_datetime(dfinal['datemonth'], format='%Y%m')
    column1 = dfinal['datemonth']
    column2 = dfinal['Florida_average']
    df['datemonth'] = pd.to_datetime(df['datemonth'], format='%Y%m')
    column3 = df['datemonth']
    #Change in housing average
    ax = plt.plot(column1, column2, marker = ".",color='g')
    plt.plot(column3, [0] * len(column3), marker = "*", color = 'r')
    #When the disasters hit
    plt.xlabel("Month and Year")
    plt.ylabel("Housing Average")
    plt.title('Plot of Florida Average vs DateMonth')
    plt.savefig('plot.png')
    mpl_fig = plt.figure()
    unique_url = py.plot_mpl(mpl_fig, filename="my first plotly plot")

