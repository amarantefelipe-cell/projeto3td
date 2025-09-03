DROP TABLE IF EXISTS usuarios;
DROP TABLE IF EXISTS atividades;
DROP TABLE IF EXISTS votos;

CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);

CREATE TABLE atividades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    categoria TEXT NOT NULL,
    descricao TEXT
);

CREATE TABLE votos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER,
    atividade_id INTEGER,
    FOREIGN KEY(usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY(atividade_id) REFERENCES atividades(id)
);
