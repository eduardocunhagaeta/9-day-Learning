# 📊 Day 05 — Logging & Observabilidade (Fundação SRE)

## 🎯 Objetivo do projeto

O objetivo do **Day 05** foi introduzir conceitos fundamentais de **observabilidade**, com foco em **logging estruturado** para aplicações containerizadas.

Este projeto demonstra como preparar uma aplicação para ambientes de produção, garantindo que seu comportamento possa ser analisado apenas a partir dos logs.

---

## 🧠 O que este projeto faz

* Executa uma API FastAPI em container
* Emite logs estruturados em formato JSON
* Envia logs exclusivamente para stdout
* Remove access logs verbosos do framework
* Mantém compatibilidade com ferramentas de observabilidade

---

## 🗂 Estrutura do projeto

```text
day05-logging-and-observability/
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

1. A aplicação utiliza o módulo `logging` do Python
2. Os logs são emitidos em formato JSON
3. As mensagens são enviadas para stdout
4. O Docker captura automaticamente os logs
5. Ferramentas externas podem coletar e processar esses logs

---

## ▶️ Como rodar o projeto

```bash
docker compose up
```

Ver logs da aplicação:

```bash
docker logs -f day05-logging-and-observability-api-1
```

---

## 🔍 Exemplo de log estruturado

```json
{
  "level": "info",
  "service": "api",
  "event": "db_connection_success"
}
```

---

## 🧠 Principais aprendizados

* Diferença entre log de framework e log de aplicação
* Importância de logs estruturados
* Uso correto de stdout/stderr em containers
* Por que não salvar logs em arquivos em ambientes containerizados
* Base para integração com ELK, Loki, Cloud Logging, entre outros

---

## 📌 Conceito-chave

> Se você não consegue entender o comportamento da aplicação apenas pelos logs,
> então você não tem observabilidade.

Este projeto estabelece a base para práticas avançadas de SRE e DevOps.

---

📌 *Projeto parte da série **9 Days Learning — DevOps & SRE***
