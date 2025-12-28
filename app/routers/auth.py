from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from .. import schemas, crud, database
from ..utils.security import create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=schemas.JuizOut)
async def register(payload: schemas.JuizCreate, db: AsyncSession = Depends(database.get_db)):
    exists = await db.execute(select(Juiz).where(Juiz.email == payload.email))
    if exists.scalars().first():
        raise HTTPException(400, "Email já cadastrado")
    juiz = await crud.create_juiz(db, payload.nome, payload.email, payload.senha)
    return juiz

@router.post("/login")
async def login(form_data: dict, db: AsyncSession = Depends(database.get_db)):
    email = form_data.get("email")
    senha = form_data.get("senha")
    juiz = await crud.authenticate_juiz(db, email, senha)
    if not juiz:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    token = create_access_token({"sub": str(juiz.id)})
    return {"access_token": token, "token_type": "bearer"}
