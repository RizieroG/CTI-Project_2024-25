import pandas as pd

csv_path = "cvss-bt.csv"  # Sostituisci con il percorso corretto se necessario

def cerca_cve(csv_path):
    cve_id = input("Inserisci l'ID della CVE (es. CVE-2024-24919): ").strip()
    df = pd.read_csv(csv_path)
    risultato = df[df['cve'] == cve_id]
    if risultato.empty:
        print("CVE non trovata.")
    else:
        # Stampa tutte le informazioni in modo verticale
        print("\nRisultati per", cve_id)
        print("-" * 40)
        print(risultato.T)
        print("-" * 40)

# Avvia la funzione
cerca_cve(csv_path)

