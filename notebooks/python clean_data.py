import pandas as pd


df = pd.read_excel('supplier_quotes.csv.xlsx')


df['timestamp'] = pd.to_datetime('1899-12-30') + pd.to_timedelta(df['timestamp'], unit='D')


numerical_cols = ['shipping_costs', 'lead_time_days', 'supplier_reliability_score', 'delivery_time_deviation']
df[numerical_cols] = df[numerical_cols].fillna(0)


df['cost_per_day'] = df['shipping_costs'] / df['lead_time_days'].replace(0, 1)  # Avoid div by zero


df.to_csv('cleaned_supplier_quotes.csv', index=False)
print("Cleaning complete. Summary:\n", df.describe())
