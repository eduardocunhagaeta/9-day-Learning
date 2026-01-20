# 📦 Day 02 — Docker Compose com Hot Reload (Ambiente de Desenvolvimento)

## 🎯 Objetivo do projeto

O objetivo do **Day 02** foi evoluir o projeto do Dia 01 para um **ambiente de desenvolvimento real**, utilizando **Docker Compose** para orquestrar o container e permitir **hot reload**, aumentando produtividade sem comprometer boas práticas de produção.

Este projeto foca na **diferença clara entre desenvolvimento e produção** em aplicações containerizadas.

---

## 🧠 O que este projeto faz

Este projeto executa uma **API simples em FastAPI**, agora utilizando:

* Docker Compose
* Bind mounts (volumes)
* Hot reload com Uvicorn
* Subida do ambiente com um único comando

Ao editar o código localmente, as alterações são refletidas **instantaneamente** no container, sem necessidade de rebuild da imagem.

---

## 🗂 Estrutura do projeto

```text
day02-docker-compose-dev/
├── app/
│   ├── __init__.py
│   └── main.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
└── .gitignore
```

---

## ⚙️ Como funciona (fluxo técnico)

1. O **Dockerfile** define como a imagem é construída
2. O **Docker Compose** define como o container é executado
3. O diretório `app/` é montado como **volume**
4. O Uvicorn roda com a flag `--reload`
5. Alterações no código reiniciam automaticamente a aplicação

Esse fluxo separa claramente:

* **Build (imagem)** → Dockerfile
* **Execução (ambiente)** → Docker Compose

---

## ▶️ Como rodar o projeto

Na pasta do projeto:

```bash
docker compose up
```

Acesse:

* `http://localhost:8000/health`
* `http://localhost:8000/docs`

---

## 🔥 Principais aprendizados

* Diferença entre `COPY` e bind mount (`volumes`)
* Por que hot reload **não deve ser usado em produção**
* Docker Compose como ferramenta de desenvolvimento
* Separação clara entre ambientes (dev vs prod)
* Como sobrescrever o comando do container via Compose

---

## 🧠 Conceito importante

> Em ambientes profissionais, **produção é imutável**.
> Mudanças de código devem gerar novas imagens e novos deploys, não reloads em runtime.

Este projeto representa **exclusivamente o ambiente de desenvolvimento**.

---

## 🏁 Conclusão

O **Day 02** consolida o uso do Docker Compose como ferramenta essencial para evitar rebuilds constantes, melhorar produtividade e manter uma base sólida para evolução futura da aplicação.

Este setup é amplamente utilizado em times de backend, DevOps e SRE no dia a dia.

---

📌 *Projeto parte da série **9 Days Learning — DevOps & SRE***
