import pandas as pd

fund_master = pd.read_csv(
    "Data/raw/01_fund_master.csv"
)

print("\nMissing Values:")
print(fund_master.isnull().sum())

print("\nDuplicates:")
print(fund_master.duplicated().sum())

print("\nData Types:")
print(fund_master.dtypes)
 
fund_master["launch_date"] = pd.to_datetime(
    fund_master["launch_date"]
)

print(fund_master.dtypes)
 
fund_master.to_csv(
    "Data/processed/01_fund_master_cleaned.csv",
    index=False
)

print("\nFund Master Cleaned File Saved!")