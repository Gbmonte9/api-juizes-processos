from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .. import database, schemas, crud, models
from ..deps import get_current_juiz

router = APIRouter(
    prefix="/juizes",
    tags=["juizes"]
)

@router.get("/", response_model=list[schemas.JuizOut])
async def listar_juizes(db: AsyncSession = Depends(database.get_db)):
    result = await db.execute(select(models.Juiz))
    return result.scalars().all()


@router.get("/me", response_model=schemas.JuizOut)
async def dados_meu_perfil(juiz=Depends(get_current_juiz)):
    return juiz


@router.delete("/{juiz_id}")
async def deletar_juiz(juiz_id: int, db: AsyncSession = Depends(database.get_db)):
    result = await db.execute(select(models.Juiz).where(models.Juiz.id == juiz_id))
    juiz = result.scalars().first()

    if not juiz:
        raise HTTPException(404, "Juiz não encontrado.")

    await db.delete(juiz)
    await db.commit()
    return {"message": "Juiz deletado com sucesso."}
