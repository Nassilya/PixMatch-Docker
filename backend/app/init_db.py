import psycopg2

def init_db():
    try:
        conn = psycopg2.connect("host=db dbname=pixmatcher user=user password=password")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS wordnet (class_id TEXT PRIMARY KEY, label TEXT);")
        
        # On insère quelques faux labels pour la démo
        labels = [("n01234560", "Chien"), ("n01234561", "Chat"), ("n01234562", "Voiture")]
        for cid, lbl in labels:
            cur.execute("INSERT INTO wordnet (class_id, label) VALUES (%s, %s) ON CONFLICT DO NOTHING", (cid, lbl))
            
        conn.commit()
        cur.close()
        conn.close()
        print("Base de données de simulation prête !")
    except Exception as e:
        print(f"Erreur DB : {e}")

if __name__ == "__main__":
    init_db()