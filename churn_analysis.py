import pandas as pd
import sqlite3

# 1. Dataset load karein
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

# 2. TotalCharges column clean karein
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)

# 3. Churn count check karein
print("--- CHURN COUNT SUMMARY ---")
print(df['Churn'].value_counts())

# 4. SQLite Database banakar data save karein
conn = sqlite3.connect('churn_db.db')
df.to_sql('customer_churn', conn, if_exists='replace', index=False)
conn.close()

print("\nSuccess! Database 'churn_db.db' aur table 'customer_churn' successfully ban gayi hai.")
# Yeh line code mein add kar dein
df.to_csv('cleaned_churn_data.csv', index=False)