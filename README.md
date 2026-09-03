# Tirocinio UNIVR – Acquisizione e Visualizzazione Dati Geografici

## Descrizione del progetto
Il progetto di tirocinio ha come obiettivo l’apprendimento del linguaggio Python e
la sua integrazione con un database geografico a livello aziendale.

Il sistema implementato consente:
- l’acquisizione di dati tramite una telecamera (simulata)
- il salvataggio delle osservazioni su database PostGIS
- il calcolo di traiettorie e metriche spaziali
- la visualizzazione dei risultati su mappa interattiva

---

## Tecnologie utilizzate
- Python
- PostgreSQL
- PostGIS
- psycopg2
- imageio / OpenCV
- Folium

---

## Struttura del database
Il database è strutturato in due tabelle principali:

- **osservazioni**: memorizza i punti geografici acquisiti nel tempo
- **traiettorie**: memorizza i percorsi calcolati a partire dalle osservazioni

Le geometrie sono gestite tramite estensione PostGIS.

---

## Struttura del codice Python
Il codice è suddiviso in moduli separati:
- configurazione database
- acquisizione dati
- analisi e calcolo traiettorie
- visualizzazione geografica

Questa organizzazione rende il progetto modulare e facilmente estendibile.

---

## Visualizzazione
Le traiettorie vengono esportate in formato GeoJSON e visualizzate su una mappa
interattiva generata in HTML, primo passo verso una futura dashboard web.

---

## Obiettivi formativi raggiunti
- utilizzo di Python per applicazioni reali
- integrazione Python–PostgreSQL
- utilizzo di database geografici
- gestione e visualizzazione di dati spaziali
- strutturazione professionale di un progetto software
