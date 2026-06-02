import requests
import pandas as pd
import os

os.makedirs("Data/raw", exist_ok=True)

schemes = {
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_largecap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

for name, code in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    print(f"\n{name}")

    print(data["meta"]["scheme_name"])

    df = pd.DataFrame(data["data"])

    df.to_csv(f"Data/raw/{name}.csv", index=False)

print("\nAll NAV files saved successfully!")
print("Code:", code)
print("Scheme:", data["meta"]["scheme_name"])