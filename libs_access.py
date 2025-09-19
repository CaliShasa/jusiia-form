import gspread
from oauth2client.service_account import ServiceAccountCredentials

def access_gsheet(SHEET_NAME=""):
    scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)
    # Apri il Google Sheet
    SHEET_NAME = "Modulo senza titolo (Risposte)"  
    sheet = client.open(SHEET_NAME).sheet1

    return sheet


def normalize_text(s: str) -> str:
    if isinstance(s, str):
        s = (
            s.replace("CO₂", "CO2")   # pedice 2 → normale
             .replace("Co2", "CO2")
             .replace("’", "'")       # apostrofo tipografico
             .replace("“", '"').replace("”", '"')  # virgolette tipografiche
             .replace("％", "%")      # percentuale full-width → ASCII
             .replace(">=", "≥")     # normalizza >= in ≥
             .replace("–", "-")      # en-dash → hyphen
             .strip()
        )
        return s
    return s

# access.py

import pandas as pd
from libs_mappings import (
    scoring_economica,
    scoring_salute,
    scoring_tecnologica,
    scoring_territoriale,
    scoring_educativa,
    scoring_generazionale,
    scoring_istituzionale_governance,
    scoring_istituzionale_stakeholder,
    scoring_sociale_equita,
    scoring_sociale_lavoro,
    scoring_ambientale_emissioni,
    scoring_ambientale_rifiuti
)

def applica_mapping(df: pd.DataFrame) -> pd.DataFrame:
    df["Punteggio_Economica"] = df["Dimensione Economica"].map(scoring_economica)
    df["Punteggio_Salute"] = df["Dimensione Salute"].map(scoring_salute)
    df["Punteggio_Tecnologica"] = df["Dimensione Tecnologica"].map(scoring_tecnologica)
    df["Punteggio_Territoriale"] = df["Dimensione Territoriale"].map(scoring_territoriale)
    df["Punteggio_Educativa"] = df["Dimensione Educativa, Culturale e Cognitiva"].map(scoring_educativa)
    df["Punteggio_Generazionale"] = df["Dimensione Generazionale"].map(scoring_generazionale)
    df["Punteggio_Istituzionale_Governance"] = df["Dimensione Istituzionale - Governance"].map(scoring_istituzionale_governance)
    df["Punteggio_Istituzionale_Stakeholder"] = df["Dimensione Istituzionale - Stakeholder"].map(scoring_istituzionale_stakeholder)
    df["Punteggio_Sociale_Equita"] = df["Dimensione Sociale e Dei Diritti Civili"].map(scoring_sociale_equita)
    df["Punteggio_Sociale_Lavoro"] = df["Dimensione Sociale e Dei Diritti Civili - Lavoro"].map(scoring_sociale_lavoro)
    df["Punteggio_Ambientale_Emissioni"] = df["Dimensione Ambientale - Emissioni"].map(scoring_ambientale_emissioni)
    df["Punteggio_Ambientale_Rifiuti"] = df["Dimensione Ambientale - Gestione dei rifiuti"].map(scoring_ambientale_rifiuti)
    return df

def calcola_punteggio(df):
    import math

    # 1. Calcola punteggio istituzionale (media con arrotondamento per eccesso)
    df["Punteggio_Istituzionale"] = ((df["Punteggio_Istituzionale_Governance"] +
                                    df["Punteggio_Istituzionale_Stakeholder"]) / 2).apply(math.ceil)

    # 2. Calcola il moltiplicatore direttamente dalla formula
    df["Istituzionale_Factor"] = 1 + (df["Punteggio_Istituzionale"] - 3) / 10

    # 3. Calcola le altre medie
    df["Punteggio_Sociale"] = ((df["Punteggio_Sociale_Equita"] +
                                df["Punteggio_Sociale_Lavoro"]) / 2).apply(math.ceil)

    df["Punteggio_Ambientale"] = ((df["Punteggio_Ambientale_Emissioni"] +
                                df["Punteggio_Ambientale_Rifiuti"]) / 2).apply(math.ceil)

    # 4. Calcola la media grezza di tutte le 9 dimensioni
    df["Raw_Average"] = (
        df["Punteggio_Istituzionale"]
        + df["Punteggio_Sociale"]
        + df["Punteggio_Ambientale"]
        + df["Punteggio_Economica"]
        + df["Punteggio_Salute"]
        + df["Punteggio_Tecnologica"]
        + df["Punteggio_Territoriale"]
        + df["Punteggio_Educativa"]
        + df["Punteggio_Generazionale"]
    ) / 9

    # 5. Formula finale come da documento
    df["Final_Score"] = df["Raw_Average"] * df["Istituzionale_Factor"]

    return df