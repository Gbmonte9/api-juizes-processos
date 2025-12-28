# API de Processos Judiciais

API desenvolvida em **Python** com **FastAPI** para gerenciamento de juízes e processos judiciais, com autenticação JWT, upload de PDFs e geração de relatórios.

---

## 🔹 Tecnologias utilizadas

- Python 3.11+
- FastAPI
- SQLAlchemy (assíncrono)
- PostgreSQL
- Alembic (migrações)
- JWT (autenticação)
- Passlib (hash de senhas)
- Python-Multipart (upload de arquivos)
- ReportLab (geração de PDFs)
- Uvicorn (servidor ASGI)
- Docker & Docker Compose (opcional)

---

## 📁 Estrutura do projeto

```
api-juizes-processos/
├─ app/
│  ├─ __init__.py
│  ├─ main.py
│  ├─ config.py
│  ├─ models.py
│  ├─ database.py
│  ├─ schemas.py
│  ├─ crud.py
│  ├─ deps.py
│  ├─ routers/
│  │  ├─ __init__.py
│  │  ├─ auth.py
│  │  ├─ juizes.py
│  │  └─ processos.py
│  └─ utils/
│     ├─ pdf_generator.py
│     └─ security.py
├─ alembic/
├─ tests/
├─ Dockerfile
├─ docker-compose.yml
├─ requirements.txt
└─ README.md
```

---

## ⚡ Funcionalidades

- Cadastro e login de juízes com autenticação JWT.
- CRUD de juízes e processos.
- Upload de arquivos PDF relacionados aos processos.
- Geração de relatórios em PDF de cada processo.
- Estrutura modular e escalável.

---

## 🚀 Como rodar o projeto

### 1. Clonar o repositório
```bash
git clone <URL_DO_REPOSITORIO>
cd api-juizes-processos
```

### 2. Criar e ativar ambiente virtual
```bash
python3 -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente
Crie um arquivo `.env` na raiz:

```
DATABASE_URL=postgresql+asyncpg://postgres:password@localhost:5432/juizesdb
JWT_SECRET=sua_chave_secreta
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

### 5. Rodar migrações do banco
```bash
alembic upgrade head
```

### 6. Rodar a API
```bash
uvicorn app.main:app --reload
```

Acesse no navegador:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🐳 Rodar com Docker (opcional)

1. Subir containers
```bash
docker-compose up -d
```

2. Ajustar `DATABASE_URL` no `.env` se necessário:
```
DATABASE_URL=postgresql+asyncpg://postgres:password@db:5432/juizesdb
```

3. Rodar a API
```bash
uvicorn app.main:app --reload
```

---

## 🔹 Endpoints principais

- **Auth**
  - `POST /auth/register` → Registrar juiz
  - `POST /auth/login` → Login e token JWT

- **Juízes**
  - `GET /juizes/` → Listar todos os juízes
  - `GET /juizes/me` → Dados do juiz logado
  - `DELETE /juizes/{id}` → Deletar juiz

- **Processos**
  - `POST /processos/{juiz_id}` → Criar processo + upload PDF
  - `GET /processos/` → Listar processos
  - `GET /processos/{id}/pdf` → Baixar relatório PDF

---

## 📌 Observações

- Recomendado usar ambiente virtual e variáveis de ambiente para segurança.
- Uploads de PDF são salvos na pasta `uploads/`.
- Arquitetura modular, pronta para evoluir para microserviços se necessário.

---

## 📝 Autor

**Gabriel Monte**
[LinkedIn](https://www.linkedin.com/in/gabriel-rodrigues-mt/)
[GitHub](https://github.com/Gbmonte9)
