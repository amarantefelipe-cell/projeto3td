## Diagrama
                ┌─────────────┐
                │  base.html  │
                │(layout geral│
                │ cabeçalho,  │
                │ rodapé,     │
                │ navegação)  │
                └─────▲───────┘
                      │
    ┌─────────────────┼─────────────────┐
    │                 │                 │
    │                 │                 │
┌────────────────┐ ┌───────────────┐ ┌──────────────────┐
│ atividades.html│ │ ranking.html  │ │ usuario_form.html│
│(lista de       │ │(ranking de    │ │(formulário       │
│ atividades)    │ │ atividades)   │ │ de usuário)      │
└─────▲──────────┘ └─────▲─────────┘ └─────▲────────────┘
      │                  │                  │
      │                  │                  │
      │                  │                  │
   URL:               URL:               URL:
 /atividades         /ranking          /usuarios/novo

┌────────────────┐
│ atividade_form │
│ (formulário    │
│ de atividade)  │
└─────▲──────────┘
      │
      URL: /atividades/novo

┌───────────────┐
│ voto_form.html│
│(formulário    │
│ de votação)   │
└─────▲─────────┘
      │
      URL: /votos/novo


# README.md

# Projeto Cultura+ - Gestão de Atividades Culturais

## 📌 Objetivo
O projeto **Cultura+** é um sistema em **Python + Flask + SQLite** para:
- Cadastrar usuários.
- Cadastrar atividades culturais.
- Permitir votação em atividades.
- Mostrar ranking das atividades mais votadas.

O sistema será usado como projeto prático para o **3º ano do Ensino Médio - Técnico em Desenvolvimento de Sistemas** e será apresentado na **Feira Cultural**.

---

## 📂 Estrutura de Arquivos

```
cultura_plus/
│── app.py              # Arquivo principal que inicializa o Flask e o banco
│── database.py         # Conexão e inicialização do banco SQLite
│── schema.sql          # Script SQL para criar tabelas
│── routes.py           # Rotas do Flask (API e páginas web)
│── templates/          # Templates HTML
│    ├── base.html         # Layout base de todas as páginas
│    ├── atividades.html   # Lista de atividades
│    ├── ranking.html      # Ranking de atividades por votos
│    ├── usuario_form.html # Formulário de cadastro de usuário
│    ├── atividade_form.html # Formulário de cadastro de atividade
│    └── voto_form.html    # Formulário de votação
│── static/             # Arquivos estáticos (CSS, imagens, JS)
```

---

## 🛠️ Passo a Passo de Implementação

O projeto será feito em **etapas (checkpoints)**. Cada checkpoint gera um sistema funcional parcial.

### ✅ Checkpoint 1 – Banco de Dados
1. Criar `schema.sql` com as tabelas:
   - `usuarios`
   - `atividades`
   - `votos`
2. Criar `database.py` para conectar e inicializar o banco.  
3. Criar `app.py` que importa `database` e roda `init_db()` na primeira execução.  
**Objetivo:** O banco deve ser criado corretamente sem erros.

---

### ✅ Checkpoint 2 – API de Cadastro e Listagem
1. Criar `routes.py` com:
   - `POST /usuarios` → cadastrar usuário via JSON
   - `POST /atividades` → cadastrar atividade via JSON
   - `GET /atividades` → listar atividades
2. Testar com Postman ou cURL.  
**Objetivo:** Cadastrar e listar dados via API JSON.

---

### ✅ Checkpoint 3 – Votos e Ranking
1. Adicionar rotas:
   - `POST /votos` → registrar voto
   - `GET /ranking` → retornar ranking de atividades
2. Testar via Postman.  
**Objetivo:** Já é possível votar e consultar ranking.

---

### ✅ Checkpoint 4 – Interface Web
1. Criar templates HTML em `templates/`:
   - `base.html` → layout geral
   - `atividades.html` → lista de atividades
   - `ranking.html` → ranking
2. Atualizar `routes.py` para renderizar templates usando `render_template`.  
**Objetivo:** Sistema navegável no browser, mesmo que os formulários não estejam implementados.

---

### ✅ Checkpoint 5 – Formulários Web
1. Criar templates HTML para formulários:
   - `usuario_form.html`
   - `atividade_form.html`
   - `voto_form.html`
2. Implementar no `routes.py` as rotas com `GET` e `POST` para salvar dados no banco.
**Objetivo:** Sistema completo, interativo, pronto para a feira.

---

## 🔹 Comandos Essenciais para Rodar (Windows)
```powershell
# Criar ambiente virtual
py -m venv venv

# Instalar Flask
py -m pip install --upgrade pip
py -m pip install flask

# Rodar aplicação
py app.py
```

> Observação: Não é necessário ativar o venv se você usar `py -m pip` e `py app.py`.

---

## 📄 Explicação de Cada Arquivo

- **app.py**: inicializa o Flask e o banco, registra o Blueprint das rotas.
- **database.py**: gerencia conexão e criação das tabelas SQLite.
- **schema.sql**: script SQL que cria as tabelas.
- **routes.py**: define todas as rotas da aplicação (API e páginas web).
- **templates/base.html**: layout principal (cabeçalho, rodapé, navegação).
- **templates/\*.html**: templates que herdam de base.html para conteúdo específico.
- **static/**: pasta para arquivos CSS, imagens e JS da aplicação.

---

## ✅ Dicas
- Teste sempre as rotas no navegador ou Postman antes de avançar.
- Complete os formulários depois que as rotas básicas estiverem funcionando.
- Use comentários no código para indicar tarefas que ainda precisam ser implementadas.
- Cada checkpoint deve gerar algo funcional, mesmo que parcial.

---

