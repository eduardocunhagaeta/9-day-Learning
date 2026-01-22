# 🐘 Day 03 — API + PostgreSQL (Stateful Services)

## 🎯 Objetivo do projeto

O objetivo do **Day 03** foi introduzir **estado** na aplicação, conectando uma API FastAPI a um banco de dados **PostgreSQL** executando em container.

Este projeto marca a transição de aplicações **stateless** para **stateful**, um ponto crítico em ambientes DevOps e SRE.

---

## 🧠 O que este projeto faz

* Executa uma API FastAPI em container
* Executa um PostgreSQL em container separado
* Conecta a API ao banco via rede interna do Docker
* Utiliza variáveis de ambiente para configuração
* Garante persistência de dados via volume

---

## 🗂 Estrutura do projeto

```text
day03-api-postgres/
├── app/
│   ├── __init__.py
│   └── main.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── .dockerignore
```

---

## ⚙️ Como funciona

1. O Docker Compose cria uma rede interna
2. O serviço `db` (Postgres) fica acessível pelo hostname `db`
3. A API lê as credenciais do arquivo `.env`
4. O endpoint `/db-check` valida a conexão com o banco
5. O volume garante persistência dos dados do Postgres

---

## ▶️ Como rodar

```bash
docker compose up --build
```

Testes:

* `http://localhost:8000/health`
* `http://localhost:8000/db-check`

---

## 🧠 Principais aprendizados

* Diferença entre **stateless** e **stateful**
* Uso de volumes para dados persistentes
* Service discovery via Docker DNS
* Uso correto de variáveis de ambiente
* Separação clara entre aplicação e banco

---

## 📌 Conceito-chave

> Containers são descartáveis.
> Dados não.

Este projeto reforça a importância de tratar bancos de dados como serviços **stateful**.

---

📌 *Projeto parte da série **9 Days Learning — DevOps & SRE***
