from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from database import get_connection

# Definindo o Blueprint
routes = Blueprint("routes", __name__)

# === Usuários ===
@routes.route("/usuarios/novo", methods=["GET", "POST"])
def criar_usuario_form():
    # TODO: Implementar formulário HTML
    # Dica: usar request.form["nome"], request.form["email"]
    # Depois redirecionar para /atividades
    ...

# === Atividades ===
@routes.route("/atividades/novo", methods=["GET", "POST"])
def criar_atividade_form():
    # TODO: Implementar formulário HTML
    # Dica: usar request.form e salvar no banco
    ...

@routes.route("/atividades", methods=["GET"])
def listar_atividades_html():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM atividades")
    atividades = [dict(row) for row in cur.fetchall()]
    return render_template("atividades.html", atividades=atividades)

# === Votos ===
@routes.route("/votos/novo", methods=["GET", "POST"])
def votar_form():
    # TODO: Criar formulário HTML
    # Deve listar usuários e atividades em <select>
    ...

@routes.route("/ranking", methods=["GET"])
def ranking_html():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT a.titulo, COUNT(v.id) as votos
        FROM atividades a
        LEFT JOIN votos v ON a.id = v.atividade_id
        GROUP BY a.id
        ORDER BY votos DESC
    """)
    ranking = [dict(row) for row in cur.fetchall()]
    return render_template("ranking.html", ranking=ranking) #teste
