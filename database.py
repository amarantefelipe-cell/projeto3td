import sqlite3

DATABASE = "cultura_plus.db"

def get_connection():
    """Cria e retorna uma conexão com o banco de dados SQLite."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Executa o script schema.sql para criar as tabelas."""
    with open("schema.sql", "r") as f:
        script = f.read()
    conn = get_connection()
    conn.executescript(script)
    conn.commit()
    conn.close()
