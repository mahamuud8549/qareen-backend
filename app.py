import psycopg2
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 1. Furayaasha Cloud-ka (Xogtaadu waa diyaar)
DB_URL = "postgresql://qareendb_user:8LZoaTaKMFo9aUz3sb0v11odqMpuKddy@dpg-d7li6pojs32c7387291g-a.ohio-postgres.render.com/qareendb"
TELEGRAM_TOKEN = "8519692108:AAFjpwzdgUc0Lp7E2jb0AEasoCFZRS1Uc0E"
CHAT_ID = "8243770547" 

def send_to_telegram(magaca, nooca, farriinta):
    text = (
        f"⚖️ *DACWAD CUSUB AYAA SOO DHACDAY!*\n\n"
        f"👤 *Magaca:* {magaca}\n"
        f"📂 *Nooca:* {nooca}\n"
        f"💬 *Farriinta:* {farriinta}"
    )
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}&parse_mode=Markdown"
    try:
        requests.get(url)
    except Exception as e:
        print(f"Telegram Error: {e}")

@app.route('/send-booking', methods=['POST'])
def send_booking():
    try:
        data = request.json
        magaca = data.get('magaca')
        nooca = data.get('nooca')
        farriinta = data.get('farriinta')

        # Keydinta Cloud Database (Render)
        conn = psycopg2.connect(DB_URL, sslmode='require')
        cur = conn.cursor()
        # Abuur table-ka haddii uusan jirin
        cur.execute("CREATE TABLE IF NOT EXISTS Ballamaha (id SERIAL PRIMARY KEY, Magaca TEXT, Nooca TEXT, Fariinta TEXT)")
        cur.execute("INSERT INTO Ballamaha (Magaca, Nooca, Fariinta) VALUES (%s, %s, %s)", (magaca, nooca, farriinta))
        conn.commit()
        cur.close()
        conn.close()

        # Ogeysiiska Telegram-ka Mobile-kaaga
        send_to_telegram(magaca, nooca, farriinta)

        return jsonify({"status": "success", "message": "Dacwadda waa la gudbiyey!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(port=5000)