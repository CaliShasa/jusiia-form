import gspread
import math
import pandas as pd
import importlib
import os
from dotenv import load_dotenv
from libs_access import access_gsheet, applica_mapping, calcola_punteggio, normalize_text
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


# 🔑 carica le variabili da auth.env
load_dotenv("auth.env")


def check_and_process():
    print("🔄 Connessione al Google Sheet...")
    sheet = access_gsheet()
    print(f"✅ Connesso al foglio: {sheet.title}")

    print("📥 Recupero dati...")
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    print(f"✅ {len(df)} righe lette dal foglio")
    print(f"📊 Colonne trovate nel DataFrame: {list(df.columns)}")

    # Normalizza il testo
    print("🧹 Normalizzazione testi...")
    df = df.applymap(normalize_text)

    for index, row in df.iterrows():
        processed_val = str(row.get("Processed")).strip().lower()
        print(f"\n➡️ Riga {index+2} (Processed={processed_val})")

        if processed_val != "yes":
            print("   🔎 Riga non ancora processata, procedo...")

            # Estrai singola riga
            df_single = pd.DataFrame([row])
            print("   📌 Riga estratta:", df_single.to_dict(orient="records")[0])

            # Applica mapping
            print("   🔄 Applico mapping...")
            df_mapped = applica_mapping(df_single)

            # Calcolo punteggio
            print("   🧮 Calcolo punteggio...")
            df_scored = calcola_punteggio(df_mapped)
            score = round(df_scored["Final_Score"].iloc[0], 2)
            print(f"   ✅ Punteggio calcolato: {score}")

            # Scrivi punteggio sul foglio
            try:
                col_score = df.columns.get_loc("Punteggio") + 1
                sheet.update_cell(index + 2, col_score, score)
                print(f"   ✅ Punteggio salvato nel foglio: {score}")
            except Exception as e:
                print(f"   ❌ Errore nel salvataggio del punteggio: {e}")

            # Invio email
            email_dest = row.get("Indirizzo email", "").strip()
            if email_dest:
                print(f"   📧 Invio email a {email_dest}...")
                try:
                    send_email(email_dest, score)
                    print(f"   ✅ Email inviata a {email_dest} con punteggio {score}")
                except Exception as e:
                    print(f"   ❌ Errore nell'invio email a {email_dest}: {e}")
            else:
                print("   ⚠️ Nessun indirizzo email trovato, salto invio.")

            # Aggiorna colonna Processed
            try:
                col_processed = df.columns.get_loc("Processed") + 1
                sheet.update_cell(index + 2, col_processed, "Yes")
                print("   ✅ Riga marcata come Processed")
            except Exception as e:
                print(f"   ❌ Errore nell'aggiornare Processed: {e}")

        else:
            print("   ⏩ Riga già processata, salto.")


def send_email(to_email, score):
    """Invia una mail con SendGrid leggendo l'API key da auth.env"""
    api_key = os.getenv("SENDGRID_API_KEY")
    if not api_key:
        raise ValueError("❌ Nessuna API key trovata. Verifica il file auth.env.")

    message = Mail(
        from_email='calishasa@gmail.com',
        to_emails=to_email,
        subject='Il tuo punteggio è pronto!',
        html_content=f"<strong>Il tuo punteggio finale è: {score}</strong>"
    )

    sg = SendGridAPIClient(api_key)
    sg.host = 'https://api.eu.sendgrid.com'
    sg.send(message)


if __name__ == "__main__":
    check_and_process()
