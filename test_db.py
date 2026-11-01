import pymssql

conn = pymssql.connect(
    server=r"LAPTOP-707J6I72\HP",
    trusted=True,
    database="CollegeChatbot"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM FAQ")

for row in cursor:
    print(row)

conn.close()