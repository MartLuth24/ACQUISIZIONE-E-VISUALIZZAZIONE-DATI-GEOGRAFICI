-- ============================
-- ANALISI OSSERVAZIONI
-- ============================

SELECT 
    id,
    timestamp,
    sorgente,
    ST_AsText(posizione) AS posizione_testo
FROM osservazioni
ORDER BY id DESC;
