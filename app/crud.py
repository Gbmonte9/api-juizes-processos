from sqlalchemy.future import select
from sqlalchemy import insert
from .models import Juiz, Processo
from .utils.security import hash_password, verify_password

async def create_juiz(db, nome, email, senha):
    senha_hash = hash_password(senha)
    novo = Juiz(nome=nome, email=email, senha_hash=senha_hash)
    db.add(novo)
    await db.commit()
    await db.refresh(novo)
    return novo

async def authenticate_juiz(db, email, senha):
    q = await db.execute(select(Juiz).where(Juiz.email == email))
    juiz = q.scalars().first()
    if not juiz:
        return None
    if not verify_password(senha, juiz.senha_hash):
        return None
    return juiz

async def create_processo(db, juiz_id, numero, parte=None, descricao=None, pdf_filename=None):
    p = Processo(numero=numero, parte=parte, descricao=descricao, pdf_filename=pdf_filename, juiz_id=juiz_id)
    db.add(p)
    await db.commit()
    await db.refresh(p)
    return p
