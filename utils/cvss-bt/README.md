# CVSS-BT Lookup

Uno script Python per consultare rapidamente tutte le informazioni disponibili su una specifica CVE, arricchite dal dataset [cvss-bt](https://github.com/t0sche/cvss-bt).

## Table of Contents

- [Introduzione](#introduzione)
- [Come funziona](#come-funziona)
- [Istruzioni d’uso](#istruzioni-duso)
- [Requisiti](#requisiti)
- [Spiegazione dei campi](#spiegazione-dei-campi)
- [Suggerimenti](#suggerimenti)
- [Maggiori dettagli su cvss-bt](#maggiori-dettagli-su-cvss-bt)

## Introduzione

La gestione delle vulnerabilità non si basa solo sul punteggio CVSS standard, ma deve considerare anche informazioni aggiuntive come la probabilità di exploit, la presenza di exploit pubblici e l’effettivo sfruttamento in-the-wild.  
Il progetto [cvss-bt](https://github.com/t0sche/cvss-bt) arricchisce i dati CVSS integrando queste informazioni in un unico file CSV aggiornato periodicamente. Per maggiori informazioni, o per maggiori curiosità, si consiglia di fare sempre riferimento alla documentazione/README del progetto stesso.

Questo script permette di **inserire l’ID di una CVE** e ottenere immediatamente tutte le informazioni correlate presenti nel file `cvss-bt.csv`, così da poter valutare con più accuratezza il rischio reale e la priorità di intervento.

## Come funziona

- Inserisci il file `cvss-bt.csv` (scaricabile dal repository [cvss-bt](https://github.com/t0sche/cvss-bt/releases)) nella stessa cartella dello script.
- Avvia lo script Python.
- Inserisci l’ID della CVE richiesta (es: `CVE-2024-24919`).
- Otterrai una stampa a video di tutte le informazioni arricchite per quella vulnerabilità.

## Istruzioni d’uso

1. Scarica questo repository o la singola cartella.
2. Scarica il file `cvss-bt.csv` dalla [pagina releases di cvss-bt](https://github.com/t0sche/cvss-bt/releases).
3. Posiziona sia lo script Python che il CSV nella stessa directory.
4. Esegui lo script:

    ```python
    python cerca_cve.py
    ```
5. Inserisci l’ID della CVE quando richiesto.

## Requisiti

- Python 3.x
- pandas (`pip install pandas`)

## Spiegazione dei campi

| Campo              | Spiegazione |
|--------------------|-------------|
| **cve**            | L’identificativo univoco della vulnerabilità (es: `CVE-2024-24919`). |
| **cvss-bt_score**  | Il punteggio “enriched” CVSS Base+Threat (CVSS-BT), cioè il punteggio CVSS base arricchito con le informazioni sulla minaccia effettiva (exploit, KEV, ecc). Più alto = più rischiosa/prioritaria. |
| **cvss-bt_severity** | Il livello di severità associato al punteggio CVSS-BT (es: HIGH, CRITICAL, MEDIUM). |
| **cvss-bt_vector** | La stringa vettoriale che descrive la composizione dettagliata del punteggio CVSS-BT secondo lo standard CVSS (quali metriche hanno contribuito). Può contenere anche una parte `E` (Exploitability) non presente nel base. |
| **cvss_version**   | Versione dello standard CVSS usato (es: 3.1, 4.0). |
| **base_score**     | Il punteggio CVSS “base”, cioè calcolato senza arricchimenti. È quello che trovi nel NVD. |
| **base_severity**  | Livello di severità associato al base score (HIGH, CRITICAL, ecc). |
| **base_vector**    | Vettore CVSS base, secondo lo standard, usato per calcolare il base score. |
| **assigner**       | L’ente/organizzazione che ha pubblicato la CVE. |
| **published_date** | Data di pubblicazione ufficiale della CVE. |
| **epss**           | Valore di EPSS (Exploit Prediction Scoring System): una probabilità da 0 a 1 che la vulnerabilità venga effettivamente sfruttata nel mondo reale. Più alto = più probabile venga sfruttata. |
| **cisa_kev**       | `True`/`False`: la vulnerabilità è presente nella lista delle vulnerabilità sfruttate attivamente secondo il catalogo CISA KEV (Known Exploited Vulnerabilities). Se True, è già stata usata in attacchi reali! |
| **vulncheck_kev**  | `True`/`False`: simile al campo sopra, ma secondo la fonte VulnCheck KEV. |
| **exploitdb**      | `True`/`False`: la vulnerabilità ha un exploit pubblico (PoC) su ExploitDB. |
| **metasploit**     | `True`/`False`: è disponibile un modulo per questa vulnerabilità su Metasploit, quindi può essere facilmente sfruttata tramite framework automatici. |
| **nuclei**         | `True`/`False`: esiste un template per il tool Nuclei (scanner automatico), utile per automatizzare la rilevazione. |
| **poc_github**     | `True`/`False`: esiste un exploit proof-of-concept pubblico su GitHub per questa vulnerabilità. |

## Suggerimenti

- Aggiorna periodicamente il file `cvss-bt.csv` per avere dati sempre aggiornati.
- Questo script può essere facilmente integrato in pipeline più grandi, ad esempio per automatizzare processi di vulnerability management.

## Maggiori dettagli su cvss-bt

Il tool cvss-bt serve per aiutarti a capire quanto è davvero pericolosa una vulnerabilità (CVE), non solo guardando il punteggio CVSS “base” che vedi sul National Vulnerability Database (NVD), ma anche tenendo conto di quante informazioni di “minaccia reale” ci sono su quella vulnerabilità, ad esempio se esistono exploit pubblici, se è già stata sfruttata da attaccanti, o se esistono strumenti automatici per sfruttarla.

Il punteggio CVSS base (quello che trovi di solito nei siti ufficiali) dà un’idea di quanto una vulnerabilità potrebbe essere pericolosa, ma non ti dice:

- Se esiste già un exploit automatico
- Se la vulnerabilità è stata già sfruttata “sul campo”
- Se esistono strumenti pubblici e facili da usare per attaccarla

Più precisamente:

1. Prende ogni CVE del catalogo NVD
2. Per ogni CVE, cerca se:
    - Esistono exploit pubblici (su GitHub, ExploitDB, Metasploit…)
    - È già stata usata in attacchi reali (fonti come CISA KEV, VulnCheck KEV)
    - Esiste codice funzionante e facile da usare (come moduli Metasploit)
    - Ha un punteggio EPSS alto (cioè la probabilità che venga sfruttata è alta)
3. Usa queste informazioni per arricchire il punteggio CVSS base, aggiungendo una componente chiamata Exploitability/Exploit Code Maturity (E).

**Perchè conviene usarlo?** Puoi vedere a colpo d’occhio non solo quanto potrebbe essere grave una vulnerabilità, ma anche quanto è probabile che venga sfruttata davvero, e se è già nel mirino degli attaccanti.

---

> Realizzato con ❤️ per chi vuole dare priorità alle patch più importanti e capire subito quali vulnerabilità sono davvero rischiose!
