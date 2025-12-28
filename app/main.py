from fastapi import FastAPI
from .routers import auth, juizes, processos

app = FastAPI(title="API de Processos Judiciais")

# Registrar Rotas
app.include_router(auth.router)
app.include_router(juizes.router)
app.include_router(processos.router)

@app.get("/")
async def root():
    return {"message": "API de Processos Judiciais funcionando!"}
