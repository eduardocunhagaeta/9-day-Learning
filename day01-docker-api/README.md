# 📦 Day 01 — Docker + FastAPI
O que é

Uma API simples construída com FastAPI, totalmente containerizada com Docker, expondo um endpoint de healthcheck e documentação automática.

O que foi aprendido

 - Criação de imagens Docker
 - Diferença entre build e run
 - Debug de erros dentro de containers
 - Exposição de portas
 - Uso correto de Uvicorn
 - Healthcheck básico para serviços

Como rodar:

 - docker build -t day01-api .
 - docker run -p 8000:8000 day01-api

Acesse:

 - http://localhost:8000/health
 - http://localhost:8000/docs
