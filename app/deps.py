from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from .config import settings
from .database import get_db
from .models import Juiz

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def get_current_juiz(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db),
):
    try:
        payload = jwt.decode(
            token,
            settings.jwt_secret,
            algorithms=[settings.jwt_algorithm]
        )
        juiz_id: str = payload.get("sub")
        if juiz_id is None:
            raise HTTPException(status_code=401, detail="Token inválido")

    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

    query = await db.execute(select(Juiz).where(Juiz.id == int(juiz_id)))
    juiz = query.scalars().first()

    if juiz is None:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")

    return juiz
