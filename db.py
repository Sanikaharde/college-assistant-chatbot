import pymssql

conn = pymssql.connect(
    server="LAPTOP-707J6I72\\HP",
    user="sa",
    password="YOUR_PASSWORD",
    database="CollegeChatbot"
)

cursor = conn.cursor()