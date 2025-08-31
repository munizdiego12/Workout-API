from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from workoutapi.contrib.database import async_session

async def get_db_session() -> AsyncSession:
    """
    Função geradora que cria e gerencia a sessão com o banco de dados.
    Garante que a sessão seja sempre fechada após o uso.
    """
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()

# Cria um 'apelido' para a nossa dependência, para ser usado nos endpoints
DatabaseDependency = Annotated[AsyncSession, Depends(get_db_session)]
