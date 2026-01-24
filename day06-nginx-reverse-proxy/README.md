# 🌐 Day 06 — Reverse Proxy com Nginx (Arquitetura de Produção)

## 🎯 Objetivo do projeto

O objetivo do **Day 06** foi introduzir o conceito de **Reverse Proxy**, utilizando o **Nginx** como camada de entrada da aplicação.

Este projeto simula uma arquitetura real de produção, onde serviços internos não são expostos diretamente à internet.

---

## 🧠 O que este projeto faz

* Executa uma API FastAPI em container
* Executa um PostgreSQL em container separado
* Utiliza Nginx como reverse proxy
* Expõe apenas o Nginx para acesso externo
* Mantém a API acessível somente pela rede interna do Docker

---

## 🏗 Arquitetura

```text
Cliente → Nginx (porta 80) → API (porta 8000) → PostgreSQL
```

* 🔓 Porta pública: **80 (Nginx)**
* 🔒 Porta interna: **8000 (API)**
* 🔒 Banco de dados não exposto externamente

---

## 🗂 Estrutura do projeto

```text
day06-nginx-reverse-proxy/
├── api/
│   ├── __init__.py
│   └── main.py
├── nginx/
│   └── default.conf
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── .dockerignore
```

---

## ⚙️ Como funciona

1. O Docker Compose cria uma rede interna entre os serviços
2. O Nginx recebe as requisições externas na porta 80
3. O Nginx encaminha as requisições para a API
4. A API se comunica com o banco de dados internamente
5. Nenhum serviço interno é acessível diretamente pelo host

---

## ▶️ Como rodar o projeto

```bash
docker compose up --build
```

---

## 🧪 Testes esperados

### ✅ Acesso via Nginx (funciona)

```bash
curl http://localhost/health
```

### ❌ Acesso direto à API (não deve funcionar)

```bash
curl http://localhost:8000/health
```

Este comportamento confirma que a API não está exposta externamente.

---

## 🧠 Principais aprendizados

* O que é e para que serve um reverse proxy
* Diferença entre `ports` e `expose` no Docker Compose
* Isolamento de serviços internos
* Uso de DNS interno do Docker
* Base para TLS, load balancing e rate limiting

---

## 📌 Conceito-chave

> A aplicação não deve ser exposta diretamente à internet.
> O acesso externo deve ser controlado por um proxy.

Este projeto representa um padrão comum em ambientes de produção.

---

📌 *Projeto parte da série **9 Days Learning — DevOps & SRE***
