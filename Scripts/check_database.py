import sqlite3

conn = sqlite3.connect("bluestock_mf.db")

cursor = conn.cursor()

cursor.execute("""
SELECT fund_house,
       COUNT(*)
FROM fund_master
GROUP BY fund_house
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()