# 🏋️‍♂️ Workout API - Competição de CrossFit

## 📖 Sobre o Projeto
Esta é uma **API RESTful assíncrona** desenvolvida para gerir os dados de uma **competição de CrossFit**.  
A aplicação permite o **registo e a consulta de atletas, categorias e centros de treinamento**, fornecendo uma base sólida para qualquer sistema de gestão de eventos desportivos.

O projeto foi construído utilizando tecnologias modernas do ecossistema Python para desenvolvimento web, com foco em **performance, escalabilidade e boas práticas de desenvolvimento**.

---

## ✨ Funcionalidades
- **Gestão de Atletas**: Operações CRUD completas.  
- **Gestão de Categorias**: Operações CRUD para as categorias da competição.  
- **Gestão de Centros de Treinamento**: Operações CRUD para os CTs participantes.  
- **Assíncrono**: Totalmente construído com `async` e `await` para alta performance.  
- **Documentação Automática**: Interfaces interativas do **Swagger UI** (`/docs`) e **ReDoc** (`/redoc`).  
- **Migrações de Base de Dados**: Controlo de versão com **Alembic**.  

---

## 🛠️ Stack de Tecnologias
- **Linguagem:** Python 3.11+  
- **Framework Web:** FastAPI  
- **Base de Dados:** PostgreSQL (em container Docker)  
- **ORM:** SQLAlchemy 2.0 (asyncio)  
- **Migrações:** Alembic  
- **Validação de Dados:** Pydantic  
- **Servidor ASGI:** Uvicorn  

---

## 📁 Estrutura do Projeto
```bash
├── alembic/              # Scripts e versões de migração do Alembic
├── workoutapi/           # Pacote principal da aplicação
│   ├── contrib/          # Módulos de suporte (ex: conexão com BD)
│   ├── models/           # Modelos de dados do SQLAlchemy
│   ├── routers/          # Endpoints (rotas) da API
│   └── schemas/          # Esquemas de validação de dados do Pydantic
├── .gitignore            # Ficheiros e pastas ignorados pelo Git
├── docker-compose.yml    # Configuração do Docker para o BD
├── alembic.ini           # Configuração do Alembic
└── requirements.txt      # Lista de dependências Python


