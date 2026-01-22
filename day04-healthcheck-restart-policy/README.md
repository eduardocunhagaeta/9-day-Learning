# ❤️‍🩹 Day 04 — Healthcheck e Restart Policy (Resiliência)

## 🎯 Objetivo do projeto

O objetivo do **Day 04** foi adicionar **resiliência** à stack do Dia 03, ensinando o Docker a identificar serviços **saudáveis** e a se recuperar automaticamente em caso de falhas.

Este projeto introduz conceitos fundamentais de **auto-healing**, base do SRE moderno.

---

## 🧠 O que este projeto faz

* Mantém a stack API + PostgreSQL
* Implementa healthcheck na API
* Aplica restart policy automática
* Permite detecção e recuperação de falhas

---

## 🗂 Estrutura do projeto

```text
day04-healthcheck-restart-policy/
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

1. O Docker executa periodicamente o endpoint `/health`
2. Se a API falhar, o container fica `unhealthy`
3. Com a restart policy, o Docker reinicia o serviço
4. O banco permanece intacto via volume

---

## ▶️ Como rodar

```bash
docker compose up
```

Verificar saúde:

```bash
docker ps
```

---

## 🧠 Principais aprendizados

* Diferença entre **rodando** e **saudável**
* Healthcheck como sinal para orquestradores
* Restart policy como mecanismo de recuperação
* Base conceitual de liveness/readiness probes

---

## 📌 Conceito-chave

> Serviço disponível não é necessariamente serviço saudável.

Este projeto demonstra como detectar e reagir a falhas automaticamente.

---

📌 *Projeto parte da série **9 Days Learning — DevOps & SRE***
