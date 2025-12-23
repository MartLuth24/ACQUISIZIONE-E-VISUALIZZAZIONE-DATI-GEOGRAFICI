-- Tabella osservazioni
CREATE TABLE IF NOT EXISTS osservazioni (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    sorgente TEXT,
    posizione GEOGRAPHY(Point, 4326)
);

-- Tabella traiettorie
CREATE TABLE IF NOT EXISTS traiettorie (
    id SERIAL PRIMARY KEY,
    sorgente TEXT,
    percorso GEOGRAPHY(LineString, 4326),
    lunghezza_m DOUBLE PRECISION,
    velocita_media_ms DOUBLE PRECISION,
    inizio TIMESTAMP,
    fine TIMESTAMP
);
