-- =========================================
-- SCHEMA DATABASE - PROGETTO TIROCINIO UNIVR
-- =========================================

-- 1) Estensione geografica
CREATE EXTENSION IF NOT EXISTS postgis;

-- 2) Tabella osservazioni
CREATE TABLE IF NOT EXISTS osservazioni (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    sorgente TEXT NOT NULL,
    posizione GEOGRAPHY(Point, 4326) NOT NULL
)

-- =========================================
-- ESTENSIONE MODELLO DATI
-- =========================================

CREATE TABLE IF NOT EXISTS traiettorie(
    id SERIAL PRIMARY KEY,
	sorgente TEXT NOT NULL,
	percorso GEOGRAPHY(LineString, 4326),
	inizio TIMESTAMP,
	fine TIMESTAMP
	
);
