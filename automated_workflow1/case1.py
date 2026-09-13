import sqlite3
import time
from datetime import datetime

#------base de donnees----

def init_db():
    conn = sqlite3.connect("demandes.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS demandes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT,
        status TEXT,
        date_creation TEXT,
        date_traitement TEXT)
        """)
    conn.commit()
    conn.close()
def ajouter_demande(description):
    conn = sqlite3.connect("demandes.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO demandes (description, status, date_creation, date_traitement)
        VALUES (?, ?, ?, ?)
        """, (description, "En attente", datetime.now().isoformat(), None))
    conn.commit()
    conn.close()

#-----workflow automatisé----
def traiter_demandes():
    conn = sqlite3.connect("demandes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, description FROM demandes WHERE status='En attente'")
    demandes = cursor.fetchall()
    for demande in demandes:
        id_demande,description = demande
        print(f"Traitement de la demande {id_demande} : {demande}")
        time.sleep(1) #simulation du temps de traitement

        cursor.execute("""
            UPDATE demandes
            SET status=?, date_traitement=?
            WHERE id=?
            """, ("Traité", datetime.now().isoformat(), id_demande))
        conn.commit()
        notifier(id_demande, description)
        
    conn.close()

#------Notification-----
def notifier(id_demande, description):
    print(f"📩 Notification : Demande {id_demande} ('{description}') traitée avec succès.")

#-----Exemple d'utilisation----
if __name__ == "__main__":
    init_db()

    # Ajout de nouvelles demandes
    ajouter_demande("Ouverture de compte client")
    ajouter_demande("Réinitialisation de mot de passe")
    ajouter_demande("Mise à jour des coordonnées")

    # Exécution du workflow automatisé
    traiter_demandes()
