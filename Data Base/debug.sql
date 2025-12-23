-- ============================
-- DEBUG STRUTTURA DATABASE
-- ============================

-- Elenco tabelle
SELECT table_schema, table_name
FROM information_schema.tables
WHERE table_type = 'BASE TABLE'
ORDER BY table_schema, table_name;

-- Struttura tabella osservazioni
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'osservazioni';
