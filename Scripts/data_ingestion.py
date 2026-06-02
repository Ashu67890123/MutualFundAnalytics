import pandas as pd
import os

folder = "Data/raw"

for file in os.listdir(folder):

    if file.endswith(".csv"):

        path = os.path.join(folder, file)

        df = pd.read_csv(path)

        print("\n" + "="*60)
        print("FILE:", file)

        print("\nSHAPE:")
        print(df.shape)

        print("\nDTYPES:")
        print(df.dtypes)

        print("\nMISSING VALUES:")
        print(df.isnull().sum())

        print("\nHEAD:")
        print(df.head())

# ---------- AMFI Validation ----------

fund_master = pd.read_csv("Data/raw/01_fund_master.csv")
nav_history = pd.read_csv("Data/raw/02_nav_history.csv")

fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

print("\n" + "="*60)
print("AMFI VALIDATION")
print("All fund_master AMFI codes exist in nav_history?")
print(fund_codes.issubset(nav_codes))