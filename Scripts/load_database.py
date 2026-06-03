import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

fund_master = pd.read_csv(
    "Data/processed/01_fund_master_cleaned.csv"
)

nav_history = pd.read_csv(
    "Data/processed/02_nav_history_cleaned.csv"
)

fund_master.to_sql(
    "fund_master",
    engine,
    if_exists="replace",
    index=False
)

nav_history.to_sql(
    "nav_history",
    engine,
    if_exists="replace",
    index=False
)

print("Database Created Successfully!")