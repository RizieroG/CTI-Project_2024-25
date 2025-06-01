# Indice

- [Introduzione](#cti-project_2024-25)
- [Obiettivo](#obiettivo)
- [Reports Utilizzati](#reports-utilizzati)
  - [APT29 Report](#apt29-report)
  - [CARBANAK Report](#carbanak-report)
  - [FIN6 Report](#fin6-report)
  - [FIN7 Report](#fin7-report)
  - [OILRIG Report](#oilrig-report)
  - [SANDWORM Report](#sandworm-report)
  - [Black Basta Report](#black-basta-report)
  - [Conti Report](#conti-report)
- [Note](#note)

# CTI-Project_2024-25

Raccolta e analisi di report relativi a diversi gruppi APT e campagne ransomware, svolta come progetto per il corso di Software Security all’Università di Napoli.

Questo dataset include vari report su minacce avanzate e gruppi cybercriminali.

**Partecipanti:** Riziero Graziani, Stefano Angelo Riviello, Andrea Esposito

## Obiettivo

Per ogni APT analizzato sono stati considerati i seguenti aspetti:

* **Vulnerabilità sfruttate**: identificazione tramite CVE, punteggio di gravità CVSS, categorizzazione CWE, prodotti vulnerabili tramite CPE, probabilità di sfruttamento con EPSS, e inclusione nella lista KEV delle vulnerabilità note come attivamente sfruttate. È stato inoltre utilizzato il progetto CVSS-BT per l’arricchimento dei dati.

* **Cronologia della vulnerabilità**: per ogni vulnerabilità è indicata la data di divulgazione pubblica, la disponibilità di patch, e l’evoluzione delle analisi e mitigazioni nel tempo, distinguendo tra zero-day e vulnerabilità già note.

* **Tecniche MITRE ATT\&CK**: mappatura delle principali tattiche e tecniche utilizzate dagli attaccanti, come Lateral Movement, Privilege Escalation, Initial Access, Execution, e altre a seconda del caso.

* **Strumenti e tool**: elenco dei principali strumenti utilizzati dagli attaccanti, come RAT (Remote Access Trojan), strumenti di escalation dei privilegi ed exploit kit specifici.

* **Prodotti vulnerabili**: specifica della tipologia (sistemi operativi, software o hardware), versioni coinvolte e distribuzione dell’impatto.

* **Altri elementi utili**: indicazione di IOC (Indicators of Compromise) come IP, hash, domini o URL, utili per l’identificazione di attività malevole, e descrizione di eventuali simulazioni di laboratorio eseguibili per replicare l’attacco.

## Reports Utilizzati

Di seguito mostriamo i documenti utilizzati per le nostre analisi.

### APT29 Report

| Title | Document | Identifier |
|---|---|---|
| [THE DUKES 7 YEARS OF RUSSIAN CYBERESPIONAGE](https://blog-assets.f-secure.com/wp-content/uploads/2020/03/18122307/F-Secure_Dukes_Whitepaper.pdf) | F-Secure_Dukes_Whitepaper.pdf | DUKES |

### CARBANAK Report

| Title | Document | Identifier |
|---|---|---|
| [CARBANAK APT THE GREAT BANK ROBBERY](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08064518/Carbanak_APT_eng.pdf) | Carbanak_APT_eng.pdf | KASPERSKY2 |

### FIN6 Report

| Title | Document | Identifier |
|---|---|---|
| [More_eggs, Anyone? Threat Actor ITG08 Strikes Again](https://securityintelligence.com/posts/more_eggs-anyone-threat-actor-itg08-strikes-again/) | FIN6-SecurityIntelligence_9.pdf | SECURITYINTELLIGENCE9 |

### FIN7 Report

| Title | Document | Identifier |
|---|---|---|
| [Profile of an Adversary – FIN7](https://www.deepwatch.com/labs/profile-of-an-adversary-fin7/) | Profile of an Adversary - FIN7 _ Deepwatch.pdf | DEEPWATCH |

### OILRIG Report

| Title | Document | Identifier |
|---|---|---|
| [APT34: The Helix Kitten Cybercriminal Group Loves to Meow Middle Eastern and International Organizations](https://www.cyware.com/blog/apt34-the-helix-kitten-cybercriminal-group-loves-to-meow-middle-eastern-and-international-organizations-48ae) | APT34 The Helix Kitten Cybercriminal Group Loves to Meow Middle Eastern and International Organizations.pdf | CYWARE |

### SANDWORM Report

| Title | Document | Identifier |
|---|---|---|
| [CRASHOVERRIDE Analysis of the Threat to Electric Grid Operations](https://www.dragos.com/wp-content/uploads/CrashOverride-01.pdf) | CrashOverride.pdf | CRASHOVERRIDE |

### Black Basta Report

| Title | Document | Identifier |
|---|---|---|
| [Ransomware Roundup - Black Basta](https://www.fortinet.com/blog/threat-research/ransomware-roundup-black-basta) | Ransomware Roundup - Black Basta _ FortiGuard Labs.pdf | FortiGuard Labs |

### Conti Report

| Title | Document | Identifier |
|---|---|---|
| [Conti Leaks](https://www.forescout.com/resources/analysis-of-conti-leaks/) | ContiLeaks.pdf | Forescout |

## Note

Questo progetto si basa e approfondisce il lavoro svolto dai nostri colleghi **Sofia Della Penna** e **Lorenzo Parracino** con il progetto basato su [CTI-HAL](https://github.com/dessertlab/CTI-HAL/tree/main).
Per maggiori dettagli sulla loro ricerca, si rimanda alla [repository CTI-HAL](https://github.com/dessertlab/CTI-HAL/tree/main) e al paper:
[CTI-HAL: A Human-Annotated Dataset for Cyber Threat Intelligence Analysis](https://arxiv.org/html/2504.05866v1).
