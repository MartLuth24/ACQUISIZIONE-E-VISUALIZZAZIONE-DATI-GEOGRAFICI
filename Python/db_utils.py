import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="psw",
        host="localhost",
        port="5432"
    )

def insert_osservazione(sorgente, lon, lat):
    conn = get_connection()
    cur = conn.cursor()

    sql = """
    INSERT INTO osservazioni (sorgente, posizione)
    VALUES (%s, ST_GeogFromText(%s));
    """

    wkt = f"POINT({lon} {lat})"
    cur.execute(sql, (sorgente, wkt))

    conn.commit()
    cur.close()
    conn.close()


def get_traiettorie():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            sorgente,
            ST_AsGeoJSON(percorso)
        FROM traiettorie;
    """)

    dati = cur.fetchall()
    cur.close()
    conn.close()

    return dati

# In questo codice ho solo messo il database quindi qua non c'è il video
