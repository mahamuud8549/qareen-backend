import pyodbc

# Macluumaadka isku xirka (Connection String)
# Waxaan u isticmaalaynaa magaca Server-kaaga: MAXAMUUDPC\SQLEXPRESS
connection_string = (
    "Driver={SQL Server};"
    "Server=MAXAMUUDPC\\SQLEXPRESS;"
    "Database=SanjabiilDB;"
    "Trusted_Connection=yes;"
)

try:
    # 1. La xiriir SQL Server
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    print("Xiriirka SQL Server waa guuleystay!")

    # 2. Soo saar xogta Menu-ka
    cursor.execute("SELECT Magaca, Qiimaha FROM Menu")
    
    print("\n--- MENU-KA SANJABIIL ---")
    for row in cursor:
        print(f"Cuntada: {row.Magaca} | Qiimaha: ${row.Qiimaha}")

except Exception as e:
    print(f"Cilad ayaa dhacday: {e}")