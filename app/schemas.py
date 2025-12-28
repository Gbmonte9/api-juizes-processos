from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class JuizCreate(BaseModel):
    nome: str
    email: str
    senha: str

class JuizOut(BaseModel):
    id: int
    nome: str
    email: str
    class Config:
        orm_mode = True

class ProcessoCreate(BaseModel):
    numero: str
    parte: Optional[str] = None
    descricao: Optional[str] = None

class ProcessoOut(BaseModel):
    id: int
    numero: str
    parte: Optional[str]
    status: str
    criado_em: datetime
    class Config:
        orm_mode = True
