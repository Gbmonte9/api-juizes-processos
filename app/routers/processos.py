from fastapi import APIRouter, File, UploadFile, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from .. import database, crud
import shutil
import os

router = APIRouter(prefix="/processos", tags=["processos"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/{juiz_id}/", response_model=schemas.ProcessoOut)
async def create_processo(juiz_id: int, numero: str, file: UploadFile | None = None, db: AsyncSession = Depends(database.get_db)):
    filename = None
    if file:
        if not file.content_type in ("application/pdf",):
            raise HTTPException(400, "Apenas PDFs são permitidos")
        filename = f"{numero}_{file.filename}"
        with open(os.path.join(UPLOAD_DIR, filename), "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    processo = await crud.create_processo(db, juiz_id, numero, descricao=None, pdf_filename=filename)
    return processo
