# 📈 Day 07 & 08 — Métricas, SLIs e SLOs (Mentalidade SRE)

## 🎯 Objetivo do projeto

Os **Days 07 e 08** tiveram como foco introduzir **métricas e confiabilidade**, pilares fundamentais da cultura **SRE (Site Reliability Engineering)**.

O objetivo foi aprender **o que medir**, **por que medir** e **como essas medições se conectam à experiência do usuário**, antes de utilizar ferramentas como Prometheus.

---

## 🧠 O que este projeto faz (Day 07)

* Instrumenta métricas manualmente na aplicação
* Mede latência por requisição
* Conta volume de tráfego
* Registra métricas em logs estruturados
* Permite observar impacto de falhas no comportamento do sistema

---

## 🗂 Estrutura do projeto

```text
day07-metrics-basics/
├── api/
│   ├── __init__.py
│   └── main.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── .dockerignore
```

---

## ⚙️ Como funciona (Day 07)

1. Um middleware intercepta todas as requisições HTTP
2. O tempo de execução é medido
3. Um contador global registra o número de requisições
4. As métricas são emitidas via logs estruturados (JSON)
5. Cada requisição gera dados quantitativos observáveis

---

## ▶️ Como rodar o projeto

```bash
docker compose up --build
```

Testes:

```bash
curl http://localhost/health
curl http://localhost/error
```

Ver logs:

```bash
docker logs -f day07-metrics-basics-api-1
```

---

## 🔍 Exemplo de métrica registrada

```json
{
  "level": "info",
  "service": "api",
  "event": "request_handled",
  "path": "/health",
  "method": "GET",
  "duration_ms": 2,
  "request_count": 5
}
```

Esses dados representam:

* **Latência** (`duration_ms`)
* **Tráfego** (`request_count`)
* **Dimensão** (`path`, `method`)

---

## 🧠 Day 08 — Conceitos de SLI, SLO e SLA

O **Day 08** foi dedicado exclusivamente à **mentalidade de confiabilidade**, sem adição de código.

### 📌 SLI — Service Level Indicator

O que está sendo medido.

Exemplos:

* Latência das requisições
* Taxa de sucesso (HTTP 200)
* Disponibilidade do serviço

---

### 📌 SLO — Service Level Objective

O nível aceitável de confiabilidade.

Exemplos:

* 99% das requisições devem responder em menos de 300ms
* 99.9% de disponibilidade mensal

---

### 📌 SLA — Service Level Agreement

Contrato formal com o cliente, geralmente com impacto financeiro.

📌 Em SRE, o foco técnico está em **SLIs e SLOs**, não em SLAs.

---

## 🧠 Relação com o projeto

As métricas instrumentadas no **Day 07** servem como base direta para definição de **SLIs**, que por sua vez permitem estabelecer **SLOs realistas**, orientados à experiência do usuário.

---

## 📌 Conceitos-chave

> Logs explicam *o que aconteceu*.
> Métricas explicam *quão grave foi*.

> Não se monitora tudo.
> Monitora-se o que impacta o usuário.

---

## 🏁 Conclusão

Este projeto estabelece a base para práticas avançadas de observabilidade, confiabilidade e definição de objetivos de serviço, preparando o terreno para o uso de ferramentas como Prometheus e Grafana.

---

📌 *Projeto parte da série **9 Days Learning — DevOps & SRE***
