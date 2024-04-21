import pandas as pd

# Read CSV files
df1 = pd.read_csv(r'C:\Users\ramru\Downloads\Florida_Sea_Level.csv')
df2 = pd.read_csv(r'C:\Users\ramru\Downloads\Housing_Data.csv')
df3 = pd.read_csv(r'C:\Users\ramru\Downloads\formatted_file.csv')
df3temp = pd.read_csv(r'C:\Users\ramru\Downloads\Incidents_0or1.csv')
df4 = pd.read_excel(r'C:\Users\ramru\Downloads\finalrent.xlsx')

df1_july2016_to_feb2024 = df1[
    (df1['Year'] >= 2016) & ((df1['Year'] > 2016) | (df1['Month'] >= 7)) & (df1['Year'] <= 2024)].copy()
df1_july2016_to_feb2024['Month'] = df1_july2016_to_feb2024['Month'].apply(lambda x: '{:02}'.format(x))
df1_july2016_to_feb2024['month_year'] = df1_july2016_to_feb2024['Year'].astype(str) + df1_july2016_to_feb2024[
    'Month']

df2_florida = df2[df2['state_id'] == 'FL']

df3 = pd.merge(df3, df3temp)
df3_july2016_to_feb2024 = df3[
    (df3['month_year'] >= 201607) & (df3['month_year'] <= 202403)].copy()
df3_july2016_to_feb2024['month_year'] = df3_july2016_to_feb2024['month_year'].astype(str)

df4_july2016_to_feb2024 = df4[
    (df4['month_year'] >= 201607) & (df4['month_year'] <= 202403)].copy()
df4_july2016_to_feb2024['month_year'] = df4_july2016_to_feb2024['month_year'].astype(str)

merged_df = pd.merge(df1_july2016_to_feb2024, df2_florida, on='month_year')
merged_df = pd.merge(merged_df, df3_july2016_to_feb2024, on='month_year')
merged_df = pd.merge(merged_df, df4_july2016_to_feb2024, on='month_year')
merged_df.drop(
    columns=['Year', 'Month', 'state', ' High_Conf.', 'Low_Conf.', 'state_id', 'median_days_on_market',
             'median_days_on_market_mm',
             'median_days_on_market_yy', 'pending_listing_count', 'pending_listing_count_mm',
             'pending_listing_count_yy', 'median_listing_price_per_square_foot',
             'median_listing_price_per_square_foot_mm', 'median_listing_price_per_square_foot_yy', 'median_square_feet',
             'median_square_feet_mm', 'median_square_feet_yy', 'pending_ratio', 'pending_ratio_mm', 'pending_ratio_yy',
             'quality_flag', 'median_listing_price_mm', 'median_listing_price_yy', 'active_listing_count_mm',
             'active_listing_count_yy', 'new_listing_count_mm', 'new_listing_count_yy', 'price_increased_count_mm',
             'price_increased_count_yy', 'price_reduced_count_mm', 'price_reduced_count_yy', 'average_listing_price_mm',
             'average_listing_price_yy', 'total_listing_count_mm', 'total_listing_count_yy'], inplace=True)
merged_df['Monthly_MSL'] = merged_df['Monthly_MSL'].apply(lambda x: x * 100000)
merged_df.to_csv(r'C:\Users\ramru\Downloads\SeaLevelZillowDisastersRent(final).csv', index=False)
